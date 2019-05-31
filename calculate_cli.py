#!/usr/bin/env python3
from src.events.Factory import Factory as EventFactory
from src.moving_average import MovingAverage
from src.Output import Factory as OutputFactory
from src.utils import parameters

print("hello circleci")

args = parameters.parameters()

results = MovingAverage(
    EventFactory.create_from_file(args.file),
    args.window_size
).calculate()

OutputFactory.Factory.print(args.output_type, results)



