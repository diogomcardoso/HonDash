import usb.core
import usb.util

KPRO2_BAT = 5

KPRO4_ECT = 2
KPRO4_IAT = 3
KPRO4_BAT = 4


class Kpro:
    def __init__(self):
        self.data0 = []
        self.data1 = []
        self.data2 = []
        self.dev = None
        self.version = 0
        if usb.core.find(idVendor=0x403, idProduct=0xf5f8) is not None: #kpro2
            self.dev = usb.core.find(idVendor=0x403, idProduct=0xf5f8)
            self.version = 2
        elif usb.core.find(idVendor=0x1c40, idProduct=0x0434) is not None: #kpro4
            self.dev = usb.core.find(idVendor=0x1c40, idProduct=0x0434)
            self.version = 4
        if self.dev is not None:
            try:
                self.dev.set_configuration()
                cfg = self.dev.get_active_configuration()
                intf = cfg[(0, 0)]
                self.ep = usb.util.find_descriptor(
                    intf,
                    custom_match= \
                        lambda e: \
                            usb.util.endpoint_direction(e.bEndpointAddress) == \
                            usb.util.ENDPOINT_OUT)
            except:
                pass
    def update(self):
        try:
            assert self.ep is not None
            self.ep.write('\x61')
            if self.version == 2:
                self.data1 = self.dev.read(0x81, 10000, 1000)  # kpro2
            elif self.version == 4:
                self.data1 = self.dev.read(0x82,10000,1000) #kpro4
        except:
            self.__init__()
            pass

    def bat(self):
        try:
            if self.version == 2:
                return self.data1[KPRO2_BAT] * 0.1
            elif self.version == 4:
                return self.data1[KPRO4_BAT] * 0.1
        except:
            return 0
