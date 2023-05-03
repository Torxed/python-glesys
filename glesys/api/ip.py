import pydantic
import json
import logging
import urllib.error

from ..output import log
from ..helpers import post_request, get_request


class IP(pydantic.BaseModel):
	base_endpoint = "/ip"

	def listfree(self):
		from ..session import configuration
		from ..cli.args import args
		
		log(f"Listing all IP's accessible by user {configuration.credentials.user}", fg="gray", level=logging.INFO)
		try:
			data = post_request(f'{self.base_endpoint}/listfree', {
				"ipversion": args.ipversion,
				"datacenter": args.datacenter,
				"platform": args.platform
			})
		except urllib.error.HTTPError as error:
			if error.status == 400:
				data = json.loads(error.read().decode())
			else:
				raise error

		if (status := data.get('response', {}).get('status', {}).get('code')) == 200:
			return data.get('response', {}).get('iplist', [])
		elif status == 400:
			reason = data.get('response', {}).get('status', {}).get('text')
			log(f"Could not get free IP's: {reason.strip()}", fg="orange", level=logging.ERROR)
			return {}