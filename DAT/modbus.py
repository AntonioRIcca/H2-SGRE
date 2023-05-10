from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import time

# Connection to device

class Modbus:
    def __init__(self):
        self.results = [0, 0, 0, 0, 0, 0, 0, 0]
        self.client = ModbusSerialClient(
            port="COM3",
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

    def read(self, reg=14, ch=21, count=8):
        if self.client.connect(): # Connection to slave device
            # print("Connection Successful")
            # register = client.read_coils(15, 2)
            register = self.client.read_holding_registers(address=reg, count=count, unit=ch)
            self.results = register.registers
            # print(self.results)
            # decoder = BinaryPayloadDecoder.fromRegisters(results, Endian.Big, wordorder=Endian.Little)
            # print(decoder.decode_16bit_int())
            # # print(register[0])
            # # register.registers[0]

            # time.sleep(1)

            # client.close()
        else:
            print("Failed to connect to Modbus device")
        return self.results

    def write_coil(self, address, value, unit):
        if self.client.connect():
            try:
                self.client.write_coil(address=address, value=value, unit=unit)
            except:
                print('error writing coil')
        else:
            print('connessione non riuscita')
