from pymodbus.client import ModbusSerialClient  # per pymodbus 3.3.x e Python 3.11


mb_conn = True

client = ModbusSerialClient(
    port="COM2",  # TODO: inserire la COM esatta
    startbit=1,
    databits=8,
    parity="N",
    stopbits=2,
    errorcheck="crc",
    baudrate=38400,
    method="RTU",
    timeout=3,
    # unit=31
)

results = [0, 0, 0, 0, 0, 0, 0, 0]
if client.connect():  # Connessione al dispositivo
    register = client.read_holding_registers(address=14, count=4, slave=31)
    results = register.registers
else:
    mb_conn = False

print(mb_conn)
print(results)