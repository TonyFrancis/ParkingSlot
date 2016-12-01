from Lot import Lot
class Parking(object):

    def __init__(self,iNum):
        self.lLot = [ None ] * iNum
        print "Created a parking lot with {} slots".format(iNum)

    def __len__(self):
        return len(self.lLot)

    def lotFree(self):
        """
        Check if there is lot free or not
        """
        for index,value in enumerate(self.lLot):
            if not value:
                return index
        return -1

    def addCar(self,sRegisration,sColor):
        """
        Add car to the lot if free lot is present
        """
        index = self.lotFree()
        if index != -1:
            self.lLot[index] = Lot(sRegisration,sColor)
            return "Allocated slot number: {}".format(index + 1)
        return "Sorry, parking lot is full"
