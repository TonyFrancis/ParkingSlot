from Slot import Slot
class Parking(object):

    def __init__(self,iNum):
        self.lSlot = [ None ] * iNum
        self.dCarsColor = {}
        self.dSlotCars = {}
        print "Created a parking lot with {} slots".format(iNum)

    def __len__(self):
        return len(self.lSlot)

    def isSlotFree(self):
        """
        Check if there is lot free or not
        """
        for index,value in enumerate(self.lSlot):
            if not value:
                return index
        return -1

    def addCar(self,sRegisration,sColor):
        """
        Add car to the lot if free lot is present
        """
        index = self.isSlotFree()
        if index != -1:
            self.lSlot[index] = Slot(sRegisration,sColor)
            self.dSlotCars[sRegisration] = index
            if sColor in self.dCarsColor:
                self.dCarsColor[sColor].append(sRegisration)
            else:
                self.dCarsColor[sColor] = [ sRegisration ]
            return "Allocated slot number: {}".format(index + 1)
        return "Sorry, parking lot is full"

    def removeCar(self,iSlot):
        """
        Remove Car from Lot
        """
        if len(self.lSlot) >= iSlot:
            if self.lSlot[iSlot - 1]:
                if self.lSlot[iSlot - 1].sColor in self.dCarsColor:
                    del self.dSlotCars[self.lSlot[iSlot - 1].sRegisration]
                    self.dCarsColor[self.lSlot[iSlot - 1].sColor].remove(self.lSlot[iSlot - 1].sRegisration)
                    if len(self.dCarsColor[self.lSlot[iSlot - 1].sColor]) == 0:
                        del self.dCarsColor[self.lSlot[iSlot - 1].sColor]
                self.lSlot[iSlot - 1 ] = None

            return "Slot number {} is free".format(iSlot)
        return "There is no Slot number {}".format(iSlot)

    def status(self):
        """
        Status of the Parking Slot
        """
        sStatus = "Slot No.\tRegistration No\t\tColour\n"
        for index,value in enumerate(self.lSlot):
            if value:
                sStatus += str(index + 1) + "\t\t"+ value.sRegisration + "\t\t\t" +value.sColor +"\n"
        return sStatus

    def carsWithColor(self,sColor):
        """
        Get all cars with Color: sColor
        """
        sData = ""
        if sColor in self.dCarsColor:
            sData = ",".join(self.dCarsColor[sColor])
        return sData

    def slotNumber(self,sRegisration):
        """
        Does a lookup on Registration and retrun its found or not.
        """
        if sRegisration in self.dSlotCars:
            return str(self.dSlotCars[sRegisration] + 1)
        return "None Found"
