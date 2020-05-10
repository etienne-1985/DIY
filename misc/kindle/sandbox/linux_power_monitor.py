#cat /sys/class/power_supply/max77696-battery/uevent > /mnt/us/sandbox/power_stats.log

#!/usr/bin/pythonimport Tkinter as tk
# import tkMessageBox
# root = tk.Tk()
# root.withdraw()

# POWER_SUPPLY_NAME=max77696-battery
# POWER_SUPPLY_STATUS=Discharging
# POWER_SUPPLY_PRESENT=1
# POWER_SUPPLY_ONLINE=1
# POWER_SUPPLY_CYCLE_COUNT=10
# POWER_SUPPLY_VOLTAGE_NOW=4006
# POWER_SUPPLY_VOLTAGE_AVG=4006
# POWER_SUPPLY_CHARGE_FULL_DESIGN=790000
# POWER_SUPPLY_CHARGE_FULL=1408
# POWER_SUPPLY_CHARGE_NOW=1181
# POWER_SUPPLY_CAPACITY=99
# POWER_SUPPLY_TEMP=125
# POWER_SUPPLY_CURRENT_NOW=-291
# POWER_SUPPLY_CURRENT_AVG=-50

import datetime
import time 
from time import sleep
import logging
datefmt='%m/%d/%Y %I:%M:%S %p'
# logging.basicConfig(filename='power_stats.log', format='%(asctime)s %(message)s', level=logging.INFO, datefmt=datefmt)
logging.basicConfig(filename='power_stats.log', format='%(message)s', level=logging.INFO)
TIME_INTER=5  # time interval in seconds

def logPowerStats():
    charge=open("/sys/class/power_supply/max77696-battery/charge_now","r").readline().strip()
    capacity=open("/sys/class/power_supply/max77696-battery/capacity","r").readline().strip()
    current=open("/sys/class/power_supply/max77696-battery/current_now","r").readline().strip()
    current_avg=open("/sys/class/power_supply/max77696-battery/current_avg","r").readline().strip()
    voltage=open("/sys/class/power_supply/max77696-battery/voltage_now","r").readline().strip()
    voltage_avg=open("/sys/class/power_supply/max77696-battery/voltage_avg","r").readline().strip()
    timestamp = datetime.datetime.now().timestamp().__round__().__str__()
    logging.info('%s, %s, %s, %s, %s, %s, %s', timestamp, current_avg, current, voltage_avg, voltage, charge, capacity)
    print('%smA (%smA), %sv (%sv), %s (%s)' %(current_avg, current, voltage_avg, voltage, charge, capacity))
    # log = timestamp+": "+current_avg+"("+" "+voltage_avg+" "+charge+" "+capacity+"\n"
    # print(log)
    # return log
    
# start logging
fullstats=open("/sys/class/power_supply/max77696-battery/uevent","r").read()
logging.info('<<<<<< START DATA LOG >>>>>>')
logging.info(fullstats)
logging.info('timestamp, current_avg, current, voltage_avg, voltage, charge, capacity')
# periodically log
while True:
    try:
        logPowerStats()
        sleep(TIME_INTER)
    except:
        logging.warning('<<<<<< END DATA LOG >>>>>>')
        break


# while int(powerStat)>=30:
#     powerStat = powerFunction()
#     chargeStat = chargeState()
#     print "Battery Tracking"
#     if int(powerStat)<=30 and chargeStat == "Discharging":
#         tkMessageBox.showwarning("Alert!","Battery Low!\nCharging  Required!\nYour Battery Status:"+powerStat+"% ("+chargeStat+")")
#         break