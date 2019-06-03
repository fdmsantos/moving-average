from argparse import ArgumentParser
import os
import logging


def parameters():

    parser = ArgumentParser()
    parser.add_argument("-i", "--input_file",
                        type=lambda x: is_valid_file(parser, x),
                        required=True,
                        dest="file",
                        help="path to events file",
                        metavar="FILE")

    parser.add_argument("-w", "--window_size",
                        type=lambda x: is_valid_window_size(parser, x),
                        default=10,
                        dest="window_size",
                        help="window size in minutes for which the output will be produced",
                        metavar="INT")

    parser.add_argument("-o", "--output-type",
                        default='json',
                        dest="output_type",
                        help="type of output",
                        metavar="STRING")

    parser.add_argument("-a", "--aggregation",
                        default="AVG",
                        dest="aggregation",
                        help="Choose the aggregation to calculate",
                        metavar="STRING")

    args = parser.parse_args()

    logging.info("printing input parameters")
    for arg in vars(args):
        logging.info(arg + " : " + str(getattr(args, arg)))

    return args


def is_valid_file(parser, arg):
    logging.debug("Checking if input file exists")
    if not os.path.exists(arg):
        logging.fatal("Input file %s does not exist", arg)
        parser.error("The file %s does not exist!" % arg)
    else:
        logging.debug("Input file exists")
        return arg


def is_valid_window_size(parser, arg):
    logging.debug("Checking if window size is valid")
    if arg.isdigit() and int(arg) > 0:
        logging.debug("window size is valid")
        return int(arg)
    else:
        logging.fatal("Window size should be at least greater than or equal to 1 and int value!")
        parser.error("Window size should be at least greater than or equal to 1 and int value!")
