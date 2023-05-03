import pydantic
import urllib.request
import json
import base64
import logging
import sys

from ..output import log


def get_request(endpoint):
	from ..session import configuration

	credentials = base64.b64encode(f"{configuration.credentials.user}:{configuration.credentials.key}".encode())

	req = urllib.request.Request(f"{configuration.network.host}{endpoint}")
	req.add_header('Accept', 'application/json; charset=utf-8')
	req.add_header('Authorization', f'Basic {credentials.decode()}')

	response = urllib.request.urlopen(req)

	return response.read()


def post_request(endpoint, payload):
	from ..session import configuration

	credentials = base64.b64encode(f"{configuration.credentials.user}:{configuration.credentials.key}".encode())

	req = urllib.request.Request(f"{configuration.network.host}{endpoint}")
	req.add_header('Content-Type', 'application/json; charset=utf-8')
	req.add_header('Authorization', f'Basic {credentials.decode()}')

	json_payload = json.dumps(payload).encode('utf-8')
	
	req.add_header('Content-Length', len(json_payload))
	response = urllib.request.urlopen(req, json_payload)

	response_data = json.loads(response.read().decode())

	return response_data


class DNS(pydantic.BaseModel):
	def all_domains(self):
		from ..session import configuration
		
		log(f"Listing all domains for user {configuration.credentials.user}", fg="gray", level=logging.DEBUG)
		response = get_request('/domain/list/')

		data = json.loads(response.decode())

		if data.get('response', {}).get('status', {}).get('code') == 200:
			return data.get('response', {}).get('domains', [])

	def all_records(self, domain):
		log(f"Listing all records for domain: {domain}", fg="gray", level=logging.DEBUG)
		response = post_request('/domain/listrecords/', {'domainname' : domain})

		if response.get('response', {}).get('status', {}).get('code') == 200:
			return response.get('response', {}).get('records', [])

	def find(self, domain, record=None, type=None, data=None):
		log(f"Performing a search on domain {domain} using query record={record}, type={type}, data={data}", fg="gray", level=logging.DEBUG)
		for dns_entry in self.all_records(domain):
			if all([
				record is None or record == dns_entry.get('host'),
				type is None or type == dns_entry.get('type'),
				data is None or data in dns_entry.get('data')
			]):
				yield dns_entry

	def add_record(self, domain, record):
		if '--verbose' in sys.argv:
			log(f"Attempting to add a record in domain {domain} with the data {record}", fg="gray", level=logging.INFO)

		record_data = {
			**{'ttl' : 360, 'domainname' : domain},
			**record
		}

		if (
			response := post_request('/domain/addrecord', record_data)
		).get('response', {}).get('status', {}).get('code') != 200:
			raise PermissionError(f"Could not create record {record_data} due to: {response}")

		return True

	def delete_record(self, domain, record):
		if '--verbose' in sys.argv:
			log(f"Attempting to delete all records in domain {domain} matching {record}", fg="gray", level=logging.INFO)

		for dns_entry in self.find(domain=domain, record=record.get('host'), type=record.get('type'), data=record.get('data')):
			log(f"Deleting record {dns_entry}", fg="gray", level=logging.DEBUG)

			if (response := post_request('/domain/deleterecord', {
				'recordid' : dns_entry.get('recordid')
			}).get('response', {}).get('status', {}).get('code')) != 200:
				raise PermissionError(f"Could not delete record {dns_entry} due to: {response}")

		return True


class API(pydantic.BaseModel):
	user :str
	key :str
	host :str

	dns :DNS = DNS()