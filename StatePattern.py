from abc import abstractmethod, ABCMeta

class InternalState(metaclass = ABCMeta):
    @abstractmethod
    def changeState(self):
        pass

class TurnedOn(InternalState):
    def changeState(self):
        print("Turning on the Radio Station!")
        return "ON"

class TurnedOff(InternalState):
    def changeState(self):
        print("Turning off the Radion Station")
        return "OFF"

class IncreaseVolume(InternalState):
    def changeState(self):
        print("The volume of the Radio Station has been increased!")
        return "+10"

class DecreaseVolume(InternalState):
    def changeState(self):
        print("The volume of the Radio Station has been decreased!")
        return "-10"

class RadioStation(InternalState):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, status):
        self.state = status

    def changeState(self):
        self.state = self.state.changeState()

Radio = RadioStation()
print(f"The internal state of the Radio Station is: {Radio.getState()}")

ON = TurnedOn()
OFF = TurnedOff()

Louder = IncreaseVolume()
Lower = DecreaseVolume()

print("Turn on the station!")
Radio.setState(ON)
Radio.changeState()
print(f"Check the state of the radio: {Radio.getState()}")

print("Give it some noise!")
Radio.setState(Louder)
Radio.changeState()
print(f"Check the state of the radio: {Radio.getState()}")

print("Make it more silent!")
Radio.setState(Lower)
Radio.changeState()
print(f"Check the state of the radio: {Radio.getState()}")

print("Turning of the Radio!")
Radio.setState(OFF)
Radio.changeState()
print(f"Check the state of the radio: {Radio.getState()}")
