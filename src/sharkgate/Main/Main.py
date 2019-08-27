"""
Main functions for the project
"""
from termcolor import cprint
from pyfiglet import figlet_format
import sys
from os.path import dirname as opd, realpath as opr
import os
from waitress import serve
import click
import colorama
import logging
logging.basicConfig(level=logging.INFO)
colorama.init(strip=not sys.stdout.isatty())

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkgate.Config.Config import Config
from sharkgate.Service.PolicySetter import PolicySetter

@click.command()
@click.option(
    '--addr',
    default="127.0.0.1",
    help="IP address on which sharkgate will be served",
    show_default=True)
@click.option(
    '--port',
    default=16461,
    help="Port number on which sharkgate will be served",
    show_default=True)
@click.option(
    '--httplog',
    default='y',
    type=click.Choice(['y','n']),
    help="Whether to enable HTTP logging in sharkgate")
@click.option(
    '--logger',
    default='file',
    type=click.Choice(['file','MQ']),
    help="Type of HTTP logging in sharkgate")
@click.option(
    '--logfile',
    default="/",
    help="Fully qualified file path of http log file, if logging enabled with file ",
    show_default=True)
@click.option(
    '--discovery',
    default="static",
    type=click.Choice(['static', 'dynamic']),
    help="Type of endpoint discovery static|dynamic (using sharkradar)",
    show_default=True)
@click.option(
    '--sharkradarhost',
    default='http://127.0.0.1:16461',
    help="Full qualified host address for sharkradar host",
    show_default=True)
@click.option(
    '--policydir',
    default='/',
    help="Fully qualified path of directory containing all yml config files for sharkgate",
    show_default=True)
def main(addr, port, httplog, logger, logfile, discovery, sharkradarhost, policydir):
    """
            Sharkgate - Command Line Interface (CLI) utility
            ===================================================
            Sharkgate is a CLI based utility as API gateway with salient 
            features of having service discovery ability with sharkradar
            and other policy based features for use.
            
    """
    cprint(figlet_format('SHARKGATE', font='slant'), 'red', attrs=['bold'])
    try:
        Config.setHTTPLog(httplog)
        Config.setLogger(logger)
        Config.setLogfile(logfile)
        Config.setDiscovery(discovery)
        Config.setSharkradarhost(sharkradarhost)
        Config.setPolicydir(policydir)
        PolicySetter.policySetter()
        from sharkgate.Controller.Controller import app
        logging.info("Sharkgate Server starting ...")
        serve(app, listen=addr + ":" + str(port))
    except Exception as e:
        click.echo(
            "Exception occurred while starting sharkgate [{0}]\nRun 'sharkgate --help' for help".format(str(e)))
        sys.exit(5)


if __name__ == "__main__":
    main()
