import pydantic
import json
import logging

from ..output import log
from ..helpers import post_request, get_request


class Server(pydantic.BaseModel):
	base_endpoint = "/server"

	def list(self):
		from ..session import configuration
		
		log(f"Listing all servers accessible by user {configuration.credentials.user}", fg="gray", level=logging.INFO)
		data = get_request(f'{self.base_endpoint}/list')

		print(data)

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('servers', [])