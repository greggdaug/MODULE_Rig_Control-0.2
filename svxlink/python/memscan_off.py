#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/16/19

ICOM IC-7100 memory scan off from CI-V

Command structure = FE FE 88 E0 0E 00 FD

@author: Gregg Daugherty (WB6YAZ)
"""

import serial

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=0.5)

# print(ser.isOpen())

ser.flushInput()
ser.flushOutput()

data = b'\xFE\xFE\x88\xE0\x0E\x00\xFD' # memory scan off

ser.write(data)

# print(data)

#s = ser.read_until('')
# print(s)


ser.close()
