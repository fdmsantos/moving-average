from argparse import ArgumentParser
import os


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
                        required=True,
                        dest="window_size",
                        help="window size in minutes for which the output will be produced")

    # TODO Implement choices - Use Strategy Folder?
    parser.add_argument("-o", "--output-type",
                        # type=lambda x: is_valid_file(parser, x),
                        # choices=list(Color),
                        default='json',
                        dest="output_type",
                        help="type of output")

    return parser.parse_args()


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def is_valid_window_size(parser, arg):
    if arg.isdigit() and int(arg) > 0:
        return int(arg)
    else:
        parser.error("Window size should be at least greater than or equal to 1 and int value!")
