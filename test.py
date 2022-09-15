from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import time

# Connection to device


client = ModbusSerialClient(
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


if client.connect(): # Connection to slave device
    while True:
        print("Connection Successful")
        # register = client.read_coils(15, 2)
        register = client.read_holding_registers(address=14, count=8, unit=11)
        results = register.registers
        print(results)
        decoder = BinaryPayloadDecoder.fromRegisters(results, Endian.Big, wordorder=Endian.Little)
        print(decoder.decode_16bit_int())
        # print(register[0])
        # register.registers[0]

        time.sleep(1)

    # client.close()
else:
    print("Failed to connect to Modbus device")