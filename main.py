from abc import ABC, abstractmethod
from typing import List

class Switchable(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def print_state(self):
        pass
        
class LightBulb(Switchable):
    def __init__(self, state:str):
        allowed_states = ["On", "Off"]
        if state in allowed_states:
            self.state = state
        else:
            raise ValueError('Please enter an allowed state. Those are: {}'.format(allowed_states))

    def turn_on(self):
        print("LigthBulb turned on")

    def turn_off(self):
        print("LightBulb turned off")

    def print_state(self):
        print(f"{self.state}")

class Fan(Switchable):

    def __init__(self, state:str):
        allowed_states = ["On", "Off"]
        if state in allowed_states:
            self.state = state
        else:
            raise ValueError('Please enter an allowed state. Those are: {}'.format(allowed_states))

    def turn_on(self):
        print("Fan turned on")

    def turn_off(self):
        print("Fan turned off")

    def print_state(self):
        print(f"{self.state}")

class PowerSwitch:

    def __init__(self, c: List[Switchable]):
        self.clients = c
        for c_temp in self.clients:
            c_temp.state = "Off"

    def press(self):
        for c_temp in self.clients:
            if c_temp.state == "Off":
                c_temp.turn_on()
                c_temp.state = "On"
            else:
                c_temp.turn_off()
                c_temp.state = "Off"


if __name__ == '__main__':
    l = LightBulb("Off")
    f = Fan("Off")
    switch1 = PowerSwitch([f,l])
    switch2 = PowerSwitch([f])
    switch3 = PowerSwitch([l])
    switch1.press()
    switch2.press()
    switch1.press()
    switch3.press()
    print('Status l: ')
    l.print_state()
    print('Status f: ')
    f.print_state()

