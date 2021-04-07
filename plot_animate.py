import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

runs = []
data_template = {"angle_min" : -np.pi, "angle_max" : np.pi, "angle_increment" : 0.02, "range_min" : 0.0, "range_max" : 12.0, "scan_time" : 0.15, "ranges" : [] }

fname = "cloud5_100.txt"
f = open(fname, "r")

data = data_template.copy()
r_max = 0

for line in f:
    for key in data:
        if key in line:
            if key == "ranges":
                #if "inf" in line: print("has inf range")
                data[key] = np.asarray(list(map(float,line.split("[")[-1].strip('[]\n').split(", "))))
                #for k in range(len(data)): print(k, " : ",data[key][k])
                #print(data[key].size)
                #print((data["angle_max"]-data["angle_min"])/data["angle_increment"])
            else:
                data[key] = float(line.split()[-1])
                print(key, " : ", data[key])
    if "---" in line:
        data["theta"] = np.arange(data["angle_min"], data["angle_max"]+data["angle_increment"], data["angle_increment"])
        runs.append(data.copy())
        r_max = max(r_max, np.nanmax(data["ranges"][data["ranges"] != np.inf]))
        data = data_template.copy()

f.close()

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)
lidar, = ax.plot([0], [r_max])

def animate(i):
    lidar.set_data(runs[i]["theta"], runs[i]["ranges"])
    return lidar, 
ani = FuncAnimation(fig, animate, frames=np.arange(0,len(runs)))

plt.show()
