from Slot import Slot
class Parking(object):
    def __init__(self,iNum):
        self.lSlot = [ None ] * iNum

    def __len__(self):
        return len(self.lSlot)

    def get_slots(self):
        return self.lSlot
