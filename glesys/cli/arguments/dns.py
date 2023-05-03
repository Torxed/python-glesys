import pathlib
from ..args import subparsers
from ...dns.cli_handler import dns_entrypoint

parser_dns = subparsers.add_parser("dns", help="Perform DNS actions on Glesys API")
parser_dns.add_argument(
	"--color",
	required=False,
	action="store_true",
	default=False,
	help="Adds colors to certain elements",
)

parser_dns.add_argument(
	"--all-domains",
	required=False,
	action="store_true",
	default=False,
	help="List all domains registered via Glesys",
)
parser_dns.add_argument(
	"--all-records",
	required=False,
	action="store_true",
	default=False,
	help="List all records for a given --domain",
)
parser_dns.add_argument(
	"--find",
	required=False,
	action="store_true",
	default=False,
	help="Search through a given --domain for --record, --type or --data",
)
parser_dns.add_argument(
	"--add",
	required=False,
	action="store_true",
	default=False,
	help="Adds a record in --domain using --record, --type, --data and -ttl",
)
parser_dns.add_argument(
	"--delete",
	required=False,
	action="store_true",
	default=False,
	help="Adds a record in --domain using --record, --type, --data and -ttl",
)

parser_dns.add_argument(
	"--domain",
	required=False,
	type=str,
	help="Defines which domain to work on",
)
parser_dns.add_argument(
	"--record",
	required=False,
	type=str,
	help="Filters which record name to look for during search",
)
parser_dns.add_argument(
	"--type",
	required=False,
	type=str,
	help="Filters which record type to look for during search",
)
parser_dns.add_argument(
	"--data",
	required=False,
	type=str,
	help="Filters which data/content to look for in the record search",
)
parser_dns.add_argument(
	"--ttl",
	required=False,
	type=int,
	help="Defines the TTL when using --add to create a DNS entry",
)
parser_dns.set_defaults(func=dns_entrypoint)