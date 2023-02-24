import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')


df['dx'] = df['Gyroscope x (rad/s)'] * (df['Time (s)'] - df['Time (s)'].shift(1))


df['angle_x'] = df['dx'].cumsum()


df['dy'] = df['Gyroscope y (rad/s)'] * (df['Time (s)'] - df['Time (s)'].shift(1))


df['angle_y'] = df['dy'].cumsum()


df['dz'] = df['Gyroscope z (rad/s)'] * (df['Time (s)'] - df['Time (s)'].shift(1))


df['angle_z'] = df['dz'].cumsum()



fig, ax = plt.subplots()
ax.plot(df['Time (s)'], df['angle_x'], label='x-axis')
ax.plot(df['Time (s)'], df['angle_y'], label='y-axis')
ax.plot(df['Time (s)'], df['angle_z'], label='z-axis')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Position (rad)')
ax.legend()
plt.show()
