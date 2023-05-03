import pydantic

from .dns import DNS
from .server import Server
from .ip import IP


class API(pydantic.BaseModel):
	"""
	This class serves as a router/gateway to the
	different endpoints in the API.

	/domain/list for instance lives under api.dns
	"""
	user :str
	key :str
	host :str

	dns :DNS = DNS()
	server :Server = Server()
	ip :IP = IP()