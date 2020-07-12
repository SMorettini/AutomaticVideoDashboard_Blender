## Script to resample data to the frame rate of your Blender Project

import pandas as pd

fps=24  ### PUT HERE THE FRAME RATE YOU WANT TO USE IN BLENDER
sample=int(1000/fps)

df=pd.read_csv("../acc_data.csv", delimiter=",")


time=pd.to_datetime(df['Time'], unit='s', errors='coerce')
df['Time']=time
df.set_index('Time')
new_df=df.set_index(df['Time']).resample(str(sample)+'ms').mean()

new_df.to_csv('acc_resampled')
