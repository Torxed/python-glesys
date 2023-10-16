import pathlib
import argparse
import logging
import psutil
import os
# https://towardsdatascience.com/dynamically-add-arguments-to-argparse-python-patterns-a439121abc39

parser = argparse.ArgumentParser("glesys")
parser.add_argument(
	"--verbose",
	required=False,
	action="store_true",
	default=False,
	help="Increase verbosity",
)
parser.add_argument(
	"--conf",
	required=False,
	type=pathlib.Path,
	default=pathlib.Path('/etc/glesys/glesys.toml'),
	help="Which configuration file to use",
)

subparsers = None
args = None

def load_arguments():
	# Detect if we're running interactively or not,
	# if we're running via python we most likely via entrypoint.
	if psutil.Process(os.getppid()).name() not in ["python", ]:
		global subparsers

		trigger_load = False
		if not subparsers:
			trigger_load = True
			subparsers = parser.add_subparsers(help="Sub-commands help")

		from ..output import log

		log("Loading cli arguments", fg="gray", level=logging.DEBUG)
		from .arguments.dns import parser_dns
		from .arguments.letsencrypt import parser_letsencrypt
		from .arguments.server import parser_server
		from .arguments.ip import parser_ip

		log("Processing arguments", fg="gray", level=logging.DEBUG)
		if trigger_load:
			global args
			args, unknowns = parser.parse_known_args()

		return args