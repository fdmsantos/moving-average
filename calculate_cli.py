#!/usr/bin/env python3
from src.events.Factory import Factory as EventFactory
from src.output import Factory as OutputFactory
from src.utils import parameters
from src.aggregations.Factory import Factory as AggregationsFactory
import logging


try:

    logging.basicConfig(filename='data/log', filemode="w", format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    args = parameters.parameters()

    results = AggregationsFactory.calculate(args.aggregation, EventFactory.create_from_file(args.file), args.window_size)

    logging.debug("printing results")
    OutputFactory.Factory.write(args.output_type, results)

except Exception as e:
    logging.exception(e)
    print("Please check the follow error: " + str(e))


