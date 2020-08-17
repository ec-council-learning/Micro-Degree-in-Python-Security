import re
import datetime
import argparse

## --serial <>

parser = argparse.ArgumentParser(description = "Process some Cisco Serial Numbers!")
parser.add_argument('--serial', metavar = 'serial', type = str, help = "This is the serial that you would like to parse!")
arguments = parser.parse_args()

class Converter(object):
    def __init__(self):
        self.pattern = re.compile("^[A-Z]{3,}[0-9]{4,}\w{4,}$")
        self.year = re.compile("^[0-9]{2,}$")
        self.month = re.compile("^[0-9]{2,}$")
    def convert(self, serial):
        self.serial = serial.upper()
        if self.pattern.match(self.serial):
            print(f"The specified serial passes the first test for form! : {self.serial}")
            if self.year.match(self.serial[3:5]):
                print("The year check has passed!")
                YoM = 1996 + int(self.year.match(self.serial[3:5]).group())
                print(f"The year of manufacturing was: {YoM}")
                if self.month.match(self.serial[5:7]):
                    MoM = datetime.date(YoM, int(self.month.match(self.serial[5:7]).group()), 1).strftime("%B")
                    print(f"The month of the manufacturing was in: {MoM}")
                else:
                    print("Could not identify the month of the manufacturing!")
            else:
                print("Could not identify the year of manufacturing!")
        else:
            print(f"The serial you have specified: {self.serial} is INVALID!")
if arguments.serial:
    print(f"The serial that will be parsed is: {arguments.serial}")
    C = Converter()
    C.convert(arguments.serial)
else:
    print("In order to use the script you need to specify a serial with the --serial switch!")
