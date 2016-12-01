import unittest
from lib.Parking import Parking
from lib.Lot import Lot
class ParkingTest(unittest.TestCase):
    def test_init(self):
        """
        On creatation there should be empty Slots
        1. assign non zero Parking lot
        2. assign zero parking lot
        3. assign negative number
        """
        oParking = Parking(1)
        self.assertEquals(len(oParking),1)
        for oLot in oParking.lLot:
            self.assertIsNone(oLot)
        oParking = Parking(0)
        self.assertEquals(len(oParking),0)
        oParking = Parking(-1)
        self.assertEquals(len(oParking),0)


    def test_lotFree(self):
        """
        test lotFree method
        1. Check lot free for non zero postive number
        2. Check for zero
        """
        oParking = Parking(2)
        self.assertEquals(oParking.lotFree(),0)
        oParking.lLot[0] = 1
        self.assertEquals(oParking.lotFree(),1)
        oParking.lLot[1] = 1
        self.assertEquals(oParking.lotFree(),-1)
        oParking = Parking(0)
        self.assertEquals(oParking.lotFree(),-1)

    def test_addCar(self):
        """
        test addCar
        1. Add non zero Cars. Check list filled up with Lot type
        """
        oParking = Parking(2)
        sMessage = oParking.addCar("a","b")
        self.assertEquals(sMessage,"Allocated slot number: {}".format(1))
        self.assertIsInstance(oParking.lLot[0],Lot)
        sMessage = oParking.addCar("a","b")
        self.assertIsInstance(oParking.lLot[1],Lot)
        self.assertEquals(sMessage,"Allocated slot number: {}".format(2))
        sMessage = oParking.addCar("a","b")
        self.assertEquals(sMessage,"Sorry, parking lot is full")


if __name__ == '__main__':
    unittest.main()
