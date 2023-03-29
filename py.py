#python -m pip install --upgrade pip
#pip install pyserial
#pip install serial
# import sys
# sys.executable
import serial
import sys
ser=serial.Serial(
    port='COM6',
    baudrate=9600,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=8
)

ser.readline()

#C:/Users/parkd/AppData/Local/Microsoft/WindowsApps/python3.10.exe -m pip install your_package_name