class Device:
    def turn_on(self):
        print('Device is turned on')

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('Portable device is turned on')
        
class TV(Device):
    def turn_on(self):
        print('TV is turned on')
        
device = Device()
radio = Radio()
portableRadio = PortableRadio()
tv = TV()

for element in device, radio, portableRadio, tv:
    element.turn_on()