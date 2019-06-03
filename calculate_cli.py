#!/usr/bin/env python3
from src.events.Factory import Factory as EventFactory
from src.moving_average import MovingAverage
from src.Output import Factory as OutputFactory
from src.utils import parameters
import logging


try:

    logging.basicConfig(filename='log', filemode="w", format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    args = parameters.parameters()

    results = MovingAverage(
        EventFactory.create_from_file(args.file),
        args.window_size
    ).calculate()

    logging.debug("printing results")
    OutputFactory.Factory.write(args.output_type, results)

except Exception as e:
    logging.exception(e)
    print("Please check the follow error: " + str(e))


