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

parser_server.set_defaults(func=server_entrypoint)