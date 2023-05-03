from ..args import subparsers
from ..ip import ip_entrypoint

parser_ip = subparsers.add_parser("ip", help="Perform IP actions on Glesys API")
parser_ip.add_argument(
	"--list-free",
	required=False,
	action="store_true",
	default=False,
	help="Lists all available IP's to the user",
)
parser_ip.add_argument(
	"--ipversion",
	required=True,
	type=str,
	help="During --list-free which IP version are we looking for? 4 or 6?",
)
parser_ip.add_argument(
	"--datacenter",
	required=True,
	type=str,
	help="During --list-free which Datacenter are we looking for free IP's in?",
)
parser_ip.add_argument(
	"--platform",
	required=True,
	type=str,
	help="During --list-free which platform are we querying (KVM, OpenVZ, VMware)",
)

parser_ip.set_defaults(func=ip_entrypoint)