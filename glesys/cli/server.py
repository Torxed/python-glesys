import json

from ..output import log
from ..session import api


def server_entrypoint(args, **kwargs):
	if args.all_servers:
		print(json.dumps(api.server.list(), indent=4))