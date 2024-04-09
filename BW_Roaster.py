#!/usr/bin/env python3
import os
import time
import datetime
import socket

user = os.getlogin()
directory = str('Bellwether')

ST_Link = int(0)

debug = int(0)

if ST_Link == 1:
    import serial
    default_firmware_log_device = '/dev/ttyUSB0'
    default_st_link_device = '/dev/ttyACM0'
    serial_port = None
    device = default_st_link_device
    baudrate = 115200
    try:
        serial_port = serial.Serial(device, baudrate, timeout=.1, write_timeout=1)
    except FileNotFoundError:
        print(f'ST Not Found')
        exit(1)

if ST_Link == 1:
    serial_port.write(b'MISC 0 GSN\r')
    response = serial_port.readline()
    response = response.decode('utf-8')
    hname = response[2:-7]
    ip_address = str('BFT')
else:
    hname = os.popen(f'curl "https://localhost:8443/roaster/sensor?m=MISC&cmd=GSN&u=0" -k -s -s').read()
    hname = hname.split(':')
    try:
        hname = hname[4]
        hname = hname.split('0')
        hname = hname[0]
        hname = hname[1:]
        hname = hname.upper()
    except IndexError:
        hname = str('Invalid')


if hname == str('PR'):
    machine_series = str('(Early V2)')
    hardware_rev = int(2)
elif hname == str('R'):
    machine_series = str('(Production V2)')
    hardware_rev = int(2)
elif hname == str('PS'):
    machine_series = str('(Project Pyra)')
    hardware_rev = int(3)
elif hname == str('S'):
    machine_series = str('(Production Pyra)')
    hardware_rev = int(3)
else:
    machine_series = str('(Unknown)')
    hardware_rev = int(0)




usr = os.getlogin()
'''''''''
Note to get curl command send sbc command.
Example: sbc -l sys 0 gac 0 (All)
Example: sbc -l sys 0 gac 1 (Critical)

API:
     SYS:GET_ALARM_CONDITIONS  SYS 0 GAC  param[0= all alarms, 1=critical only]
                               Status=Bit fields of the Alarms
'''''''''
if ST_Link != 1:
    # os.system('sudo mount /dev/sda1 /home/rinlee/rin')
    open_ = open(f'/boot/ip.rin', 'rt')
    add = open_.read()
    # add = int(add)
    port = str('8443')

    ip_address = str(add)

    ip_address = ip_address.split('\n')
    ip_address = ip_address[0]

    bit = int(0)

    # if add == 1:
    #     from ip_address_a import ip_address
    # elif add == 2:
    #     from ip_address_b import ip_address
    # elif add == 3:
    #     from ip_address_c import ip_address
    # elif add == 4:
    #     from ip_address_d import ip_address
    # elif add == 5:
    #     from ip_address_e import ip_address
    # elif add == 6:
    #     from ip_address_f import ip_address
    # elif add == 7:
    #     from ip_address_g import ip_address
    # else:
    #     print('IP Error')

    import socket

elog = str(0)

home = str('')
home = os.popen('echo ~$HOME').read()
home = str(home)[7:-1]

if elog == 1:
    import logging

    LOG_FORMAT = '%(levelname)s: %(asctime)s: %(message)s'
    logging.basicConfig(filename='/home/' + home + '/Roaster_Object.log',
                        level=logging.ERROR,
                        format=LOG_FORMAT)
    logger = logging.getLogger()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



try:
    s.connect(("8.8.8.8", 80))
    ip_address_l = s.getsockname()[0]
    s.close()
    net = 1

except OSError:
    net = 0

