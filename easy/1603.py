""" Design Parking System """
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.spots = [None, big, medium, small]

    def addCar(self, carType):
        if self.spots[carType] > 0:
            self.spots[carType] -= 1
            return True
        return False