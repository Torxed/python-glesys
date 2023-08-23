import json
import pathlib
from .output import log
from .models.configuration import Configuration

"""
Configuration will be loaded from a few different locations.
./glesys.toml has priority over /etc/glesys/glesys.toml but
--conf will override any other location.
"""

def load_configuration():
	from .session import session

	args = session['args']
	conf_location = None
	print(args)
	if 'conf' in dir(args) and args.conf:
		if args.conf.exists() is False:
			raise PermissionError(f"Could not load --conf from {args.conf}, file does not exist or permission error.")
		log(f"Loading default confuration from --conf {args.conf}", fg="gray")
		conf_location = args.conf
	elif (path := pathlib.Path('./glesys.toml')).exists():
		conf_location = path
	elif (path := pathlib.Path('/etc/glesys/glesys.toml')).exists():
		conf_location = path

	try:
		# Py3.10+
		import tomllib
		file_mode = 'rb'
	except:
		# Py3.9 or below (external dep needed)
		import toml as tomllib
		file_mode = 'r'

	with conf_location.open(file_mode) as f:
		configuration = Configuration(**tomllib.load(f))

	return configuration