#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/6/19

ICOM IC-7100 read s-meter level

Command structure = FE FE 88 E0 15 02 FD (reading between 0 and 241, 120 = s9)

@author: Gregg Daugherty (WB6YAZ)
"""

import serial
import struct
import math

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=0.5)

# print(ser.isOpen())

ser.flushInput()
ser.flushOutput()

data = b'\xFE\xFE\x88\xE0\x15\x02\xFD' # get signal strength

ser.write(data)

# print(data)

s = ser.read_until('')

# print(s)

# bytes = b'\x12\x45\x00\xab'
val = struct.unpack('<BBBBBBBBBBBBBBBB', s)

# print(val)

sval = 100*val[13]+val[14]

# print(sval)

# svaldbm = abs(math.ceil(-0.00071*sval**2 + 0.75*sval - 153))
svaldbm = math.ceil(0.00012*sval**2 + 0.45*sval - 129)

print(svaldbm)

ser.close()
