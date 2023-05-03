import pydantic
import json
import logging
import urllib.error

from ..output import log
from ..helpers import post_request, get_request


class Server(pydantic.BaseModel):
	base_endpoint = "/server"

	def _fuzzy_find(self, server):
		if not (server_info := list(self.find(hostname=server, server_id=server))):
			raise ValueError(f"Could not find server with name={server} or server_id={name}")

		if len(server_info) > 1:
			raise ValueError(f"Multiple servers found with the name/server_id of {server}")
		else:
			server_info = server_info[0]

		return server_info

	def list(self):
		from ..session import configuration
		
		log(f"Listing all servers accessible by user {configuration.credentials.user}", fg="gray", level=logging.INFO)
		data = get_request(f'{self.base_endpoint}/list')

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('servers', [])

	def find(self, lazy=False, **kwargs):
		"""
		Due to the amount of properties on a server, this function
		can take any ambigious top-level property of the server detail listing
		and match on anonymous parameters via **kwargs.

		For instance:
		api.server.find(description="some description") will look in the
		/server/list result for any server containing info.get('description') == "some description"

		Adding --lazy to the search will perform:
		"some description" in info.get('description') instead
		"""
		from ..cli.args import args

		log(f"Trying to locate server based on search parameters lazy={lazy} and {kwargs}", fg="gray", level=logging.INFO)

		for server in self.list():
			for key in kwargs:
				if kwargs[key] is None:
					continue

				if lazy:
					if kwargs[key].lower() in str(server.get(key)):
						yield server
						break
				if str(server.get(key)).lower() == kwargs[key].lower():
					yield server
					break

	def details(self, server):
		server_info = self._fuzzy_find(server)

		data = get_request(f"{self.base_endpoint}/details?serverid={server_info['serverid']}")

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('server', {})

	def networkadapters(self, server):
		server_info = self._fuzzy_find(server)

		data = get_request(f"{self.base_endpoint}/networkadapters?serverid={server_info['serverid']}")

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('networkadapters', {})

	def status(self, server):
		server_info = self._fuzzy_find(server)

		data = get_request(f"{self.base_endpoint}/status?serverid={server_info['serverid']}")

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('server', {})

	def limits(self, server):
		server_info = self._fuzzy_find(server)

		try:
			data = get_request(f"{self.base_endpoint}/limits?serverid={server_info['serverid']}")
		except urllib.error.HTTPError as error:
			if error.status == 400:
				data = json.loads(error.read().decode())
			else:
				raise error

		if (status := data.get('response', {}).get('status', {}).get('code')) == 200:
			return data.get('response', {}).get('server', {})
		elif status == 400:
			reason = data.get('response', {}).get('status', {}).get('text')
			log(f"Could not get limits of this server: {reason}", fg="gray", level=logging.INFO)
			return {}

	def costs(self, server):
		server_info = self._fuzzy_find(server)

		data = get_request(f"{self.base_endpoint}/costs?serverid={server_info['serverid']}")

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('costs', {})

	def estimatedcost(self, server):
		"""
		This API endpoint takes an existing serverid or
		a server spec and convert that to an estimated cost.
		"""

		return {} # Returns 400 Bad Request currently

		server_info = self._fuzzy_find(server)

		data = post_request(f"{self.base_endpoint}/estimatedcost", {'serverid' : server_info['serverid']})

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('estimatedcost', {})

	