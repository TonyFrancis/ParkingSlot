import sys
from lib.Parking import Parking
if __name__ == '__main__':
    bInteractive = bool(len(sys.argv) > 1)
    if bInteractive:
        input_file = open(sys.argv[1],'r')
        getCommand = input_file.readline
    else:
        getCommand = raw_input
    sCommand = getCommand()
    while sCommand:
        lCommands = sCommand.split()
        if lCommands[0] == "create_parking_lot":
            oParking = Parking(int(lCommands[1]))
        elif lCommands[0] == "park":
            sMessage = oParking.addCar(lCommands[1],lCommands[2])
            print sMessage
        sCommand = getCommand()
