import json

from ..output import log, stylize_output
from ..session import api


def dns_entrypoint(args, **kwargs):
	if args.all_domains:
		result = json.dumps(api.dns.all_domains(), indent=4)
		if args.color:
			result = result.replace('"usingglesysnameserver": "no",', stylize_output('"usingglesysnameserver": "no",', fg="orange"))
			result = result.replace('"state": "EXPIRING60",', stylize_output('"state": "EXPIRING60",', fg="red"))
		print(result)
	elif args.all_records:
		print(json.dumps(api.dns.all_records(args.domain), indent=4))

	elif args.find:
		print(list(api.dns.find(domain=args.domain, record=args.record, type=args.type, data=args.data)))

	elif args.add:
		api.dns.add_record(args.domain, {
			'host': args.record,
			'data': args.data,
			'type': args.type,
			'ttl': args.ttl
		})

	elif args.delete:
		api.dns.delete_record(args.domain, {
			'host': args.record,
			'data': args.data,
			'type': args.type,
			'ttl': args.ttl
		})