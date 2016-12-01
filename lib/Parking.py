from Lot import Lot
class Parking(object):

    def __init__(self,iNum):
        self.lLot = [ None ] * iNum
        print "Created a parking lot with {} slots".format(iNum)

    def __len__(self):
        return len(self.lLot)

    def slotFree(self):
        for index,value in enumerate(self.lLot):
            if not value:
                return index
        return -1

    def addCar(self,sRegisration,sColor):
        index = self.slotFree()
        if index != -1:
            self.lLot[index] = Lot(sRegisration,sColor)
            return "Allocated slot number: {}".format(index + 1)
        return "Sorry, parking lot is full"
