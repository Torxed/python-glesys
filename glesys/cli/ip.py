import json

from ..output import log
from ..session import api


def ip_entrypoint(args, **kwargs):
	if args.list_free:
		print(json.dumps(api.ip.listfree(), indent=4))