#!/usr/bin/env python3
from Factory import Factory
from MovingAverage import MovingAverage
from Output import JsonWriter

average = MovingAverage(Factory.create_from_file("events.json"), 10)
results = average.calculate()
JsonWriter.JsonWriter.write(results)
