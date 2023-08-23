import json

from ..output import log
from ..session import session


def server_entrypoint(args, **kwargs):
	if args.all_servers:
		print(json.dumps(session['api'].server.list(), indent=4))

	elif args.find:
		servers = session['api'].server.find(
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
		print(json.dumps(session['api'].server.details(args.details), indent=4))
	elif args.adapters:
		print(json.dumps(session['api'].server.networkadapters(args.adapters), indent=4))
	elif args.status:
		print(json.dumps(session['api'].server.status(args.status), indent=4))
	elif args.limits:
		print(json.dumps(session['api'].server.limits(args.limits), indent=4))
	elif args.costs:
		print(json.dumps(session['api'].server.costs(args.costs), indent=4))
	elif args.est_costs:
		print(json.dumps(session['api'].server.estimatedcost(args.est_costs), indent=4))
	