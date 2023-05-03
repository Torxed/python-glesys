from .api import API
from .configuration import configuration

api = API(
	user=configuration.credentials.user,
	key=configuration.credentials.key,
	host=configuration.network.host
)