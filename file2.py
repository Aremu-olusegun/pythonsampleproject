"""
Create a function that finds out the state of water (i.e., gas, liquid, solid)
given the temperature. In other words, the function has a
temperature parameter and returns either "Gas", "Liquid" or "Solid"
as a string depending on the temperature. The function should be written in a
separate file from the command line interface file.
"""

solid = 0
liquid = 100

def findTemperature(temperature):
        if temperature <= solid:
            return "solid"
        elif 0 <= int(temperature) < liquid:
            return "liquid"
        else:
            return "Gas"
