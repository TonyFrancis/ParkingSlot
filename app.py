#!/usr/bin/python
import sys
from lib.Parking import Parking
if __name__ == '__main__':
    bInteractive = bool(len(sys.argv) == 1)
    if not bInteractive:
        input_file = open(sys.argv[1],'r')
        getCommand = input_file.readline
    else:
        getCommand = raw_input
    if bInteractive:
        print "Input:"
    sCommand = getCommand()
    while sCommand:
        lCommands = sCommand.split()
        iLength = len(lCommands)
        if iLength:
            if bInteractive:
                print "\nOutput:"
            if lCommands[0] == "create_parking_lot" and iLength == 2:
                oParking = Parking(int(lCommands[1]))
            elif lCommands[0] == "park" and iLength == 3:
                print oParking.addCar(lCommands[1],lCommands[2])+"\n"
            elif lCommands[0] == "leave" and iLength == 2:
                print oParking.removeCar(int(lCommands[1]))+"\n"
            elif lCommands[0] == "status":
                print oParking.status()
            elif lCommands[0] == "registration_numbers_for_cars_with_colour" and iLength == 2:
                print oParking.carsWithColor(lCommands[1])+"\n"
            elif lCommands[0] == "slot_number_for_registration_number" and iLength == 2:
                print oParking.slotNumber(lCommands[1])+"\n"
        if bInteractive:
            print "Input:"
        sCommand = getCommand()
