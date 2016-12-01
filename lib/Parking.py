from Slot import Slot
class Parking(object):

    def __init__(self,iNum):
        self.lSlot = [ None ] * iNum
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
            return "Allocated slot number: {}".format(index + 1)
        return "Sorry, parking lot is full"

    def removeCar(self,iSlot):
        """
        Remove Car from Lot
        """
        if len(self.lSlot) >= iSlot:
            if self.lSlot[iSlot - 1]:
                self.lSlot[iSlot - 1 ] = None
            return "Slot number {} is free".format(iSlot)
        return "There is no Slot number {}".format(iSlot)
