"""DNS Authenticator for slimDNS."""
import json
import logging
import sys

import urllib
import zope.interface
import psycopg2, psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from certbot import errors
from certbot import interfaces
from certbot.plugins import dns_common

from ...output import log
from ...session import api

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
	"""DNS Authenticator for ISPConfig

	This Authenticator uses the ISPConfig Remote REST API to fulfill a dns-01 challenge.
	"""

	description = ('Obtain certificates using a DNS TXT record.')
	ttl = 60

	def __init__(self, *args, **kwargs):
		super(Authenticator, self).__init__(*args, **kwargs)

	def _setup_credentials(self):
		# Just have to be here for certbot reasons
		return True

	def more_info(self): # pylint: disable=missing-docstring,no-self-use
		return 'This plugin configures a DNS TXT record to respond to a dns-01 challenge using ' + \
			   'the Glesys API DNS endpoint.'

	def _perform(self, domain, validation_name, validation):
		api.dns.add_record(domain, {
			'host': validation_name,
			'data': validation,
			'type': 'TXT',
			'ttl': self.ttl
		})

	def _cleanup(self, domain, validation_name, validation):
		api.dns.delete_record(domain, {
			'host': validation_name,
			'data': validation,
			'type': 'TXT',
			'ttl': self.ttl
		})