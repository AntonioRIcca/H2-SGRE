try:
    from pymodbus.client.sync import ModbusSerialClient     # Per pymodbus 2.x e Python 3.7
except:
    from pymodbus.client import ModbusSerialClient          # per pymodbus 3.3.x e Python 3.11

from _shared import variables as v
# from pymodbus.payload import BinaryPayloadDecoder
# from pymodbus.constants import Endian
# import time


# Connection to device
class Modbus:
    def __init__(self):
        self.results = [0, 0, 0, 0, 0, 0, 0, 0]

        # Impostazione della connessione
        self.client = ModbusSerialClient(
            port="COM2",    #TODO: inserire la COM esatta
            startbit=1,
            databits=8,
            parity="N",
            stopbits=2,
            errorcheck="crc",
            baudrate=38400,
            method="RTU",
            timeout=3,
            # unit=11
        )

    def read_holding(self, reg=14, ch=21, count=8):
        self.results = [0, 0, 0, 0, 0, 0, 0, 0]
        if self.client.connect():   # Connessione al dispositivo
            register = self.client.read_holding_registers(address=reg, count=count, slave=ch)
            self.results = register.registers
        else:
            v.mb_conn = False
        return self.results

    def read_coils(self, ch=11, reg=16, count=4):
        self.results = [False, False, False, False, False]
        if self.client.connect():
            try:
                register = self.client.read_coils(address=reg, count=count, slave=ch)
                self.results = register.bits
            except:
                print('error reading coils')
        else:
            v.mb_conn = False
        return self.results

    def write_coil(self, address, value, unit):
        if self.client.connect():
            try:
                self.client.write_coil(address=address, value=value, slave=unit)
            except:
                print('error writing coil')
        else:
            # print('connessione non riuscita')
            pass
