from ..args import subparsers
from ..server import server_entrypoint

parser_server = subparsers.add_parser("server", help="Perform Server actions on Glesys API")
parser_server.add_argument(
	"--all-servers",
	required=False,
	action="store_true",
	default=False,
	help="Lists all available servers to the user",
)
parser_server.add_argument(
	"--find",
	required=False,
	action="store_true",
	default=False,
	help="Attempts to find a server given --name, --description, --datacenter, --platform, --ip or --state",
)
parser_server.add_argument(
	"--lazy",
	required=False,
	action="store_true",
	default=False,
	help="Attempts a more relaced .find() by matching more loosely (mandatory for searching --ip for instance)",
)
parser_server.add_argument(
	"--details",
	required=False,
	default=None,
	type=str,
	help="Prints the details of a server (takes server_id or hostname/name)",
)
parser_server.add_argument(
	"--adapters",
	required=False,
	default=None,
	type=str,
	help="Prints the network adapters of a given server (takes server_id or hostname/name)",
)
parser_server.add_argument(
	"--status",
	required=False,
	default=None,
	type=str,
	help="Prints the status of a given server (takes server_id or hostname/name)",
)
parser_server.add_argument(
	"--limits",
	required=False,
	default=None,
	type=str,
	help="Prints the OpenVZ limits of a given server (takes server_id or hostname/name)",
)
parser_server.add_argument(
	"--costs",
	required=False,
	default=None,
	type=str,
	help="Prints the costs of a given server (takes server_id or hostname/name)",
)
parser_server.add_argument(
	"--est-costs",
	required=False,
	default=None,
	type=str,
	help="Prints the estimated costs of a given server (takes server_id or hostname/name)",
)


parser_server.add_argument(
	"--name",
	required=False,
	default=None,
	type=str,
	help="This is a search parameter for --find",
)
parser_server.add_argument(
	"--description",
	required=False,
	default=None,
	type=str,
	help="This is a search parameter for --find",
)
parser_server.add_argument(
	"--datacenter",
	required=False,
	default=None,
	type=str,
	help="This is a search parameter for --find",
)
parser_server.add_argument(
	"--platform",
	required=False,
	default=None,
	type=str,
	help="This is a search parameter for --find",
)
parser_server.add_argument(
	"--ip",
	required=False,
	default=None,
	type=str,
	help="This is a search parameter for --find",
)
parser_server.add_argument(
	"--state",
	required=False,
	default=None,
	type=str,
	help="This is a search parameter for --find",
)

parser_server.set_defaults(func=server_entrypoint)