import unittest
from lib.Parking import Parking
class ParkingTest(unittest.TestCase):
    def test_init(self):
        """
        On creatation there should be empty Slots
        """
        oParking = Parking(1)
        self.assertEquals(len(oParking),1)
        for oSlot in oParking.lSlot:
            self.assertIsNone(oSlot)


if __name__ == '__main__':
    unittest.main()
