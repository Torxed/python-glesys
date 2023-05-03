from .args import subparsers, load_arguments
from .arguments.dns import parser_dns
from .arguments.letsencrypt import parser_letsencrypt
from .arguments.server import parser_server
from .arguments.ip import parser_ip

loaded = True