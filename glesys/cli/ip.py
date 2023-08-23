import json

from ..output import log
from ..session import session


def ip_entrypoint(args, **kwargs):
	if args.list_free:
		print(json.dumps(session['api'].ip.listfree(), indent=4))