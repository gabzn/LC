https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        slot_index = carType - 1
        if self.slots[slot_index] == 0:
            return False
        
        self.slots[slot_index] -= 1
        return True
