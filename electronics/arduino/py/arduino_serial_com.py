import serial
import time
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM3', 9600)
ser.flushInput()

ser_bytes = ser.readline()
print(ser_bytes)
ser.write("=".encode()) # Convert the decimal number to ASCII then send it to the Arduin
# ser.write("=".encode()) # Convert the decimal number to ASCII then send it to the Arduino
ser_bytes = ser.readline()
print(ser_bytes)

plot_window = 20
y_var = np.array(np.zeros([plot_window]))
t = np.arange(0.0, 2.0, 0.01)
y_var = 1 + np.sin(2 * np.pi * t)

plt.ion()
# fig, ax = plt.subplots()
# line, = ax.plot(y_var)

# ax.plot(t, y_var)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',title='toto')
# ax.grid()

while True:
    try:
        ser_bytes = ser.readline()
        log = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        
        try:
            amp = float(log[0:4])
            volt = float(log[6:10])
            watt = float(log[15:19])
            print(' %sA %sV => %sW' %(amp, volt, watt))
        except:
            continue
        y_var = np.append(y_var,watt)
        y_var = y_var[1:plot_window+1]
        # line.set_ydata(y_var)
        # ax.plot(y_var)

        # ax.relim()
        # ax.autoscale_view()
        # fig.canvas.draw()
        # fig.canvas.flush_events()
    except:
        print("Keyboard Interrupt")
        break