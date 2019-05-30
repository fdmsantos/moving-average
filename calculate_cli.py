#!/usr/bin/env python3
from events.Factory import Factory as EventFactory
from moving_average import MovingAverage
from Output import Factory as OutputFactory
from utils import parameters

args = parameters.parameters()

results = MovingAverage(
    EventFactory.create_from_file(args.file),
    args.window_size
).calculate()

OutputFactory.Factory.print(args.output_type, results)



