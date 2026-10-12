import colorsys
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from skimage.color import lab2rgb

root = Path(__file__).resolve().parents[1]
fig, ax = plt.subplots(figsize= (10,5))

ext_path = r"Geophysical_Interpretations\Faults\Volve_Official_Faults.dat"
clear_ext_path = ext_path.replace("\\", "/")

fault_path = (root / ext_path)

pattern = r"^(\d)([a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)?)_(.*)$"

# 2011 fault sticks number
N = 52
fault_colors = []
for i in range(52):
    h = (i * 0.61803398875)%1
    s= 0.5
    v= 0.75
    fault_colors.append(colorsys.hsv_to_rgb(h,s,v))

# OKLCH
L= 0.7
C= 0.2
hues = np.linspace(0, 360, N, endpoint = False )

oklab = np.zeros((N, 3))
oklab[:,0] = L
oklab[:,1] = C*np.cos(np.radians(hues))
oklab[:,2] = C*np.sin(np.radians(hues))

fault_colors = lab2rgb(oklab.reshape(1,N,3)).reshape(N,3)

with (open(fault_path, "r", encoding = "utf-8", errors = "Replace" ) as f):

    lines_dict = []

    for line_no, line in enumerate(f, start=1):
        line = line.strip()
        line_list = line.split()
        lines_dict.append({
            "x": line_list[0],
            "y": line_list[1],
            "twt":line_list[2],
            "fault_stick":line_list[-7]
        })
    df_faults = pd.DataFrame(lines_dict)
    df_faults[["x","y","twt"]] = df_faults[["x","y","twt"]].astype(float)

    df_extracted = df_faults["fault_stick"].str.extract(pattern)
    df_faults[["fault_number","fault_name","fault_year"]] = df_extracted

    for idx, fault_name in enumerate(df_faults[df_faults["fault_year"] == "2011"]["fault_name"].unique()):
        for fault_number in df_faults["fault_number"].unique():
            fault_filter = (df_faults["fault_year"] == "2011"
                            ) & (df_faults["fault_name"] == fault_name
                                 ) & (df_faults["fault_number"] == fault_number)

            df_fault = df_faults[fault_filter][["x", "y"]]

            if len(df_fault) >0 :
                mid = len(df_fault)//2

                ax.plot(df_fault["x"], df_fault["y"], color = fault_colors[idx], linewidth = 1, alpha =1)


                ax.annotate(
                    f"{fault_number}-{fault_name}",
                    xy = (df_fault["x"].iloc[mid], df_fault["y"].iloc[mid]),
                    xytext = (5,5),
                    textcoords = "offset points",
                    color = fault_colors[idx],
                    fontweight = "bold",
                    fontsize = 7,
                    bbox = dict(
                        facecolor = "white",
                        edgecolor = "none",
                        alpha = 0.5,
                        pad = 1.5

                    )
                )




ax.set_xlabel("X")
ax.set_ylabel("Y")

scale_x = 1e5
scale_y = 1e6

formatter_x = FuncFormatter(lambda x, pos: f"{x/scale_x:.2f}" )
formatter_y = FuncFormatter(lambda x, pos: f"{x/scale_y:.2f}" )

ax.xaxis.set_major_formatter(formatter_x)
ax.yaxis.set_major_formatter(formatter_y)

ax.set_xlabel(r"X ($\times10^5$)")
ax.set_ylabel(r"Y ($\times10^6$) ")

plt.show()