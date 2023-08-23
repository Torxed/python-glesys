from .cli.args_router import loaded
from .cli.args import load_arguments
from .configuration import load_configuration
from .api import API
from .session import session

__version__ = "0.2"

def init_session():
	session['args'] = load_arguments()
	session['configuration'] = load_configuration()
	session['api'] = API(
		user=session['configuration'].credentials.user,
		key=session['configuration'].credentials.key,
		host=session['configuration'].network.host
	)

def run_as_a_module():
	# global session
	init_session()
	
	# import importlib
	# import sys
	# import pathlib

	# Load .git version before the builtin version
	# if pathlib.Path('./glesys/session.py').absolute().exists():
	# 	spec = importlib.util.spec_from_file_location("session", "./glesys/session.py")
	# 	session = importlib.util.module_from_spec(spec)
	# 	sys.modules["session"] = session
	# 	spec.loader.exec_module(sys.modules["session"])
	# else:
	# 	import glesys.session
	
	if 'func' in dir(session['args']):
		session['args'].func(session['args'])

if __name__ in ('__main__', 'glesys'):
	init_session()