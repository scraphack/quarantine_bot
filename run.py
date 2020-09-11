#!/usr/bin/env python3
"bot.py"

import argparse
import logging

import quarantinebot.bot as qb

LOG_LOC = "/tmp/qbot.log"


def setup_arguments():
    """
    Sets up command line arguments to allow for debug and optional log file
    location
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
        "--debug", 
        action="store_true", 
        help="Sets debug mode"
        ) 
    parser.add_argument(
        "-f",
        "--filename",
        action="store",
        type=str,
        default=LOG_LOC,
        help="Location where the log file will be located"
        )
    return parser.parse_args()


def setup_logging(debug, file_name):
    "Sets defaults for logging."

    log_format = '%(asctime)s - %(message)s'
    if debug:
        severity = logging.DEBUG
    else:
        severity = logging.INFO
    logging.basicConfig(format=log_format, level=severity, filename=file_name)
     

if __name__  == "__main__":    
    args = setup_arguments()
    setup_logging(args.debug, args.filename)
    qb.bot.run(qb.TOKEN)
 
