#!/usr/bin/env python3
import time
import datetime
from ADO import ado
from Temp import temp
import csv


sample = int(0)
machine = int(1)

if machine == 1:
    from BW_Roaster import bw
    ssn = bw.SGRN()
else:
    ssn = str('N/A')


try:
    open_ = open('/home/rinlee/Bellwether/file_cnt.txt', 'rt')
    file_contents = open_.read()
    file_contents = int(file_contents)
    open_.close()

    file_contents += 1
    with open('/home/rinlee/Bellwether/file_cnt.txt', 'w') as file:
        file.write(str(file_contents))

except FileNotFoundError:
    file_contents = str('1')
    with open('/home/rinlee/Bellwether/file_cnt.txt', 'w') as file:
        file.write(str(file_contents))

with open(f'/boot/logs/tmphum_{str(file_contents)}.csv', mode='w') as canary_file:  # Rpi
    canary_writer = csv.writer(canary_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    canary_writer.writerow(['Date', 'Time', 'Sample CNT', 'S1 Temp', 'S2 Temp', 'S1 Humidity', 'S2 Humidity', 'MState'])
    canary_file.flush()

while True:
    now = datetime.datetime.now()
    ddate = (now.strftime("%m-%d-%Y"))
    ttime = (now.strftime("%H:%M:%S"))

    t1 = str(temp.temp1())
    h1 = str(temp.hum1())
    t2 = str(temp.temp2())
    h2 = str(temp.hum2())

    if machine == 1:
        mstate = bw.SS()
        mstatem = mstate * 10
    else:
        mstatem = 0

    sample += 1

    ado.GDisplay(f'S1 T={str(t1)}F | H={str(h1)}%',
                 (f'S2 T={str(t2)}F | H={str(h2)}%'),
                 (f'Sample CNT: {str(sample)}'),
                 (f'File# {str(file_contents)} | {str(ssn)}: {str(mstate)}'))

    with open(f'/boot/logs/tmphum_{str(file_contents)}.csv', mode='a') as canary_file:  # Rpi
        canary_writer = csv.writer(canary_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        canary_writer.writerow([ddate, ttime, sample, t1, t2, h1, h2, mstatem])
        canary_file.flush()

    time.sleep(3)