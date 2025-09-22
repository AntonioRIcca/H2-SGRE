from pymodbus.client import ModbusSerialClient  # per pymodbus 3.3.x e Python 3.11
from PyQt5 import QtCore, QtWidgets
import sys
import time

mb_conn = True

client = ModbusSerialClient(
    port="COM3",  # TODO: inserire la COM esatta
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

app = QtWidgets.QApplication(sys.argv)

a=0

def refresh():
    for i in [21, 22, 31]:
        register = client.read_holding_registers(address=21, count=8, slave=i)
        results = register.registers
        print(a, results)
    for i in [11, 12, 13, 14]:
        register = client.read_coils(address=0, count=4, slave=i)
        register1 = client.read_coils(address=0, count=4, slave=i)
        results = register.bits[:4] + register1.bits[:4]
        print(a, results)
    print(time.perf_counter())

if client.connect():  # Connessione al dispositivo
    print('connesso: inizio ciclo')
    timer = QtCore.QTimer()
    timer.timeout.connect(refresh)
    timer.start(10)

    app.exec()

i = 0
