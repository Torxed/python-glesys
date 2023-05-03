from .args import subparsers, load_arguments
from .arguments.dns import parser_dns
from .arguments.letsencrypt import parser_letsencrypt

loaded = True