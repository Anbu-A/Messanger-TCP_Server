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
    parser = argparse.ArgumentParser(description="Starts a Server")
    parser.add_argument(
        "--version",
        action="version",
        version="Messanger-TCP_Server {ver}".format(ver=__version__),
    )
    parser.add_argument(dest="server_ip", help="enter the server ip")
    parser.add_argument(dest="port", help="enter the server port", type = int)

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
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m messanger_tcp_server.skeleton 42
    #
    run()
