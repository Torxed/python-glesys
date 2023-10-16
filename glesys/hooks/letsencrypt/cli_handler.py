import json
import logging
import datetime
import pathlib
import time

from ...output import log, stylize_output
from ...session import session
from ...workers import SysCommandWorker

def has_expired(date):
	
	expiry_date = datetime.datetime.fromtimestamp(
		time.mktime(
			time.strptime(date, '%Y-%m-%d')
		)
	)

	if (expiry_date - datetime.datetime.now()).total_seconds() > 0:
		return False

	return True


def letsencrypt_entrypoint(args, **kwargs):
	if args.all_domains:
		for path in ['/etc/letsencrypt/.certbot.lock', '/var/log/letsencrypt/.certbot.lock', '/var/lib/letsencrypt/.certbot.lock']:
			if pathlib.Path(path).exists():
				raise KeyError(f"Another instance of certbot is already running: {path}")

		certbot_domain_string = ""

		log(f"Fetching all domains at Glesys accessible by account {session['configuration'].credentials.user}", fg="blue", level=logging.INFO)

		debug_output_domains = 0
		domains = []
		for domain in session['api'].dns.all_domains():
			if domain.get('usingglesysnameserver') == "no" and args.no_ignores is False:
				log(f"Ignoring domain {domain['domainname']} - not using Glesys nameserver", fg="gray", level=logging.INFO)
				continue

			if has_expired(domain.get('registrarinfo', {}).get('expire')):
				log(f"Ignoring domain {domain['domainname']} - has expired", fg="gray", level=logging.DEBUG)
				continue

			certbot_domain_string += f"*.{domain['domainname']},{domain['domainname']},"
			debug_output_domains += 1
			domains.append(domain['domainname'])

		log(f"Requesting new certificates using LetsEncrypt for {debug_output_domains} domains", fg="blue", level=logging.INFO)
		if args.verbose:
			log(f" ╷", fg="gray", level=logging.INFO)
			for index, domain in enumerate(domains):
				log(f" {'├' if index != len(domains)-1 else '└'}─ {domain}", fg="gray", level=logging.INFO)

		certbot_cmd_string = "certbot certonly --non-interactive"
		if args.verbose:
			certbot_cmd_string += ' --verbose'
		certbot_cmd_string += " --authenticator dns-glesys"
		certbot_cmd_string += " --preferred-challenges dns"
		certbot_cmd_string += f" --work-dir {args.workdir.resolve()}"
		certbot_cmd_string += f" --logs-dir {args.logsdir.resolve()}"
		certbot_cmd_string += f" --config-dir {args.confdir.resolve()}"
		certbot_cmd_string += " --text --agree-tos --email anton@hvornum.se"
		certbot_cmd_string += " --expand --renew-by-default"
		certbot_cmd_string += " --manual-auth-hook /tmp/exit.sh"
		if args.production:
			certbot_cmd_string += " --server https://acme-v02.api.letsencrypt.org/directory"
		else:
			certbot_cmd_string += " --dry-run"
			certbot_cmd_string += " --server https://acme-staging-v02.api.letsencrypt.org/directory"
		certbot_cmd_string += f" -d '{certbot_domain_string[:-1]}'"

		with open('/tmp/exit.sh', 'w') as fh:
			fh.write('#!/bin/bash\nexit(0)\n')

		if args.verbose:
			log(f"Executing: {certbot_cmd_string}", fg="gray", level=logging.INFO)

		# chmod +x /tmp/exit.sh
		worker = SysCommandWorker(certbot_cmd_string, peek_output=args.verbose)

		while worker.is_alive():
			time.sleep(1)


		log(f"Certificates have been generated successfully", fg="green", level=logging.INFO)