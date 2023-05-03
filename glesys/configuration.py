import json
import pathlib
from .cli.args import args
from .output import log
from .models.configuration import Configuration

"""
Configuration will be loaded from a few different locations.
./glesys.toml has priority over /etc/glesys/glesys.toml but
--config will override any other location.
"""

config_location = None
if 'config' in dir(args) and args.config:
	if args.config.exists() is False:
		raise PermissionError(f"Could not load --conf from {args.config}, file does not exist or permission error.")
	log(f"Loading default configuration from --conf {args.config}", fg="gray")
	config_location = args.config
elif (path := pathlib.Path('./glesys.toml')).exists():
	config_location = path
elif (path := pathlib.Path('/etc/glesys/glesys.toml')).exists():
	config_location = path

try:
	# Py3.10+
	import tomllib
	file_mode = 'rb'
except:
	# Py3.9 or below (external dep needed)
	import toml as tomllib
	file_mode = 'r'

with config_location.open(file_mode) as f:
	configuration = Configuration(**tomllib.load(f))