if net == 1:
    if hname == str('PS'):
        rev = str('4.0a Pre-Release for Pyra')
    elif hname == str('S'):
        rev = str('4.0a Pre-Release for Pyra')
    else:
        rev = str('4.0a Release for V2')

    IP = str('')
    statelist = ['Reset 0', 'init 1', 'Offline 2', 'Ready 3', 'PreHeat 4', 'Roast 5', 'Cool 6', 'Shutdown 7',
                 'Error 8', 'Standby 9', '<NULL> -1']


    class BW:
        def __init__(self):
            pass

        def SHD(self):
            if ST_Link == 1:
                import serial
                default_firmware_log_device = '/dev/ttyUSB0'
                default_st_link_device = '/dev/ttyACM0'
                serial_port = None
                device = default_st_link_device
                baudrate = 115200
                try:
                    serial_port = serial.Serial(device, baudrate, timeout=.1, write_timeout=1)
                except FileNotFoundError:
                    print(f'ST Not Found')
                    exit(1)

            if ST_Link == 1:
                serial_port.write(b'MISC 0 GSN\r')
                response = serial_port.readline()
                response = response.decode('utf-8')
                hname = response[2:-7]
                ip_address = str('BFT')
            else:
                hname = os.popen(f'curl "https://localhost:8443/roaster/sensor?m=MISC&cmd=GSN&u=0" -k -s -s').read()
                hname = hname.split(':')
                try:
                    hname = hname[4]
                    hname = hname.split('0')
                    hname = hname[0]
                    hname = hname[1:]
                    hname = hname.upper()
                except IndexError:
                    hname = str('Invalid')

            if hname == str('PR'):
                machine_series = str('(Early V2)')
                hardware_rev = int(2)
            elif hname == str('R'):
                machine_series = str('(Production V2)')
                hardware_rev = int(2)
            elif hname == str('PS'):
                machine_series = str('(Project Pyra)')
                hardware_rev = int(3)
            elif hname == str('S'):
                machine_series = str('(Production Pyra)')
                hardware_rev = int(3)
            else:
                machine_series = str('(Unknown)')
                hardware_rev = int(0)
            print (hardware_rev)
            return hardware_rev


        def SINITB(self):  # Initializes blower BLDC Pyra
            if hardware_rev != 3:
                print(f'Hardware not supported.  HW ID: {hardware_rev})')
                time.sleep(2)
            if hardware_rev == 3:

                if ST_Link == 1:
                    print(f'Blower BLDC Reset...')
                    serial_port.write(b'SWT 13 OFF\r')
                    time.sleep(5)
                    serial_port.write(b'SWT 13 OFF\r')
                    os.system('clear')
                    print(f'Blower BLDC Reset complete')
                    time.sleep(2)
                else:
                    print(f'Blower BLDC Reset...')
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFF&u=13" -k -s')
                    time.sleep(5)
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=13" -k -s')
                    os.system('clear')
                    print(f'Blower BLDC Reset complete')
                time.sleep(2)

        def SCAA(self):  # Clears alarms for POST@
            if ST_Link == 1:
                serial_port.write(b'SYS 0 CAA\r')
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SYS&cmd=CAA&u=0" -k -s -s')
                os.system('clear')
            print('Alarms Cleared')
            time.sleep(2)

        def SSPHT(self):  # SystemStartPreHeaT
            if ST_Link == 1:
                serial_port.write(b'BCP 0 BGPH\r')
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BGPH&u=0" -k -s')

        def PYRAAPP(self):
            os.system('sudo systemctl restart roaster-app.service')
            time.sleep(1)
            os.system('sudo snap restart wpe-webkit-mir-kiosk')
            print('Pyra App Restarted')

        def BLUWEIGHT(self):
            if ST_Link == 1:
                x = str(f'W\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')[2:]
                self.v = str(response)
            else:
                self.v = os.popen(
                    f'curl "https://localhost:8443/roaster/sensor?m=BLU&cmd=GALWX&u=0" -k -s -s').read()
                os.system('clear')
                self.v = self.v.split('"')
                self.v = str(self.v[11])
            print(f'BLU Weight: {str(self.v)}lbs.')

        def BLULOAD(self):
            if ST_Link == 1:
                x = str(f'BLU 0 SALLX\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(
                    f'curl "https://localhost:8443/roaster/sensor?m=BLU&cmd=SALLX&u=0" -k -s -s')
            os.system('clear')
            print('BLU Loading')

        def BLUTARE(self):  # todo Ask Pierre how he's handling this
            if ST_Link == 1:
                x = str(f'BLU 0 GALTX\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')[2:]
                self.v = str(response)
            else:
                os.system(
                    f'curl "https://localhost:8443/roaster/sensor?m=BLU&cmd=GALTX&u=0" -k -s -s')
            os.system('clear')
            print('BLU Tare')

        def BLUPURGE(self):
            os.system(
                f'curl "https://localhost:8443/roaster/sensor?m=BLU&cmd=SALPX&u=0" -k -s -s')
            os.system('clear')
            print('BLU Purge')

        def BLUSTOP(self):
            if ST_Link == 1:
                x = str(f'BLU 0 SALXX\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(
                    f'curl "https://localhost:8443/roaster/sensor?m=BLU&cmd=SASSX&u=0" -k -s -s')
            os.system('clear')
            print('BLU Stop')

        def BLUEXIT(self):
            if ST_Link == 1:
                x = str(f'BLU 0 SALXX\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(
                    f'curl "https://localhost:8443/roaster/sensor?m=BLU&cmd=SALXX&u=0" -k -s -s')
                os.system('clear')
            print('BLU Exit')

        def STESTOPT(self):
            os.system('clear')
            mask = int('1', 2)
            er_tb = {0: '[Save N/V RAM            ]',
                     1: '[Set Firmware Debug      ]',
                     2: '[FlashRegTimer           ]',
                     3: '[Erase NvReg Flash       ]',
                     4: '[Main Blower Test        ]',
                     5: '[Log Roast Curve Download]',
                     6: '[Aux Heater On Test      ]',
                     7: '[Short Cool Cycle        ]',
                     8: '[Aux On During Preheat   ]',
                     9: '[Unlimited Preheat Time  ]',
                     10: '[DefeatPowerInterlock    ]',
                     11: '[LogCmdProcessing        ]',
                     12: '[Batch Roasting Test     ]',
                     13: '[Bypass Debug Mode       ]',
                     14: '[CoolBeansInDrumTest     ]',
                     15: '[BypassDisable           ]'}
            er_st = {}
            bin_st = {}
            if ST_Link == 1:
                serial_port.write(b'MISC 0 GTMD\r')
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                self.state = str(response[2:])
                self.state = int(self.state)

            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=GTMD&u=0" -k -s -s').read()
                self.state = self.state[42:-3]
                self.state = int(self.state)
                os.system('clear')

            for x in er_tb:

                byte1 = int(mask)
                map = byte1 & self.state
                if x == 0:
                    er_st[x] = ('[  ---  ]')
                    bin_st[x] = str(mask)
                else:
                    if map == 0:
                        er_st[x] = ('[  OFF  ]')
                        bin_st[x] = str(mask)
                    elif map >= 1:
                        er_st[x] = ('[  ON   ]')
                        bin_st[x] = str(mask)
                mask = mask << 1
            os.system('clear')
            print(f'System Test Options {str(self.state)} Machine: {str(mname)}')
            print('')
            print('[Options                 ] [On/Off ] Decimal')
            print('____________________________________________')

            for x in er_tb:
                print(f'{str(er_tb[x])} {str(er_st[x])} {str(bin_st[x])}')
            print('')
            state = input('Enter desired options: ')
            if ST_Link == 1:
                x = (f'MISC 0 STMD {str(state)}\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=STMD%20{str(state)}&u=0" -k -s -s')

            time.sleep(2)
            os.system('clear')
            bw.STESTOPTQ()

        def STESTOPTQ(self):  # System TEST OPTions Query @
            mask = int('1', 2)
            er_tb = {0: '[Save N/V RAM            ]',
                     1: '[Set Firmware Debug      ]',
                     2: '[FlashRegTimer           ]',
                     3: '[Erase NvReg Flash       ]',
                     4: '[Main Blower Test        ]',
                     5: '[Log Roast Curve Download]',
                     6: '[Aux Heater On Test      ]',
                     7: '[Short Cool Cycle        ]',
                     8: '[Aux On During Preheat   ]',
                     9: '[Unlimited Preheat Time  ]',
                     10: '[DefeatPowerInterlock    ]',
                     11: '[LogCmdProcessing        ]',
                     12: '[Batch Roasting Test     ]',
                     13: '[Bypass Debug Mode       ]',
                     14: '[CoolBeansInDrumTest     ]',
                     15: '[BypassDisable           ]'}
            er_st = {}
            bin_st = {}
            if ST_Link == 1:
                x = str(f'MISC 0 GTMD\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                response = response[2:]
                response = int(response)
                self.state = response
                self.state = response
                pass
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=GTMD&u=0" -k -s -s').read()
                self.state = self.state[42:-3]
                self.state = int(self.state)
                os.system('clear')

            for x in er_tb:
                byte1 = int(mask)
                map = byte1 & self.state
                if x == 0:
                    er_st[x] = ('[  ---  ]')
                    bin_st[x] = str(mask)
                else:
                    if map == 0:
                        er_st[x] = ('[  OFF  ]')
                        bin_st[x] = str(mask)
                    elif map >= 1:
                        er_st[x] = ('[  ON   ]')
                        bin_st[x] = str(mask)
                mask = mask << 1
            os.system('clear')
            print(f'System Test Options {str(self.state)} Machine: {str(mname)}')
            print('')
            print('[Options                 ] [On/Off ] Decimal')
            print('____________________________________________')
            for x in er_tb:
                print(f'{str(er_tb[x])} {str(er_st[x])} {str(bin_st[x])}')
            print('')

            return self.state

        def SGTMP_B(self):  # Get Blower Set Temp
            self.state = os.popen(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=GTMP&u=5" -k -s -s').read()
            os.system('clear')
            self.state = self.state[42:-3]
            self.state = int(self.state)
            print(f'Blower Target {str(self.state)} degrees.')
            return self.state

        def SGTMP_A(self):  # Get Aux Set Temp
            self.state = os.popen(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=GTMP&u=4" -k -s -s').read()
            os.system('clear')
            self.state = self.state[42:-3]
            self.state = int(self.state)
            print(f'Aux Target {str(self.state)} degrees.')
            return self.state

        def SPIP(self):  # System Public IP @
            self.pip = os.popen('curl ipinfo.io/ip').read()
            self.pip = str(self.pip)
            os.system('clear')
            print(f'Public IP {str(self.pip)}')
            return self.pip

        def SSETUP(self):  # ST interlock Bypass
            os.system(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=STMD%201281&u=0" -k -s -s')  # Set
            os.system('clear')
            print('ST Interlock Bypassed')
            bw.SEBUCKET()
            print('SRO Set')

        def SSETUP_E(self):
            os.system(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=STMD%209&u=0" -k -s -s')  # Erase
            os.system('clear')
            print('ST Interlock Erased')

        '''''''''
                            NOTES!!! Value entered in decimal.  Add '1' at the end to save in NV RAM
                    INFO  Cooler Agitator OFF
                    INFO       0x0002(    2) Set Firmware Debug
                    INFO       0x0008(    8) Erase NvReg Flash
                    INFO       0x0010(   16) Main Blower Test
                    INFO       0x0020(   32) Log Roast Curve Download
                    INFO       0x0040(   64) Aux Heater On Test
                    INFO       0x0080(  128) Short Cool Cycle
                    INFO    On 0x0100(  256) Aux On During Preheat
                    INFO       0x0200(  512) Unlimited Preheat Time
                    INFO    On 0x0400( 1024) DefeatPowerInterlock
                    INFO       0x8000(32768) Bypass Disable
                    INFO       0x0800( 2048) Log Command Processing
                    INFO       0x1000( 4096) Batch Roasting Test
                    INFO  roasterOptions: 0x0000(0)
                    INFO       0x0002(   2) Batch Roasting
                    INFO       0x0004(   4) Disable Preheat Ramp
                    INFO       0x0008(   8) Enable Bean Confirmation Required
                    INFO       0x0010(  16) Enable Bucket Detect
                    INFO       0x0020(  32) Enable AST
                    INFO       0x0040(  64) Disable POST Clear Event
                    INFO       0x0080( 128) Enable POST TC Clear Event
                    INFO       0x0100( 256) Enable Interlock Fail Description   


        '''''''''

        def SEBUCKET(self):
            opt = str('49')
            os.system(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SRO%20{str(opt)}&u=0" -k -s -s')
            os.system('clear')
            print('Bucket Detect Enabled')

        def SROPT(self):  # System Roaster OPTions
            now = datetime.datetime.now()
            ddate = (now.strftime("%m-%d-%Y"))
            ttime = (now.strftime("%H:%M:%S"))
            global bit
            bit = 1
            y = bw.SROPTQ()
            os.system('clear')
            print(f'Set Roaster Options Machine: {str(mname)}')
            mask = int('1', 2)
            er_tb = {0: '[Spare                              ]',
                     1: '[Batch Roasting                     ]',
                     2: '[Disable Preheat Ramp               ]',
                     3: '[Enable Bean Confirmation Required  ]',
                     4: '[Enable Bucket Detect              *]',
                     5: '[Enable AST                        *]',
                     6: '[Disable POST Clear Event           ]',
                     7: '[Enable POST TC Clear Event         ]',
                     8: '[Enable Interlock Fail Description *]',
                     9: '[EnableChaffElevatorNormallyClosed  ]',
                     10: '[EnableDualExitSensors  < R310      ]',
                     11: '[EnableNormallyOpenExitSensors      ]'
                     }
            er_st = {}
            opt_lst = {}
            if ST_Link == 1:
                serial_port.write(b'BCP 0 GRO\r')
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                self.state = str(response[2:])
                self.state = int(self.state)
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GRO&u=0" -k -s').read()
                self.state = str(self.state)
                self.state = self.state[42:-3]
                self.state = int(self.state)
            os.system('clear')
            print(f'System Roaster Options {str(self.state)} Machine: {str(mname)}')
            print('')
            print('[Options                            ] [On/Off] Decimal')
            print('______________________________________________________')
            for x in er_tb:
                byte1 = int(mask)
                map = byte1 & self.state
                if map == 0:
                    er_st[x] = ('[  Off ]')
                    opt_lst[x] = str(mask)
                elif map >= 1:
                    er_st[x] = ('[  On  ]')
                    opt_lst[x] = str(mask)
                mask = mask << 1
                t = (f'{str(er_tb[x])} {str(er_st[x])} ')

            for x in er_tb:
                if x <= 0:
                    pass
                else:
                    print(f'{str(er_tb[x])} {str(er_st[x])} {str(opt_lst[x])}')
            print('')
            print('* On By Default')
            opt = input('Enter Options : ')
            if ST_Link == 1:
                x = (f'BCP 0 SRO {str(opt)}\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SRO%20{str(opt)}&u=0" -k -s -s')  # Set
            os.system('clear')
            print(f'Roaster options set to "{str(opt)}" on {str(ddate)} @ {str(ttime)}.')
            time.sleep(2)
            bw.SROPTQ()
            '''''''''
            Query curl "https://localhost:8443/roaster/sensor?m=BCP&cmd=GRO&u=0" -k -s
            INFO  roasterOptions: 0x0000(0)
            '''''''''

        def SROPTQ(self):  # System Roaster OPTions Query@
            mask = int('1', 2)
            er_tb = {0: '[Spare                              ]',
                     1: '[Batch Roasting                     ]',
                     2: '[Disable Preheat Ramp               ]',
                     3: '[Enable Bean Confirmation Required  ]',
                     4: '[Enable Bucket Detect              *]',
                     5: '[Enable AST                        *]',
                     6: '[Disable POST Clear Event           ]',
                     7: '[Enable POST TC Clear Event         ]',
                     8: '[Enable Interlock Fail Description *]',
                     9: '[EnableChaffElevatorNormallyClosed  ]',
                     10: '[EnableDualExitSensors  < R310      ]',
                     11: '[EnableNormallyOpenExitSensors      ]'
                     }
            er_st = {}
            opt_lst = {}

            if ST_Link == 1:
                serial_port.write(b'BCP 0 GRO\r')
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                self.state = str(response[2:])
                self.state = int(self.state)
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GRO&u=0" -k -s').read()
                self.state = str(self.state)
                self.state = self.state[42:-3]
                self.state = int(self.state)
            os.system('clear')
            print(f'System Roaster Options {str(self.state)} Machine: {str(mname)}')
            print('')
            print('[Options                            ] [On/Off] Decimal')
            print('______________________________________________________')
            for x in er_tb:
                byte1 = int(mask)
                map = byte1 & self.state
                if map == 0:
                    er_st[x] = ('[  Off ]')
                    opt_lst[x] = str(mask)
                elif map >= 1:
                    er_st[x] = ('[  On  ]')
                    opt_lst[x] = str(mask)
                mask = mask << 1
            for x in er_tb:
                if x <= 0:
                    pass
                else:
                    print(f'{str(er_tb[x])} {str(er_st[x])} {str(opt_lst[x])}')
            print('')
            print('* On By Default')
            return self.state

        def SAGI(self):  # System Agitator I(Current) @
            if ST_Link == 1:
                x = str(f'MOT 1 GMI\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                response = response.split(' ')
                self.v = response[2]
                if len(self.v) == 2:
                    a = str(self.v[:1])
                    b = str(self.v[-1])
                    self.v = str(a + '.' + b)
                else:
                    self.v = str('0.' + self.v)
            else:
                try:
                    self.v = os.popen(
                        f'curl -k -s -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MOT&cmd=GMI&u=1"').read()
                    os.system('clear')
                    self.z, self.x = self.v.split('p1":"')
                    self.t, self.u = self.x.split('","p2":"')
                    self.v = self.t
                    if len(self.v) == 2:
                        a = str(self.v[:1])
                        b = str(self.v[-1])
                        self.v = str(a + '.' + b)
                    else:
                        self.v = str('0.' + self.v)
                except ValueError:
                    if elog == 1:
                        logger.exception('Error ' + self.v)
                    self.v = ('0')
            print('Agitator Current ' + self.v)
            return self.v

        def SBP(self, distance):  # SystemByPass @
            if ST_Link == 1:
                x = (f'VOUT 8 PWM {str(distance)}\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VOUT&cmd=PWM%20{str(distance)}&u=8" -k -s')
            os.system('clear')
            print('Bypass @  ' + str(distance))

        def SAGOP(self):  # System Agitator On (Pyra) PS5>
            Speed2 = int(100)
            if ST_Link == 1:
                x = str(f'SWT 5 ON\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=5" -k -s')
            os.system('clear')
            print(f'Agitator On')

        def SAGOFFP(self):  # System Agitator OFF On (Pyra) PS5>
            if ST_Link == 1:
                x = str(f'SWT 5 OFF\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFF&u=5" -k -s')

            os.system('clear')
        print('Drum Agitator set to off')

        if hardware_rev == 3:
            def SAGO(self):  # System Agitator On (Pyra)
                Speed2 = int(100)
                if ST_Link == 1:
                    x = (f'VOUT 3 PWM {str(Speed2)}\r')
                    serial_port.write(bytes(x, 'utf-8'))
                else:
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VOUT&cmd=PWM%20{str(Speed2)}&u=3" -k -s')
                os.system('clear')
                print(f'Agitator On')
        else:
            def SAGO(self, Speed, Direction):  # System Agitator On @
                loop = int(2)
                Speed2 = (str(Speed) + '0')
                Speed2 = int(Speed2)
                while loop != 0:  # Note have to repeat due to legacy ST Bug
                    if ST_Link == 1:
                        x = str(f'VOUT 3 PWM {str(Speed2)}\r')
                        serial_port.write(bytes(x, 'utf-8'))
                    else:
                        os.system(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VOUT&cmd=PWM%20{str(Speed2)}&u=3" -k -s')
                    if Direction == 0:
                        direction = str('Clockwise')
                        try:
                            if ST_Link == 1:
                                x = str(f'SWT 5 OFF\r')
                                serial_port.write(bytes(x, 'utf-8'))
                            else:
                                os.system(
                                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFF&u=5" -k -s')
                        except ValueError:
                            if ST_Link == 1:
                                x = str(f'SWT 5 OFF\r')
                                serial_port.write(bytes(x, 'utf-8'))
                            else:
                                os.system(
                                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFF&u=5" -k -s')
                    elif Direction == 1:
                        try:
                            direction = str('Anti Clockwise')
                            if ST_Link == 1:
                                x = str(f'SWT 5 ON\r')
                                serial_port.write(bytes(x, 'utf-8'))
                            else:
                                os.system(
                                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=5" -k -s')
                        except ValueError:
                            direction = str('Anti Clockwise')
                            if ST_Link == 1:
                                x = str(f'SWT 5 ON\r')
                                serial_port.write(bytes(x, 'utf-8'))
                            else:
                                os.system(
                                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=5" -k -s')
                    else:
                        print('Error, Not valid direction!')
                    loop -= 1
                os.system('clear')
                print(f'Agitator speed set to {str(Speed)}% Direction {str(direction)}')

        def SAGOFF(self):  # System Agitator OFF @
            try:
                if ST_Link == 1:
                    x = str(f'VOUT 3 PWM 0\r')
                    serial_port.write(bytes(x, 'utf-8'))
                else:
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VOUT&cmd=PWM%200&u=3" -k -s')
                os.system('clear')
            except ValueError:
                if ST_Link == 1:
                    x = str(f'VOUT 3 PWM 0\r')
                    serial_port.write(bytes(x, 'utf-8'))
                else:
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VOUT&cmd=PWM%200&u=3" -k -s')
                os.system('clear')
            print('Drum Agitator set to off')

        def SAGR(self):  # System Agitator RPM @
            try:
                if ST_Link == 1:
                    x = str(f'MOT 1 GMI\r')
                    serial_port.write(bytes(x, 'utf-8'))
                    response = serial_port.readline()
                    response = response.decode('utf-8')
                    response = str(response.replace('\r', ''))
                    response = response.split(' ')
                    self.v = response[1]
                else:
                    self.v = os.popen(
                        f'curl -k -s -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MOT&cmd=GMI&u=1"').read()
                    self.x, self.z = self.v.split('p2":"')
                    self.v = self.z[:-3]
                    a = str(self.v[:2])
                    b = str(self.v[-1])
                    self.v = str(a + '.' + b)
            except ValueError:
                if elog == 1:
                    logger.exception('Retry ' + self.v)
                else:
                    pass
                self.v = ('0')
            os.system('clear')
            print('Agitator RPM ', self.v)
            return self.v

        def SATC(self):  # System All TC @
            label = {0: '[  Inlet    ]',
                     1: '[Bean Front ]',
                     2: '[ByPass Exit]',
                     3: '[Heater Out ]',
                     4: '[   Blower  ]',
                     5: '[    CAT    ]',
                     6: '[Drum Bottom]',
                     7: '[ Not Used  ]',
                     8: '[ Not Used  ]',
                     9: '[ Not Used  ]',
                     10: '[ Not Used  ]',
                     11: '[Cool Tray  ]'}
            label2 = {0: '[Heater Out ]',
                      1: '[  Inlet    ]',
                      2: '[ByPass Exit]',
                      3: '[Bean       ]',
                      4: '[Drum Bottom]',
                      5: '[Cool Tray  ]'}

            port = {0: '[ I2C1 J5 ]',
                    1: '[ I2C1 J6 ]',
                    2: '[ I2C3 J8 ]',
                    3: '[ I2C3 J3 ]',
                    4: '[ I2C1 J3 ]',
                    5: '[ I2C3 J5 ]',
                    6: '[ 12C1 J8 ]',
                    7: '[ 12C1 J2 ]',
                    8: '[ 12C1 J9 ]',
                    9: '[ 12C3 J9 ]',
                    10: '[ 12C3 J2 ]',
                    11: '[ 12C3 J6 ]'}
            port2 = {0: '[ I2C1 J2 ]',
                     1: '[ I2C1 J5 ]',
                     2: '[ I2C1 J3 ]',
                     3: '[ I2C1 J6 ]',
                     4: '[ I2C1 J8 ]',
                     5: '[ I2C1 J9 ]'}
            temp = {}
            ssn = bw.SSN()
            ssn = ssn.split('0')
            ssn = ssn[0]
            if ssn == ('PR'):
                for x in label:
                    tmp = bw.STC(x)
                    temp[x] = (f'[{str(tmp)}]')
                os.system('clear')
                print(f'System TCs')
                for x in label:
                    if label[x] == ('[ Not Used  ]'):
                        if temp[x] == ('[32.0]'):
                            pass
                        else:
                            print(f'{str(label[x])} {str(port[x])} {str(temp[x])}')
                        pass
                    else:
                        print(f'{str(label[x])} {str(port[x])} {str(temp[x])}')
            elif ssn == ('R'):
                for x in label:
                    tmp = bw.STC(x)
                    temp[x] = (f'[{str(tmp)}]')
                os.system('clear')
                print(f'System TCs')
                for x in label:
                    if label[x] == ('[ Not Used  ]'):
                        if temp[x] == ('[32.0]'):
                            pass
                        else:
                            print(f'{str(label[x])} {str(port[x])} {str(temp[x])}')
                        pass
                    else:
                        print(f'{str(label[x])} {str(port[x])} {str(temp[x])}')
            else:
                for x in label2:
                    tmp = bw.STC(x)
                    temp[x] = (f'[{str(tmp)}]')
                os.system('clear')
                print(f'System TCs')
                for x in label2:
                    if label[x] == ('[ Not Used  ]'):
                        if temp[x] == ('[32.0]'):
                            pass
                        else:
                            print(f'{str(label2[x])} {str(port2[x])} {str(temp[x])}')
                        pass
                    else:
                        print(f'{str(label2[x])} {str(port2[x])} {str(temp[x])}')

        def SAUX(self):  # Enables Aux for preheat @
            os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=STMD%20768&u=0" -k -s -s')

        def SBD(self, state):  # System Belly Drop @
            if ST_Link == 1:
                if state == 1:
                    x = str(f'SWT 7 ON\r')
                    print('BD Open ')
                elif state == 0:
                    x = str(f'SWT 8 ON\r')
                    print('BD Close ')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
            else:
                if state == 1:
                    try:
                        os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=7" -k -s')
                        os.system('clear')
                    except ValueError:
                        os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=7" -k -s')
                        os.system('clear')
                    print('BD Open ')
                elif state == 0:
                    try:
                        os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=8" -k -s')
                        os.system('clear')
                    except ValueError:
                        os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=8" -k -s')
                        os.system('clear')
                    print('BD Close ')
                else:
                    os.system('clear')
                    print('Error')

        def SBDT(self):  # System Belly Drop Toggle
            s = bw.SBDS()
            if s == 0:
                try:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=7" -k -s')
                    os.system('clear')
                except ValueError:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=7" -k -s')
                    os.system('clear')
                print('BD Open ')
            elif s == 1:
                try:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=8" -k -s')
                    os.system('clear')
                except ValueError:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=8" -k -s')
                    os.system('clear')
                print('BD Close ')
            else:
                os.system('clear')
                print('Error')

        def SBE(self, state):  # System Bean Exit @
            if ST_Link == 1:
                if state == 1:
                    x = str(f'SWT 4 ONA\r')
                elif state == 0:
                    x = str(f'SWT 4 OFFA\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                if state == 1:
                    try:
                        os.system(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ONA&u=4" -k -s')
                        os.system('clear')
                    except ValueError:
                        os.system(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ONA&u=4" -k -s')
                        os.system('clear')
                    print('BE Open ')
                elif state == 0:
                    try:
                        os.system(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFFA&u=4" -k -s')
                        os.system('clear')
                    except ValueError:
                        os.system(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFFA&u=4" -k -s')
                        os.system('clear')
                    print('BE Close')
                else:
                    os.system('clear')
                    print('Error')

        def SBET(self):  # System Bean Exit Toggle @
            s = bw.SBES()
            if s == 2:
                try:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ONA&u=4" -k -s')
                    os.system('clear')
                except ValueError:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ONA&u=4" -k -s')
                    os.system('clear')
                print('BE Open ')
            elif s == 0:
                try:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFFA&u=4" -k -s')
                    os.system('clear')
                except ValueError:
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFFA&u=4" -k -s')
                    os.system('clear')
                print('BE Close')
            else:
                os.system('clear')
                print('Error')

        def SBES(self):  # System Bean Exit Status @
            if ST_Link == 1:
                x = str(f'BCP 0 BXS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')[2:]
                ssn = bw.SSN()
                ssn = ssn.split('0')
                ssn = ssn[0]
            else:
                try:
                    self.state = os.popen(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BXS&u=0" -k -s').read()
                    self.state = self.state[42:-3]
                    self.state = int(self.state)
                except ValueError:
                    while len(self.state) != 46:
                        if elog == 1:
                            logger.error('Error ' + self.state)
                            time.sleep(1)
                        self.state = os.popen(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BXS&u=0" -k -s').read()
                        self.state = self.state[42:-3]
                        self.state = int(self.state)
                os.system('clear')
                ssn = bw.SSN()
                ssn = ssn.split('0')
                ssn = ssn[0]

            if ssn == ('R'):
                if self.state == 2:
                    os.system('clear')
                    print('Bean Exit Closed "Sensor"')
                elif self.state == 0:
                    os.system('clear')
                    print('Bean Exit Open "Sensor"')
                elif self.state == 3:
                    os.system('clear')
                    print('Bean Exit "Both"')
            elif ssn == ('PR'):
                if self.state == 2:
                    os.system('clear')
                    print('Bean Exit Closed "Sensor"')
                elif self.state == 0:
                    os.system('clear')
                    print('Bean Exit Open "Sensor"')
            elif ssn == ('M'):
                if self.state == 2:
                    os.system('clear')
                    print('Bean Exit Closed "Sensor"')
                elif self.state == 1:
                    os.system('clear')
                    print('Bean Exit Open "Sensor"')
            elif ssn == ('N'):
                if self.state == 2:
                    os.system('clear')
                    print('Bean Exit Closed "Sensor"')
                elif self.state == 1:
                    os.system('clear')
                    print('Bean Exit Open "Sensor"')
            elif ssn == ('Q'):
                if self.state == 2:
                    os.system('clear')
                    print('Bean Exit Closed "Sensor"')
                elif self.state == 0:
                    os.system('clear')
                    print('Bean Exit Open "Sensor"')
            else:
                os.system('clear')
                print('Invalid')
            print(self.state)
            return self.state

        def SBL(self, state):  # System Bean Load @
            if state == 1:
                if ST_Link == 1:
                    x = str(f'SWT 3 ON\r')
                    serial_port.write(bytes(x, 'utf-8'))
                    response = serial_port.readline()
                else:
                    try:
                        os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=3" -k -s')
                        os.system('clear')
                    except ValueError:
                        os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=3" -k -s')
                        os.system('clear')
                print('BL Open ')
            elif state == 0:
                if ST_Link == 1:
                    x = str(f'SWT 3 OFF\r')
                    serial_port.write(bytes(x, 'utf-8'))
                else:
                    try:
                        os.system(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFF&u=3" -k -s')
                        os.system('clear')
                    except ValueError:
                        os.system(
                            f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFF&u=3" -k -s')
                        os.system('clear')
                print('BL Close')
            else:
                os.system('clear')
                print('Error')

        def SBLS(self):  # System Bean Load State @
            if ST_Link == 1:
                x = str(f'BCP 0 BLS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')[2:]
                self.state = int(self.state)
            else:
                try:
                    self.state = os.popen(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BLS&u=0" -k -s').read()
                    self.state = self.state[42:-3]
                    self.state = int(self.state)
                except ValueError:
                    self.state = os.popen(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BLS&u=0" -k -s').read()
                    self.state = self.state[42:-3]
                    self.state = int(self.state)
            if self.state == 1:
                self.state = int(2)
                os.system('clear')
                print('Invalid Both Sensors Not Present')
            elif self.state == 2:
                self.state = int(0)
                os.system('clear')
                print('Bean Load Closed "Sensor" ')
            elif self.state == 0:
                self.state = int(1)
                os.system('clear')
                print('Bean Load Open "Sensor" ')
            elif self.state == 3:
                self.state = int(2)
                os.system('clear')
                print('Invalid Both Sensors Are Present')
            return self.state

        def SBO(self, Speed):  # System Blower On @
            Speed2 = (str(Speed) + '0')
            Speed2 = int(Speed2)
            if ST_Link == 1:
                x = str(f'VFD 0 PWM {str(Speed2)}\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                try:
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VFD&cmd=PWM%20' + str(
                            Speed2) + '&u=0" -k -s')
                    os.system('clear')
                except ValueError:
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VFD&cmd=PWM%20' + str(
                            Speed2) + '&u=0" -k -s')
                    os.system('clear')
            print('Blower speed set to ' + str(Speed) + '%')

        def SBOFF(self):  # SystemBlowerOFF @
            if ST_Link == 1:
                x = str(f'VFD 0 PWM 0\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
            else:
                try:
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VFD&cmd=PWM%200&u=0" -k -s')
                    os.system('clear')
                except ValueError:
                    os.system(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VFD&cmd=PWM%200&u=0" -k -s')
                    os.system('clear')
            print('Blower set to off')

        def SCA(self, State):  # System Cooling Agitator @
            if State == 1:
                State = str('ON')
            elif State == 0:
                State = str('OFF')
            else:
                print('Invalid State')
            if ST_Link == 1:
                x = str(f'SWT 0 {str(State)}\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
            else:
                os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=' + str(
                        State) + '&u=0" -k -s')
            os.system('clear')
            print('Cooling Agitator ', State)

        def SHOPS(self):  # System HOPper State @
            if ST_Link == 1:
                x = str(f'BCP 0 GHS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.v = response.replace('\r', '')[2:]
            else:
                self.v = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GHS&u=0" -k -s').read()
                self.v = self.v[42:-3]
            os.system('clear')
            print('Hopper Present ', self.v)
            self.v = int(self.v)
            return self.v

        def SNET(self):  # System NETwork @
            self.sinternet = os.popen('ping -c 1 google.com').read()
            self.sinternet = self.sinternet.split(', ')
            self.sinternet = self.sinternet[2].split('%')
            if self.sinternet[0] == '0':
                self.bit = 1
            elif self.sinternet[0] == '1':
                self.bit = 0
            print(f'Internet Access {str(self.bit)}')
            return self.bit

        def SINFO(self):  # System INFOrmation @
            a = bw.SSN()
            b = bw.SVN()
            c = bw.SS()
            c = statelist[c]
            if c == -1:
                c = 10
            d = str(bw.SPIP())
            os.system('clear')
            print()
            print('Machine IP Address:     ', str(ip_address))
            print('Terminal IP Address:    ', ip_address_l)
            print('Public IP Address:      ', d)
            print(f'Serial Number:          ', f'{str(a)} {str(machine_series)}')
            print('ST Firmware Version:    ', b)
            print('BW Roaster Object Rev:  ', rev)
            print('Roaster State:          ', c)

        def SIP(self):  # System IP @
            self.v = ip_address
            print(self.v)
            return str(self.v)

        def SIPL(self):  # System IP Local @
            self.v = ip_address_l
            print(self.v)
            return self.v

        def SM24(self, state):
            if ST_Link == 1:
                if state == 1:
                    x = str(f'SWT 11 ON\r')
                    serial_port.write(bytes(x, 'utf-8'))
                elif state == 0:
                    x = str(f'SWT 11 OFF\r')
                    serial_port.write(bytes(x, 'utf-8'))

            else:
                if state == 1:
                    # os.system('sudo sbc -l swt 11 on')
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=ON&u=11" -k -s')
                elif state == 0:
                    # os.system('sudo sbc -l swt 11 off')
                    os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SWT&cmd=OFF&u=11" -k -s')
                else:
                    print('Invalid')
                    time.sleep(10)

        def SNPFB(self, Speed):  # System Negative Pressure Filter Box @
            print('Speed ', Speed)
            Speed2 = (str(Speed) + '0')
            Speed2 = int(Speed2)
            if ST_Link == 1:
                x = str(f'VOUT 1 PWM {str(Speed2)}\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=VOUT&cmd=PWM%20' + str(
                    Speed2) + '&u=1" -k -s')
            os.system('clear')
            print(f'FilterBox speed set to {str(Speed)}%')

        def SPH(self):  # System PreHeat @
            if ST_Link == 1:
                serial_port.write(b'BCP 0 SST 4\r')
                response = serial_port.readline()
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SST%204&u=0" -k -s')
            os.system('clear')
            print('Roaster Pre Heat Enabled')

        def SPHNH(self):  # System PreHeat No Heat
            os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SST%204&u=0" -k -s')
            os.system('clear')
            print('Roaster Pre Heat Enabled')
            time.sleep(3)
            bw.SSCT(0)

        def SINIT(self):  # System Init @
            if ST_Link == 1:
                serial_port.write(b'BCP 0 SST 1\r')
                response = serial_port.readline()
                # response = response.decode('utf-8')
                # self.ssn = str(response[2:])
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SST%201&u=0" -k -s')
            os.system('clear')
            print('Roaster Init')

        def SRB(self):  # System ReBoot @
            os.system('sudo reboot')
            print('Roaster Reboot')

        def SRO(self):  # System ROast # manual roast @
            os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SST%205&u=0" -k -s')
            os.system('clear')
            print('Roaster Manual Roast Enabled')

        def SRSTART(self):  # System ReStart @
            os.system(f'python3 /home/{str(ado_)}/Bellwether/BW_Shell.py')

        def SS(self):  # System Status @
            if ST_Link == 1:
                x = str(f'BCP 0 GST\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.z = response.replace('\r', '')[2:]
                self.z = int(self.z)
            else:
                try:
                    self.v = os.popen(f'curl "https://{str(ip_address)}:{str(port)}/roaster/state" -k -s -s').read()
                    # os.system('clear')
                    self.z = int(self.v[35:-1])
                except ValueError:
                    if elog == 1:
                        logger.error('ERROR ' + self.v)
                        time.sleep(1)
                    self.z = int(-1)
            statelist = ['Reset', 'init', 'Offline', 'Ready', 'PreHeat', 'Roast', 'Cool', 'Shutdown', 'Error',
                         'Standby']
            if self.z == -1:
                print('<NULL>')
            elif self.z == 0:
                print('Roaster state: "Reset"')
            elif self.z == 1:
                print('Roaster state: "Init"')
            elif self.z == 2:
                print('Roaster state: "Offline"')
            elif self.z == 3:
                print('Roaster state: "Ready"')
            elif self.z == 4:
                print('Roaster state: "PreHeat"')
            elif self.z == 5:
                print('Roaster state: "Roast"')
            elif self.z == 6:
                print('Roaster state: "Cool"')
            elif self.z == 7:
                print('Roaster state: "ShutDown')
            elif self.z == 8:
                print('Roaster state: "Error"')
            elif self.z == 9:
                print('Roaster state: "Standby"')
            return self.z

        def SSD(self):  # System ShutDown @
            if ST_Link == 1:
                x = str(f'BCP 0 SST 7\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system('curl -H "Content-Type: application/json" -X POST "https://' + ip_address +
                          ':' + str(port) + '/roaster/state" -d "{\\"state\\":7}" -k -s')
            time.sleep(2)
            os.system('clear')
            print('Roaster Shutdown')

        def SCO(self):  # System Cool @
            if ST_Link == 1:
                x = str(f'BCP 0 SST 6\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system('curl -H "Content-Type: application/json" -X POST "https://' + ip_address +
                          ':' + str(port) + '/roaster/state" -d "{\\"state\\":6}" -k -s')
                time.sleep(2)
            os.system('clear')
            print('Roaster Cool')

        def SSN(self):  # System Serial Number @
            try:
                if ST_Link == 1:
                    x = str(f'MISC 0 GSN\r')
                    serial_port.write(bytes(x, 'utf-8'))
                    response = serial_port.readline()
                    response = response.decode('utf-8')
                    self.ssn = response.replace('\r', '')[2:]

                else:
                    self.ssn = os.popen(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=GSN&u=0" -k -s -s').read()
                    self.ssn = self.ssn[42:-4]
                if self.ssn == (''):
                    self.ssn = str('<NULL>')
            except ValueError:
                self.ssn = str('<NULL>')
            print('Machine Serial # ', self.ssn)
            return self.ssn

        def SGRN(self):  # System Get Roaster Name
            if ST_Link == 1:
                serial_port.write(b'MISC 0 GRN\r')
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.ssn = str(response[2:])
                return self.ssn
            else:
                try:
                    self.ssn = os.popen(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=GRN&u=0" -k -s -s').read()
                    self.ssn = self.ssn[42:-3]
                    if self.ssn == (''):
                        self.ssn = str('<NULL>')
                except ValueError:
                    self.ssn = str('<NULL>')

                    # os.system('clear')
                print('Machine Name # ', self.ssn)
                return self.ssn

        def SGRV(self):  # System Get Roaster Version
            # curl -k -s “http://localhost:8080/version”
            try:
                self.ssn = os.popen('cat /opt/data/deploy/current_release').read()
                if self.ssn == (''):
                    self.ssn = ('DVT')
                elif self.ssn == ('"'):
                    self.ssn = ('Pyra EVT')
            except FileNotFoundError:
                self.ssn = str('Pyra')
            os.system('clear')
            print(f'Roaster App Ver. {str(self.ssn)}')
            return self.ssn

        def SSS(self):  # System Set State @
            print(statelist)
            print()
            state = input('Selection --> ')
            state = int(state)
            if state == 0:
                print('Roaster state: "Reset"')
            elif state == 1:
                print('Roaster state: "Init"')
            elif state == 2:
                print('Roaster state: "Offline"')
            elif state == 3:
                print('Roaster state: "Ready"')
            elif state == 4:
                print('Roaster state: "PreHeat"')
            elif state == 5:
                print('Roaster state: "Roast"')
            elif state == 6:
                print('Roaster state: "Cool"')
            elif state == 7:
                print('Roaster state: "ShutDown')
            elif state == 8:
                print('Roaster state: "Error"')
            elif state == 9:
                print('Roaster state: "Standby"')

            if ST_Link == 1:
                x = str(f'BCP 0 SST {str(state)}\r')
                serial_port.write(bytes(x, 'utf-8'))

            else:
                os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SST%20{str(state)}&u=0" -k -s')
            time.sleep(2)
            os.system('clear')

        def SSST(self):  # System Set ST SSN @
            series = input('Enter Series of Machine (P, N, M, PQ, Q, PR, R, PY, Y, PS, S): ')
            # series = ('R')
            series = series.upper()
            serial = input('Enter Serial Number of machine: ')
            if series == str('P'):
                series = str('1')
            if series == ('N'):
                series = str('2')
            if series == ('M'):
                series = str('3')
            if series == ('Q'):
                series = str('5')
            if series == ('PQ'):
                series = str('7')
            if series == ('R'):
                series = str('9')
            if series == ('PR'):
                series = str('10')
            if series == ('NR'):
                series = str('11')
            if series == ('S'):
                series = str('12')
            if series == ('PS'):
                series = str('13')
            if series == ('NS'):
                series = str('14')
            if series == ('Y'):
                series = str('15')
            if series == ('PY'):
                series = str('16')
            if series == ('NY'):
                series = str('17')

            if ST_Link == 1:
                x = str(f'MISC 0 SSN {str(series)} {str(serial)}\r')
                serial_port.write(bytes(x, 'utf-8'))

            else:
                a = str(f'curl -k -s -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=SSN%20')
                b = str('%20')
                c = str('&u=0"')
                end = (a + series + b + serial + c)
                time.sleep(5)
                os.system(end)

            print(f'Serial Number set to: {str(bw.SSN())}')
            '''''''''
                FOX Code
                    enum SERIES {
                  UnknownSeries = 0,
                  FirstSeries   = UnknownSeries,
                  Pseries       = 1,
                  Nseries       = 2,
                  Mseries       = 3,
                  Tseries       = 4,
                  Qseries       = 5,
                  TseriesProto  = 6,
                  QseriesProto  = 7,
                  TseriesNPI    = 8,
                  Rseries       = 9,
                  RseriesProto  = 10,
                  RseriesNPI    = 11,
                  Sseries       = 12,
                  SseriesProto  = 13,
                  SseriesNPI    = 14,
                  Yseries       = 15,
                  YseriesProto  = 16,
                  YseriesNPI    = 17,
                  UniversalSeries = 100,
                  LastSeries      = UniversalSeries,
                  numSeries,
                };
            //Use a macro since even a constexpr of constant parameters is not a constant.....
            #define MODEL_FROM_SERIES_NUMBER(series, number) ( (((unsigned long)(series))<<24) | (unsigned long)(number) )
            //Supported build configurations
             enum MODEL {
              ModelUnknown      = MODEL_FROM_SERIES_NUMBER(UnknownSeries, 0),
              ModelUniversal    = MODEL_FROM_SERIES_NUMBER(UniversalSeries, 0),
              ModelRC_Px        = MODEL_FROM_SERIES_NUMBER(Pseries, 0),
              ModelRC_Nx        = MODEL_FROM_SERIES_NUMBER(Nseries, 0),
              ModelRC_Mx        = MODEL_FROM_SERIES_NUMBER(Mseries, 0),
              ModelRC_PTx       = MODEL_FROM_SERIES_NUMBER(TseriesProto,0),
              ModelRC_Tx        = MODEL_FROM_SERIES_NUMBER(Tseries, 0),
              ModelRC_PQx       = MODEL_FROM_SERIES_NUMBER(QseriesProto,0),
              ModelRC_Qx        = MODEL_FROM_SERIES_NUMBER(Qseries, 0),
              ModelRC_Rx        = MODEL_FROM_SERIES_NUMBER(Rseries, 0),
              ModelRC_PRx       = MODEL_FROM_SERIES_NUMBER(RseriesProto, 0),
              ModelRC_NRx       = MODEL_FROM_SERIES_NUMBER(RseriesNPI, 0),
              ModelRC_Sx        = MODEL_FROM_SERIES_NUMBER(Sseries, 0),
              ModelRC_PSx       = MODEL_FROM_SERIES_NUMBER(SseriesProto, 0),
              ModelRC_NSx       = MODEL_FROM_SERIES_NUMBER(SseriesNPI, 0),
              ModelRC_NTx       = MODEL_FROM_SERIES_NUMBER(TseriesNPI, 0),
            };
            enum SeriesID {
              P = ModelRC_Px,
              N = ModelRC_Nx,
              M = ModelRC_Mx,
              T = ModelRC_Tx,
              Q = ModelRC_Qx,
              R = ModelRC_Rx,
              S = ModelRC_Sx,
              U = ModelUniversal,
              PT = ModelRC_PTx,
              PQ = ModelRC_PQx,
              PR = ModelRC_PRx,
              PS = ModelRC_PSx,
              NT = ModelRC_NTx,
              NR = ModelRC_NRx,
              NS = ModelRC_NSx,
              numSeriesIDs = numSeries,
            };
            '''''''''

        def SSTB(self):  # System StandBy @
            if ST_Link == 1:
                serial_port.write(b'BCP 0 SST 9\r')
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SST%209&u=0" -k -s')
                time.sleep(2)
                os.system('clear')
            print('Roaster Standby')

        def STC(self, Channel):  # System TC @
            ssn = bw.SSN()
            ssn = ssn.split('0')
            ssn = ssn[0]
            if hardware_rev == 2:
                print('I2C')
                tc_label = ['Inlet', 'Bean Front', 'ByPass Exit', 'Heater Out', 'Blower', 'CAT', 'Drum Bottom',
                            '7', '8', '9', '10', 'Cooling Tray']

                if Channel >= 12:
                    print('Input Out of Range')
                else:
                    if ST_Link == 1:
                        x = str(f'TMP {str(Channel)} VAL\r')
                        serial_port.write(bytes(x, 'utf-8'))
                        response = serial_port.readline()
                        response = response.decode('utf-8')
                        self.v = response.replace('\r', '')
                        self.v = self.v.split(' ')
                        self.v = self.v[2]
                        self.z = (float(self.v) / 2) * 9 / 5 + 32
                    else:
                        try:
                            self.v = os.popen(
                                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=TMP&cmd=VAL&u={str(Channel)}" -k -s').read()
                            if elog == 1:
                                logger.info('TC Return String ' + self.v)
                            self.x, self.y = self.v.split('p1":"')
                            self.z = self.y[:-3]
                            self.z = (float(self.z) / 2) * 9 / 5 + 32
                        except ValueError:
                            if elog == 1:
                                logger.exception('Retry' + self.v)
                            time.sleep(1)
                        self.v = -1
                    os.system('clear')
                    print('I2C Channel', Channel, tc_label[Channel], self.z, 'Degrees F')
                    return self.z

            elif hardware_rev == 3:
                print('I2C (Pyra)')
                tc_label = ['Heater Out', 'Inlet', 'ByPass Exit', 'Bean Front', 'Drum Bottom', 'Cooling Tray']
                if Channel >= 6:
                    print('Input Out of Range')
                else:
                    try:
                        if ST_Link == 1:
                            x = str(f'TMP {int(Channel)} VAL\r')
                            serial_port.write(bytes(x, 'utf-8'))
                            self.v = serial_port.readline()
                            self.v = self.v.decode('utf-8')[2:]
                            self.v = self.v.split(' ')
                            self.v = self.v[1]
                            self.z = (float(self.v) / 2) * 9 / 5 + 32

                            pass
                        else:
                            self.v = os.popen(
                                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=TMP&cmd=VAL&u={str(Channel)}" -k -s').read()
                            if elog == 1:
                                logger.info('TC Return String ' + self.v)
                            self.x, self.y = self.v.split('p1":"')
                            self.z = self.y[:-3]
                            self.z = (float(self.z) / 2) * 9 / 5 + 32
                    except ValueError:
                        if elog == 1:
                            logger.exception('Retry' + self.v)
                        time.sleep(1)
                        self.v = -1
                    os.system('clear')
                    print('I2C Channel', Channel, tc_label[Channel], self.z, 'Degrees F')
                    return self.z
            else:
                input('Series Not Supported.')

        def SVN(self):  # System Version Number @
            try:
                if ST_Link == 1:
                    x = str(f'MISC 0 FWV\r')
                    serial_port.write(bytes(x, 'utf-8'))
                    response = serial_port.readline()
                    response = response.decode('utf-8')[2:]
                    self.svn = response.replace('\r', '')
                else:
                    self.svn = os.popen(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=FWV&u=0" -k -s -s').read()
                    self.svn = self.svn[42:-3]
                if self.svn == (''):
                    self.svn = str('<NULL>')
            except ValueError:
                self.ssn = ('<NULL>')
            os.system('clear')
            print('ST FW Ver. ', str(self.svn))
            return str(self.svn)

        def SGCS(self):  # System Get Chaff State @
            mask = int('1', 2)
            er_tb = {0: '[Spare          ]',
                     1: '[Water Bottle   ]',
                     2: '[Chaff Can      ]',
                     3: '[Chaff Elevator ]'}
            er_st = {}
            if ST_Link == 1:
                x = str(f'BCP 0 GCS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')[2:]
                self.state = int(response.replace('\r', ''))
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GCS&u=0" -k -s').read()
                self.state = self.state[42:-3]
                self.state = int(self.state)

            os.system('clear')
            print('')
            print(f'Chaff Assembly State: {str(self.state)}')
            print('')

            for x in er_tb:
                if x == 0:
                    pass
                byte1 = int(mask)
                map = byte1 & self.state
                if map == 0:
                    er_st[x] = ('[  0  ]')
                elif map >= 1:
                    er_st[x] = ('[  1  ]')
                if x == 0:
                    pass
                else:
                    mask = mask << 1

            for x in er_tb:
                if x <= 0:
                    pass
                else:
                    print(f'{str(er_tb[x])} {str(er_st[x])}')
            print('')
            return int(self.state)

        def SGBS(self):  # System Get Bucket State @
            if ST_Link == 1:
                x = str(f'BCP 0 GBS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')[2:]
                self.state = int(response.replace('\r', ''))
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GBS&u=0" -k -s').read()
                self.state = str(self.state)
                self.state = self.state[42:-3]
            self.state = int(self.state)
            os.system('clear')
            print('Bucket State ', str(self.state))
            if self.state == 0:
                print('Not Supported')
            elif self.state == 1:
                print('Bucket Not Present')
            elif self.state == 2:
                print('Bucket Present')
            elif self.state == 3:
                print('Full Bucket Present')
            elif self.state == 4:
                print('Empty Bucket Present')
            else:
                print('Out Of Range')
            return str(self.state)

        def SBPS(self):  # System ByPass Status
            if ST_Link == 1:
                x = str(f'BCP 0 BYPS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')[2:]

            else:
                self.state = os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BYPS&u=0" -k -s')
            return self.state
            # print(self.state)

        def SBPS_A(self):  # System ByPass Status (Absolute) @
            if ST_Link == 1:
                x = str(f'BCP 0 BYPS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')[2:]
                response = response.split(' ')
                self.a = response[1]

            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BYPS&u=0" -k -s').read()
                os.system('clear')
                self.state = self.state.split('"')
                self.a = int(self.state[15])
            print(self.a)
            return self.a

        def SBPS_E(self):  # System ByPass Status (Encoder) @
            if ST_Link == 1:
                x = str(f'BCP 0 BYPS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')[2:]
                response = response.split(' ')
                self.a = response[2]
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BYPS&u=0" -k -s').read()
                os.system('clear')
                self.state = self.state.split('"')
                self.a = self.state[19]
            print(self.a)
            return self.a

        def SBPS_T(self):  # System ByPass Status (Target) @
            if ST_Link == 1:
                x = str(f'BCP 0 BYPS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')[2:]
                response = response.split(' ')
                self.a = response[0]
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=BYPS&u=0" -k -s').read()
                os.system('clear')
                self.state = self.state.split('"')
                self.a = int(self.state[11])
            print(self.a)
            return self.a

        def SPT(self, f):  # System Preheat Target
            f = (((f - 32) * 5) / 9)
            # os.system(f'curl -k -s -s https://localhost:8443/roaster/sensor?m=BCP&cmd=STMP%20176&u=0')
            os.system(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=STMP%20{str(f)}&u=0" -k -s')

        def SPA(self, record, time, f):  # System Preheat Array
            f = (((f - 32) * 5) / 9)
            test = str(
                f'curl -k -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SRP%20{str(record)}%20{str(time)}%20{str(f)}&u=0" -k -s')
            # curl -k -s "https://localhost:8443/roaster/sensor?m=BCP&cmd=SRP%201%205%2023&u=0" -k -s'
            os.system(test)

        def SPLF(self):  # System Preheat Log Feedback
            os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=STMD%2032&u=0" -k -s')
            os.system('clear')
            print(f'System Preheat Log Feedback Enabled')
            time.sleep(2)

        def SRCA(self, state):  # System Raise Chaff Assembly @
            if ST_Link == 1:
                x = str(f'BCP 0 RCA {str(state)}\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=RCA%20'
                          + str(state) + '&u=0" -k -s')
            time.sleep(2)
            os.system('clear')
            print(str(state))
            if state == 1:
                print('Chaff Closed')
            else:
                print('Chaff Open')

        def SSTRS(self):  # System ST ReSet @
            if ST_Link == 1:
                serial_port.write(b'MISC 0 RST\r')
            else:
                self.svn = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MISC&cmd=RST&u=0" -k -s -s')
            time.sleep(4)
            os.system('clear')
            print('ST Reset Sent')

        def SBDS(self):  # System Belly Drop State @
            try:
                if ST_Link == 1:
                    serial_port.write(b'BCP 0 GBDS\r')
                    response = serial_port.readline()
                    response = response.decode('utf-8')
                    response = response.replace('\r', '')
                    self.state = str(response[2:])
                else:
                    self.state = os.popen(
                        f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GBDS&u=0" -k -s').read()
                    self.state = self.state[42:-3]
                self.state = int(self.state)
            except ValueError:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GBDS&u=0" -k -s').read()
                self.state = self.state[42:-3]
                self.state = int(self.state)
            if self.state == 1:
                self.state = int(2)
                os.system('clear')
                print('Invalid Both Sensors Not Present')
            elif self.state == 2:
                self.state = int(0)
                os.system('clear')
                print('Belly Drop Closed "Sensor" ')
            elif self.state == 0:
                self.state = int(1)
                os.system('clear')
                print('Belly Drop Open "Sensor" ')
            elif self.state == 3:
                self.state = int(2)
                os.system('clear')
                print('Invalid Both Sensors Are Present')
            print(self.state)
            return self.state

        def SGCT(self):  # System Get Contactor State @
            if ST_Link == 1:
                serial_port.write(b'HTR 0 GCT\r')
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                self.state = str(response[2:])

            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=GCT&u=0" -k -s').read()
                self.state = str(self.state)
                self.state = self.state[42:-3]
            self.state = int(self.state)
            if self.state == 0:
                print(f'Contactor Not Engaged State {str(self.state)}')
            else:
                print(f'Contactor Engaged State {str(self.state)}')
            return self.state

        def SSCT(self, state):  # System Set ConTactor @
            if ST_Link == 1:
                x = str(f'HTR 0 SCT {str(state)}\r')
                serial_port.write(bytes(x, 'utf-8'))
            else:
                os.system(f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=SCT%20'
                          + str(state) + '&u=0" -k -s')
            time.sleep(2)
            os.system('clear')
            print(str(state))
            if state == 1:
                print(f'Contactor Engaged')
            else:
                print(f'Contactor Not Engaged')

        def SGCB(self):  # System Get Cooler Blower @
            if ST_Link == 1:
                x = str(f'BCP 0 GCBR\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                self.state = response[2:]

            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GCBR&u=0" -k -s').read()
                os.system('clear')
                self.state = str(self.state)
                self.state = self.state[42:-3]
                self.state = int(self.state)
            print(f'Exhaust RPM {str(self.state)}')
            return self.state

        if ST_Link == 1:
            def SGAC(self):  # System Get Alarm Conditions 1 @
                mask = int('1', 2)
                er_tb = {0: '[Inlet TC       ]',
                         1: '[Bean Front TC  ]',
                         2: '[ByPass Exit TC ]',
                         3: '[Heater Out TC  ]',
                         4: '[Blower TC      ]',
                         5: '[CAT TC         ]',
                         6: '[Drum Bottom TC ]',
                         7: '[N/A TC         ]',
                         8: '[N/A TC         ]',
                         9: '[N/A TC         ]',
                         10: '[N/A TC         ]',
                         11: '[Cooling Tray TC]',
                         12: '[Bucket         ]',
                         13: '[BucketFull     ]',
                         14: '[watlowTC_A     ]',
                         15: '[watlowTC_B     ]',
                         16: '[watlowSafe_A   ]',
                         17: '[watlowSafe_B   ]',
                         18: '[BoardRev       ]',
                         19: '[DigitalOutput  ]',
                         20: '[ModBusComm     ]',
                         21: '[BeanLoad       ]',
                         22: '[BeanDrop       ]',
                         23: '[BeanExit       ]',
                         24: '[DrumAgitatorVFD]',
                         25: '[MainBlowerVFD  ]',
                         26: '[Bypass         ]',
                         27: '[BeanCooling    ]',
                         28: '[BypassLevel2   ]',
                         29: '[ExhaustBlower  ]'
                         }
                er_st = {}
                dec_tb = {}

                x = str(f'SYS 0 GAC 0\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')[2:-2]
                self.state = str(self.state)
                self.stateb = self.state
                self.statec = self.state
                self.state = int(self.state)
                os.system('clear')
                print(f'Alarm Conditions Page 1 Machine: {str(mname)}: {str(self.state)}')
                print('')
                print('[    Alarm      ] [   P/F  ]   Decimal  ')
                print('________________________________________')

                y = self.state
                y = str(y)
                if y.isnumeric():
                    for x in er_tb:
                        mask = mask << 1
                        dec_tb[x] = mask
                        byte1 = int(mask)
                        map = byte1 & self.state
                        if map == 0:
                            er_st[x] = ('[  PASS  ]')
                        elif map >= 1:
                            er_st[x] = ('[* FAIL *]')
                    for x in er_tb:
                        print(f'{str(er_tb[x])} {str(er_st[x])}   {str(dec_tb[x])}')
                    print('')
                    return self.state
                else:
                    self.state = int(99999)
                    return self.state

            def SGAC2(self):  # System Get Alarm Conditions 2 @
                mask = int('1', 2)
                er_tb = {0: '[BeansInDrumBeanExit      ]',
                         1: '[BeansInDrumExhaustBlower ]',
                         2: '[InterlockBlower          ]',
                         3: '[InterLockMainHeater      ]',
                         4: '[InterLockAuxHeater       ]',
                         5: '[InterLockDrum            ]',
                         6: '[BypassStuck              ]',
                         7: '[DrumAgCritical           ]',
                         8: '[BeanFrontProbePreheat    ]',
                         9: '[RoastCurve               ]',
                         10: '[Hopper                   ]',
                         11: '[BeanConfirmation         ]',
                         12: '[UnusedEvent2             ]',
                         13: '[UnlimitedPreheat         ]',
                         14: '[PreheatTimeout           ]',
                         15: '[DrumEmpty                ]',
                         16: '[PreheatOverheat          ]',
                         17: '[ChaffCan                 ]',
                         18: '[WaterBottle              ]',
                         19: '[CoolerEmpty              ]',
                         20: '[BeanDrop Open            ]',
                         21: '[BeanDrop Closed          ]'
                         }

                '''''''''
                CoolBeansInDrum           = 32, // 0x0000,0001 << 32BeanFrontProbeProfile     = 33, // 0x0000,0002 << 32
                InterlockBlower           = 34, // 0x0000,0004 << 32
                InterlockMainHeater       = 35, // 0x0000,0008 << 32
                InterlockAuxHeater        = 36, // 0x0000,0010 << 32
                InterlockDrum             = 37, // 0x0000,0020 << 32
                BypassStuck               = 38, // 0x0000,0040 << 32
                DrumAgCritical            = 39, // 0x0000,0080 << 32
                BeanFrontProbePreheat     = 40, // 0x0000,0100 << 32
                RoastCurve                = 41, // 0x0000,0200 << 32
                Hopper                    = 42, // 0x0000,0400 << 32
                BeanConfirmation          = 43, // 0x0000,0800 << 32
                UnusedEvent2              = 44, // 0x0000,1000 << 32
                UnlimitedPreheat          = 45, // 0x0000,2000 << 32
                PreheatTimeout            = 46, // 0x0000,4000 << 32
                PreheatOverheat           = 47, // 0x0000,8000 << 32
                DrumEmpty                 = 48, // 0x0001,0000 << 32
                ChaffCan                  = 49, // 0x0002,0000 << 32
                WaterBottle               = 50, // 0x0004,0000 << 32
                CoolerEmpty               = 51, // 0x0008,0000 << 32
                BeanDropOpen              = 52, // 0x0010,0000 << 32
                BeanDropClosed            = 53, // 0x0020,0000 << 32

                '''''''''
                er_st = {}
                dec_tb = {}

                x = str(f'SYS 0 GAC 0\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.split(' ')
                self.state = self.state[2]
                self.state = str(self.state)
                self.stateb = self.state
                self.statec = self.state
                self.state = int(self.state)

                os.system('clear')
                print(f'Alarm Conditions Page 2 Machine: {str(mname)}: {str(self.state)}')
                print('')
                print('[    Alarm      ] [   P/F  ]   Decimal  ')
                print('________________________________________')

                for x in er_tb:
                    byte1 = int(mask)
                    dec_tb[x] = mask
                    map = byte1 & self.state
                    if map == 0:
                        er_st[x] = ('[  PASS  ]')
                    elif map >= 1:
                        er_st[x] = ('[* FAIL *]')
                    mask = mask << 1

                for x in er_tb:
                    if x == 0:
                        pass
                    else:
                        print(f'{str(er_tb[x])} {str(er_st[x])} {str(dec_tb[x])}')
                print('')
                return self.state
        else:
            def SGAC(self):  # System Get Alarm Conditions 1 @
                mask = int('1', 2)
                er_tb = {0: '[Inlet TC       ]',
                         1: '[Bean Front TC  ]',
                         2: '[ByPass Exit TC ]',
                         3: '[Heater Out TC  ]',
                         4: '[Blower TC      ]',
                         5: '[CAT TC         ]',
                         6: '[Drum Bottom TC ]',
                         7: '[N/A TC         ]',
                         8: '[N/A TC         ]',
                         9: '[N/A TC         ]',
                         10: '[N/A TC         ]',
                         11: '[Cooling Tray TC]',
                         12: '[Bucket         ]',
                         13: '[BucketFull     ]',
                         14: '[watlowTC_A     ]',
                         15: '[watlowTC_B     ]',
                         16: '[watlowSafe_A   ]',
                         17: '[watlowSafe_B   ]',
                         18: '[BoardRev       ]',
                         19: '[DigitalOutput  ]',
                         20: '[ModBusComm     ]',
                         21: '[BeanLoad       ]',
                         22: '[BeanDrop       ]',
                         23: '[BeanExit       ]',
                         24: '[DrumAgitatorVFD]',
                         25: '[MainBlowerVFD  ]',
                         26: '[Bypass         ]',
                         27: '[BeanCooling    ]',
                         28: '[BypassLevel2   ]',
                         29: '[ExhaustBlower  ]'
                         }
                er_st = {}
                dec_tb = {}
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SYS&cmd=GAC%200&u=0" -k -s').read()
                self.state = str(self.state)
                self.stateb = self.state
                self.statec = self.state

                try:
                    self.state = self.state[42:-12]  # For > FW 5.1.7RC
                    self.state = int(self.state)
                    os.system('clear')
                    print(f'Alarm Conditions Page 1 Machine: {str(mname)}: {str(self.state)}')
                    print('')
                    print('[    Alarm      ] [   P/F  ]   Decimal  ')
                    print('________________________________________')
                except ValueError:
                    p0 = self.stateb.split('p')
                    try:
                        self.stateb = p0[1]
                        self.state = self.stateb[4:-3]
                        self.state = int(self.state)
                        os.system('clear')
                        print(f'Alarm Conditions Page 1 Machine: {str(mname)}: {str(self.state)}')
                        print('')
                        print('[    Alarm      ] [   P/F  ]   Decimal  ')
                        print('________________________________________')

                    except IndexError:
                        os.system('clear')
                        self.state = str('FW Build NOT SUPPORTED')
                y = self.state
                y = str(y)
                if y.isnumeric():

                    for x in er_tb:
                        mask = mask << 1
                        dec_tb[x] = mask
                        byte1 = int(mask)
                        map = byte1 & self.state
                        if map == 0:
                            er_st[x] = ('[  PASS  ]')
                        elif map >= 1:
                            er_st[x] = ('[* FAIL *]')
                    for x in er_tb:
                        print(f'{str(er_tb[x])} {str(er_st[x])}   {str(dec_tb[x])}')
                    print('')
                    return self.state
                else:
                    self.state = int(99999)
                    return self.state

            def SGAC2(self):  # System Get Alarm Conditions 2 @
                mask = int('1', 2)
                er_tb = {0: '[BeansInDrumBeanExit      ]',
                         1: '[BeansInDrumExhaustBlower ]',
                         2: '[InterlockBlower          ]',
                         3: '[InterLockMainHeater      ]',
                         4: '[InterLockAuxHeater       ]',
                         5: '[InterLockDrum            ]',
                         6: '[BypassStuck              ]',
                         7: '[DrumAgCritical           ]',
                         8: '[BeanFrontProbePreheat    ]',
                         9: '[RoastCurve               ]',
                         10: '[Hopper                   ]',
                         11: '[BeanConfirmation         ]',
                         12: '[UnusedEvent2             ]',
                         13: '[UnlimitedPreheat         ]',
                         14: '[PreheatTimeout           ]',
                         15: '[DrumEmpty                ]',
                         16: '[PreheatOverheat          ]',
                         17: '[ChaffCan                 ]',
                         18: '[WaterBottle              ]',
                         19: '[CoolerEmpty              ]',
                         20: '[BeanDrop Open            ]',
                         21: '[BeanDrop Closed          ]'
                         }

                '''''''''
                CoolBeansInDrum           = 32, // 0x0000,0001 << 32BeanFrontProbeProfile     = 33, // 0x0000,0002 << 32
                InterlockBlower           = 34, // 0x0000,0004 << 32
                InterlockMainHeater       = 35, // 0x0000,0008 << 32
                InterlockAuxHeater        = 36, // 0x0000,0010 << 32
                InterlockDrum             = 37, // 0x0000,0020 << 32
                BypassStuck               = 38, // 0x0000,0040 << 32
                DrumAgCritical            = 39, // 0x0000,0080 << 32
                BeanFrontProbePreheat     = 40, // 0x0000,0100 << 32
                RoastCurve                = 41, // 0x0000,0200 << 32
                Hopper                    = 42, // 0x0000,0400 << 32
                BeanConfirmation          = 43, // 0x0000,0800 << 32
                UnusedEvent2              = 44, // 0x0000,1000 << 32
                UnlimitedPreheat          = 45, // 0x0000,2000 << 32
                PreheatTimeout            = 46, // 0x0000,4000 << 32
                PreheatOverheat           = 47, // 0x0000,8000 << 32
                DrumEmpty                 = 48, // 0x0001,0000 << 32
                ChaffCan                  = 49, // 0x0002,0000 << 32
                WaterBottle               = 50, // 0x0004,0000 << 32
                CoolerEmpty               = 51, // 0x0008,0000 << 32
                BeanDropOpen              = 52, // 0x0010,0000 << 32
                BeanDropClosed            = 53, // 0x0020,0000 << 32

                '''''''''
                er_st = {}
                dec_tb = {}
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=SYS&cmd=GAC%200&u=0" -k -s').read()
                self.state = str(self.state)
                p1 = self.state.split('p1')
                try:
                    self.state = p1[1]
                    self.state = self.state[3:-3]
                    self.state = int(self.state)
                    pst = 0
                except IndexError:
                    self.state = str('FW Build NOT SUPPORTED')
                    pst = 1

                os.system('clear')
                print(f'Alarm Conditions Page 2 Machine: {str(mname)}: {str(self.state)}')
                print('')
                print('[    Alarm      ] [   P/F  ]   Decimal  ')
                print('________________________________________')

                if pst == 1:
                    pass
                else:
                    for x in er_tb:
                        byte1 = int(mask)
                        dec_tb[x] = mask
                        map = byte1 & self.state
                        if map == 0:
                            er_st[x] = ('[  PASS  ]')
                        elif map >= 1:
                            er_st[x] = ('[* FAIL *]')
                        mask = mask << 1

                    for x in er_tb:
                        if x == 0:
                            pass
                        else:
                            print(f'{str(er_tb[x])} {str(er_st[x])} {str(dec_tb[x])}')
                    print('')
                return self.state

        def SSHBS(self, state):  # System Set Hopper Bean Status.
            if ST_Link == 1:
                x = str(f'BCP 0 SHBS {str(state)}\r')
                serial_port.write(bytes(x, 'utf-8'))
                # response = serial_port.readline()
                # print(f"HERE {response.decode('utf-8')}")

            else:
                os.system(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SHBS%20{str(state)}&u=0" -k -s -s')
            os.system('clear')
            print(f'Hopper Full Status set to : {str(state)}')

        def SGHBS(self):  # System Get Hopper Bean Status
            if ST_Link == 1:
                x = str(f'BCP 0 GHBS\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')[2:]
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GHBS&u=0" -k -s').read()
                os.system('clear')
                self.state = str(self.state)
                self.state = self.state[42:-3]
                self.state = int(self.state)
            print(f'Hopper Full Status {str(self.state)}')
            return self.state

        def SPF(self):  # System SPF Data
            if ST_Link == 1:
                x = str(f'HTR 0 GTMP\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')

            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=GTMP&u=1" -k -s').read()
                os.system('clear')
                self.state = str(self.state)
                self.state = self.state[42:-3]
            self.state = float(self.state)
            self.state = (((float(self.state) * 9) / 5) + 32)
            print(f'SPF Data {str(self.state)}')
            return self.state

        def SAIRPWM(self):  # System SPF Data
            if ST_Link == 1:
                x = str(f'HTR 3 GHDC\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=GHDC&u=3" -k -s').read()
                os.system('clear')
                self.state = str(self.state)
                self.state = self.state[42:-3]
            self.state = int(self.state)
            print(f'HTR PWM {self.state}')
            return self.state

        def SGAUXPWM(self):  # System SPF Data
            if ST_Link == 1:
                x = str(f'HTR 4 GHDC\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')
            else:
                self.state = os.popen(
                    f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=GHDC&u=4" -k -s').read()
                os.system('clear')
                self.state = str(self.state)
                self.state = self.state[42:-3]
            self.state = int(self.state)
            print(f'Aux PWM {self.state}')
            return self.state

        def SBOI(self):  # System Blower I(Current) @
            if ST_Link == 1:
                x = str(f'MOT 0 GMI\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                response = response.replace('\r', '')
                response = response.split(' ')
                self.v = response[2]
                if len(self.v) == 2:
                    a = str(self.v[:1])
                    b = str(self.v[-1])
                    self.v = str(a + '.' + b)
                else:
                    self.v = str('0.' + self.v)
            else:
                try:
                    self.v = os.popen(
                        f'curl -k -s -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MOT&cmd=GMI&u=0"').read()
                    os.system('clear')
                    self.z, self.x = self.v.split('p1":"')
                    self.t, self.u = self.x.split('","p2":"')
                    self.v = self.t
                    if len(self.v) == 2:
                        a = str(self.v[:1])
                        b = str(self.v[-1])
                        self.v = str(a + '.' + b)
                    else:
                        self.v = str('0.' + self.v)
                except ValueError:
                    if elog == 1:
                        logger.exception('Error ' + self.v)
                    self.v = ('0')
            print('Blower Current ' + self.v)
            return self.v

        def SBOR(self):  # System Blower RPM (in Hz) @
            try:
                self.v = os.popen(
                    f'curl -k -s -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=MOT&cmd=GMI&u=0"').read()
                self.x, self.z = self.v.split('p0":"')
                self.v = self.z[:-3]
                a = str(self.v[:2])
                b = str(self.v[-1])
                self.v = str(a + '.' + b)
            except ValueError:
                if elog == 1:
                    logger.exception('Retry ' + self.v)
                else:
                    pass
                self.v = ('0')
            os.system('clear')
            print('Blower RPM (in Hz) ', self.v)
            return self.v

        def MAXHTR(self, htr, pwm):  # MAX HeaTeR

            if htr == 1:
                htr = 3
            elif htr == 2:
                htr = 4

            if ST_Link == 1:
                x = str(f'HTR {str(htr)} GHDC {str(pwm)}\r')
                serial_port.write(bytes(x, 'utf-8'))
                response = serial_port.readline()
                response = response.decode('utf-8')
                self.state = response.replace('\r', '')
            else:
                os.system(
                    f'curl -k -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=SHMP%20{str(pwm)}&u={str(htr)}"')

        def SSMAXHTR(self):  # System Set MAX HeaTeR
            set = int(0)

            while set != 1:
                os.system('clear')
                print('Select Heater')
                print('')
                print(f'Main Heater = 1')
                print(f'Aux  Heater = 2')
                print('')
                htr = input(f'Enter Selection: ')
                htr = int(htr)
                htr_l = str('')

                if htr == 1:
                    htr = 3
                    htr_l = str('Main')
                    print('Main heater selected')
                    set += 1
                elif htr == 2:
                    htr = 4
                    htr_l = str('Aux')
                    print('Aux heater selected')
                    set += 1
                else:
                    input(f'Entry "{str(htr)}" is invalid.  Press "Enter" to continue: ')

            set = 0

            while set != 1:
                os.system('clear')
                print('Set Max PWM')
                print('')
                pwm = input(f'Set max PWM as a percentage in whole number: ')
                pwm = int(pwm)
                if pwm < 101:
                    print(f'Max PWM for {str(htr_l)} is set to {str(pwm)}%')
                    set += 1
                    time.sleep(2)
                else:
                    input(f'Entry "{str(pwm)}" is invalid.  Press "Enter" to continue: ')

            os.system(
                f'curl -k -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=SHMP%20{str(pwm)}&u={str(htr)}"')

            os.system('clear')
            input(f'Max PWM for {str(htr_l)} heater set to {str(pwm)}%.  Press Enter to continue: ')

        def SGMAXHTR(self, htr):  # System Get MAX HeaTeR
            if htr == 1:
                htr = 3
            elif htr == 2:
                htr = 4
            set = int(0)

            self.state = os.popen(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=HTR&cmd=GHMP&u={str(htr)}" -k -s').read()
            os.system('clear')
            self.state = self.state[42:-3]
            self.state = int(self.state)
            print(f'Heater Max PWM @ {str(self.state)}%')
            return (self.state)

        def SSPOINT(self):
            os.system('clear')
            print('Inlet Set Point')
            print('')
            low = input(f'Enter lower inlet set point (in degrees F): ')
            time = input(f'Enter duration time (in seconds): ')
            rise = input('Enter rise inlet set point (in degrees F): ')
            x = input('Maintain difference between inlet set point and profile? Y/n: ')
            x = x.upper()
            if x == ('Y'):
                x = int(2)
            else:
                x = int(1)
            print('')
            os.system(
                f'curl -k -s "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SRIA%20{str(x)}'
                f'%20{str(low)}%20{str(time)}%20{str(rise)}%200%200&u=0"'
            )

            bw.SSPOINT_Q()
            print('')
            print('Set points have been updated.')

        def SSPOINT_Q(self):
            self.state = os.popen(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=GRIA&u=0" -k -s').read()
            x = self.state.split('p')
            os.system('clear')
            print('Inlet Set Point value query')
            print('')
            print(f'Low Set Point  "{str((x[2])[4:-3])}F"')
            print(f'Duration       "{str((x[3])[4:-3])}s"')
            print(f'Rise Set Point "{str((x[4])[4:-3])}F"')
            y = (x[1])[4:-3]
            y = int(y)
            if y == 1:
                print('Follow Curve:  " N "')
            elif y == 2:
                print('Follow Curve:  " Y "')

        def SSPOINT_D(self):
            os.system(
                f'curl "https://{str(ip_address)}:{str(port)}/roaster/sensor?m=BCP&cmd=SRIA%200%200%200%200%200%200&u=0" -k -s')
            os.system('clear')
            bw.SSPOINT_Q()
            print('')
            print('Inlet Set Point set to default.')

bw = BW()
