import pathlib
from ..args import subparsers
from ...hooks.letsencrypt.cli_handler import letsencrypt_entrypoint

parser_letsencrypt = subparsers.add_parser("lets-encrypt", help="Perform LetsEncrypt actions using Glesys")
parser_letsencrypt.add_argument(
	"--all-domains",
	required=False,
	action="store_true",
	default=False,
	help="Create certificate for all domains under the Glesys DNS hosting",
)
parser_letsencrypt.add_argument(
	"--individual",
	required=False,
	action="store_true",
	default=False,
	help="Divides up certificates per domain rather than unifying them all (preferred but not default)",
)
parser_letsencrypt.add_argument(
	"--production",
	required=False,
	action="store_true",
	default=False,
	help="Replaces acme-staging-v02 with LetsEncrypt prod server https://acme-v02.api.letsencrypt.org/directory",
)

parser_letsencrypt.add_argument(
	"--workdir",
	required=False,
	type=pathlib.Path,
	default=pathlib.Path('/var/lib/letsencrypt'),
	help="The path of the certbot working directory",
)
parser_letsencrypt.add_argument(
	"--logsdir",
	required=False,
	type=pathlib.Path,
	default=pathlib.Path('/var/log/letsencrypt'),
	help="The path of the certbot log directory",
)
parser_letsencrypt.add_argument(
	"--confdir",
	required=False,
	type=pathlib.Path,
	default=pathlib.Path('/etc/letsencrypt'),
	help="The path of the certbot config directory",
)

parser_letsencrypt.set_defaults(func=letsencrypt_entrypoint)