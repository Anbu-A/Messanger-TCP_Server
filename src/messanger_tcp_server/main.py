import argparse
import logging
import sys
from .server import Server
from messanger_tcp_server import __version__


__author__ = "Anbu-A"
__copyright__ = "Anbu-A"
__license__ = "MIT"


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Creates socket on binds it on chosen ip and port")
    parser.add_argument(
        "--version",
        action="version",
        version="Messanger-TCP_Server {ver}".format(ver=__version__),
    )
    parser.add_argument(dest="server_ip", help="enter the server ip here")
    parser.add_argument(dest="port", help="enter the server port here", type = int)

    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    with Server(args.server_ip, args.port) as server:
        server.start_server() 


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
