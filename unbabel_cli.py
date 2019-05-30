#!/usr/bin/env python3
from Factory import Factory
from MovingAverage import MovingAverage
from Output import JsonWriter
from utils import parameters

args = parameters.parameters()
average = MovingAverage(Factory.create_from_file(args.file), args.window_size)
results = average.calculate()
JsonWriter.JsonWriter.write(results)


