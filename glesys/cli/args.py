import pathlib
import argparse
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

subparsers = parser.add_subparsers(help="Sub-commands help")

def load_arguments():
	args, unknowns = parser.parse_known_args()
	return args