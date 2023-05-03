import json

from ..output import log
from ..session import api


def server_entrypoint(args, **kwargs):
	if args.all_servers:
		print(json.dumps(api.server.list(), indent=4))

	elif args.find:
		servers = api.server.find(
			hostname=args.name,
			description=args.description,
			datacenter=args.datacenter,
			platform=args.platform,
			iplist=args.ip,
			state=args.state,
			lazy=args.lazy
		)

		for server in servers:
			print(json.dumps(server, indent=4))

	elif args.details:
		print(json.dumps(api.server.details(args.details), indent=4))
	elif args.adapters:
		print(json.dumps(api.server.networkadapters(args.adapters), indent=4))
	elif args.status:
		print(json.dumps(api.server.status(args.status), indent=4))
	