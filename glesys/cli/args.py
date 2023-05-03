import argparse
# https://towardsdatascience.com/dynamically-add-arguments-to-argparse-python-patterns-a439121abc39
args = None

parser = argparse.ArgumentParser("glesys")
parser.add_argument(
	"--verbose",
	required=False,
	action="store_true",
	default=False,
	help="Increase verbosity",
)

subparsers = parser.add_subparsers(help="Sub-commands help")

def load_arguments():
	global args

	args, unknowns = parser.parse_known_args()
	return args