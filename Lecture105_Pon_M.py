class Vehicle:
    LicenseName = ""
    SerialCode = ""
    def TurnonConditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    def OpenConvertibleRoof(self):
        print("Open Roof")
class PickUp(Vehicle):
    def OpenTailgate(self):
        print("Open Tailgate")
class Van(Vehicle):
    def OpenTheDoor(self):
        print("Open The Door")

class EstateCar(Vehicle):
    def TurnOnMap(self):
        print("Open Map")


car1 = Car()
car1.TurnonConditioner()
car1.OpenConvertibleRoof()

van1 = Van()
van1.TurnonConditioner()
van1.OpenTheDoor()

pickup1 = PickUp()
pickup1.TurnonConditioner()
pickup1.OpenTailgate()

estatecar1 = EstateCar()
estatecar1.TurnonConditioner()
estatecar1.TurnOnMap()
