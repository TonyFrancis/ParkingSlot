import unittest
from lib.Parking import Parking
from lib.Slot import Slot
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
        for oSlot in oParking.lSlot:
            self.assertIsNone(oSlot)
        oParking = Parking(0)
        self.assertEquals(len(oParking),0)
        oParking = Parking(-1)
        self.assertEquals(len(oParking),0)


    def test_isSlotFree(self):
        """
        test isSlotFree method
        1. Check lot free for non zero postive number
        2. Check for zero
        """
        oParking = Parking(2)
        self.assertEquals(oParking.isSlotFree(),0)
        oParking.lSlot[0] = 1
        self.assertEquals(oParking.isSlotFree(),1)
        oParking.lSlot[1] = 1
        self.assertEquals(oParking.isSlotFree(),-1)
        oParking = Parking(0)
        self.assertEquals(oParking.isSlotFree(),-1)

    def test_addCar(self):
        """
        test addCar
        1. Add non zero Cars. Check list filled up with Lot type
        """
        oParking = Parking(2)
        sMessage = oParking.addCar("a","b")
        self.assertEquals(len(oParking.dCarsColor["b"]),1)
        self.assertEquals(sMessage,"Allocated slot number: {}".format(1))
        self.assertIsInstance(oParking.lSlot[0],Slot)
        sMessage = oParking.addCar("a","b")
        self.assertEquals(len(oParking.dCarsColor["b"]),2)
        self.assertIsInstance(oParking.lSlot[1],Slot)
        self.assertEquals(sMessage,"Allocated slot number: {}".format(2))
        sMessage = oParking.addCar("a","b")
        self.assertEquals(len(oParking.dCarsColor["b"]),2)
        self.assertEquals(sMessage,"Sorry, parking lot is full")

    def test_removeCar(self):
        """
        test removeCar
        test if slot number greater than no of slots
        check for non zero slot
        """
        oParking = Parking(0)
        sMessage = oParking.removeCar(1)
        self.assertEquals(sMessage,"There is no Slot number {}".format(1))
        oParking = Parking(2)
        sMessage = oParking.removeCar(2)
        self.assertEquals(sMessage,"Slot number {} is free".format(2))
        oParking.addCar("12","white")
        oParking.addCar("13","black")
        sMessage = oParking.removeCar(2)
        self.assertEquals(len(oParking.dCarsColor["black"]),0)
        self.assertEquals(sMessage,"Slot number {} is free".format(2))
    def test_status(self):
        """
        test status
        """
        oParking = Parking(3)
        sMessage = oParking.status()
        self.assertEquals(sMessage,"Slot No.\tRegistration No\t\tColour\n")
        oParking.lSlot[0] = Slot("1234","123")
        sMessage = oParking.status()
        self.assertEquals(sMessage,"Slot No.\tRegistration No\t\tColour\n1\t\t1234\t\t\t123\n")
        oParking.lSlot[2] = Slot("1234","123")
        sMessage = oParking.status()
        self.assertEquals(sMessage,"Slot No.\tRegistration No\t\tColour\n1\t\t1234\t\t\t123\n3\t\t1234\t\t\t123\n")

    def test_carsWithColor(self):
        """
        test cars with Color
        check output after insert and delete to be excepted
        """
        oParking = Parking(2)
        sMessage = oParking.carsWithColor("white")
        self.assertEquals("","")
        oParking.addCar("12","white")
        sMessage = oParking.carsWithColor("white")
        self.assertEquals(sMessage,"12")
        oParking.addCar("13","black")
        sMessage = oParking.carsWithColor("white")
        self.assertEquals(sMessage,"12")
        oParking.removeCar(1)
        sMessage = oParking.carsWithColor("white")
        self.assertEquals(sMessage,"")

if __name__ == '__main__':
    unittest.main()
