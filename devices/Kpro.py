import usb.core
import usb.util

KPRO2_BAT = 5

KPRO4_ECT = 2
KPRO4_IAT = 3
KPRO4_BAT = 4


class Kpro:
    def __init__(self):
        self.version = 2
        self.data = []
        self.dev = usb.core.find(idVendor=0x403, idProduct=0xf5f8)  # kpro2
        # self.dev = usb.core.find(idVendor=0x1c40, idProduct=0x0434) #kpro4
        self.dev.set_configuration()
        cfg = self.dev.get_active_configuration()
        intf = cfg[(0, 0)]
        self.ep = usb.util.find_descriptor(
            intf,
            custom_match= \
                lambda e: \
                    usb.util.endpoint_direction(e.bEndpointAddress) == \
                    usb.util.ENDPOINT_OUT)

    def update(self):
        try:
            assert self.ep is not None
            self.ep.write('\x61')
            # datos = dev.read(0x82,10000,1000) kpro4
            self.data = self.dev.read(0x81, 10000, 1000)  # kpro2
        except:
            pass

    def bat(self):
        try:
            if self.version == 2:
                return self.data[KPRO2_BAT] * 0.1
            elif self.version == 4:
                return self.data[KPRO4_BAT] * 0.1
        except:
            return 0
