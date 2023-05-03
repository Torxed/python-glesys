from .cli.args_router import loaded
from .cli.args import load_arguments

session = None
__version__ = "0.2"

def run_as_a_module():
	# global session

	args = load_arguments()
	
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
	
	if 'func' in dir(args):
		args.func(args)