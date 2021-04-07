import numpy as np
import matplotlib.pyplot as plt

data = {"angle_min" : -np.pi, "angle_max" : np.pi, "angle_increment" : 0.02, "range_min" : 0.0, "range_max" : 12.0, "scan_time" : 0.15, "ranges" : [] }
fname = "cloud1.txt"
f = open(fname, "r")

for line in f:
    for key in data:
        if key in line:
            if key is "ranges":
                #if "inf" in line: print("has inf range")
                data[key] = np.asarray(list(map(float,line.split("[")[-1].strip('[]\n').split(", "))))
                #for k in range(len(data)): print(k, " : ",data[key][k])
                #print(data[key].size)
                #print((data["angle_max"]-data["angle_min"])/data["angle_increment"])
            else:
                data[key] = float(line.split()[-1])
                print(key, " : ", data[key])

f.close()
data["theta"] = np.arange(data["angle_min"], data["angle_max"]+data["angle_increment"], data["angle_increment"])

plt.polar(data["theta"], data["ranges"])
plt.show()
