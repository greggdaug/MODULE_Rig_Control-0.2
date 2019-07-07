#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/7/19

ICOM IC-7100 set preamp 1 off from CI-V

Command structure = FE FE 88 E0 16 02 00 FD

@author: Gregg Daugherty (WB6YAZ)
"""

import serial

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=0.5)

# print(ser.isOpen())

ser.flushInput()
ser.flushOutput()

data = b'\xFE\xFE\x88\xE0\x16\x02\x00\xFD' # set ptt lock on

ser.write(data)

# print(data)

#s = ser.read_until('')
# print(s)


ser.close()
