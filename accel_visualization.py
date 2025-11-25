import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/kaggle/input/animal-behavior-prediction/abp_accel.csv")

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['acc_magnitude'] = np.sqrt(df['x']**2 + df['y']**2 + df['z']**2)

df = df.set_index('timestamp').resample('1s').mean().dropna()

print(df.describe())

# 시각화
plt.figure(figsize=(14,4))
plt.plot(df.index, df['acc_magnitude'], linewidth=0.8)
plt.title('Acceleration Magnitude over Time')
plt.xlabel('Time')
plt.ylabel('Acceleration Magnitude')
plt.show()
