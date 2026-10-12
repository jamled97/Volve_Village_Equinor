import re
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.ticker import FuncFormatter

root = Path(__file__).resolve().parents[1]
reg_pattern = r"^\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+\.\d+,\d+\.\d+$"

hugin_horizons_files = ["Hugin_Fm_Base+ST10010ZC11_Near_190314_adj_2999_EasyDC+STAT+DEPTH.dat", "Hugin_Fm_Top+ST10010ZC11_Near_190314_adj2_2760_EasyDC+STAT+DEPTH.dat"]

# well picks

well_pick_dict = {
    "Hugin_Fm_Base+ST10010ZC11_Near_190314_adj_2999_EasyDC+STAT+DEPTH.dat":{
    "MD":4178.59,
    "TVD":3299.68,
    "TVDSS":3274.68,
    "Easting":436437.4,
    "Northing":6477478.2,
    "label": '15/9-19 BT2 Hugin Base Pick',
    "color": 'darkblue',
    "marker": 'x',
    "s": 100,
    "linewidths": 5,
    "alpha":1,
    "interpolation_color" : "darkblue",
    "interpolation_marker": 'x',
    "interpolation_s": 100,
    "interpolation_lw": 5,
    "interpolation_alpha": 1

},
    "Hugin_Fm_Top+ST10010ZC11_Near_190314_adj2_2760_EasyDC+STAT+DEPTH.dat":{
    "MD":4035.8,
    "TVD":3173.92,
    "TVDSS":3148.92,
    "Easting":436408.4,
    "Northing":6477539.1,
    "label": '15/9-19 BT2 Hugin Top Pick',
    "color": 'green',
    "marker": 'x',
    "s": 200,
    "linewidths": 5,
    "alpha": 1,
    "interpolation_color" : "red",
    "interpolation_marker": 'x',
    "interpolation_s": 100,
    "interpolation_lw": 5,
    "interpolation_alpha": 1
    }
 }

horizon_plot_dict = {
    "Hugin_Fm_Base+ST10010ZC11_Near_190314_adj_2999_EasyDC+STAT+DEPTH.dat" : {
        "cmap" : 'seismic',
        "label" : "Hugin Base",
        "marker": 'o',
        "alpha": 0.05,
        "depth_min" : 0,
        "depth_max" : 5000,
        "easting_min: " : 0,
        "easting_max: " : 0,
        "northing_min: " : 0,
        "northing_max: " :0
    },
    "Hugin_Fm_Top+ST10010ZC11_Near_190314_adj2_2760_EasyDC+STAT+DEPTH.dat" : {
        "cmap" : 'gist_earth',
        "label": "Hugin Top",
        "marker": 'o',
        "alpha": 0.08,
        "depth_min" : 0,
        "depth_max" : 5000,
        "easting_min: " : 0,
        "easting_max: " : 0,
        "northing_min: " : 0,
        "northing_max: " :0
    }
}

# 3D
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(projection="3d")

for horizon in hugin_horizons_files:

    dat_path = (root / "Geophysical_Interpretations" / "Horizons/Horizons_DEPTH/Official_Horizons" / horizon)

    with (open(dat_path, "r", encoding = "utf-8", errors = "Replace" ) as f):
        lines_dict = []
        for line_no, line in enumerate(f, start=1):
            line.strip()
            if re.match(reg_pattern, line):
                line_list = line.split(",")
                lines_dict.append({
                    "line": line_list[0],
                    "trace": line_list[1],
                    "x": line_list[2],
                    "y": line_list[3],
                    "z": line_list[4].rstrip('\n')
                })

    df_coordinates = pd.DataFrame(lines_dict)
    df_coordinates = df_coordinates.astype(float)

    horizon_xy = df_coordinates[['x','y']].values
    horizon_z = df_coordinates['z'].values

    horizon_plot_dict[horizon]["easting_min"] = df_coordinates['x'].min()
    horizon_plot_dict[horizon]["easting_max"] = df_coordinates['x'].max()

    horizon_plot_dict[horizon]["northing_min"] = df_coordinates['y'].min()
    horizon_plot_dict[horizon]["northing_max"] = df_coordinates['y'].max()

    horizon_plot_dict[horizon]["depth_min"] = df_coordinates['z'].min()
    horizon_plot_dict[horizon]["depth_max"] = df_coordinates['z'].max()

    norm = Normalize(vmin = horizon_plot_dict[horizon]["depth_min"],
                     vmax=  horizon_plot_dict[horizon]["depth_max"])

    sc= ax.plot_trisurf(df_coordinates['x'],
                        df_coordinates["y"],
                        df_coordinates["z"],
                        cmap = horizon_plot_dict[horizon]["cmap"],
                        alpha=horizon_plot_dict[horizon]["alpha"],
                        norm = norm,
                        linewidth = 0,
                        antialiased = True)


    # Well pick

    ax.scatter(well_pick_dict[horizon]["Easting"],well_pick_dict[horizon]["Northing"],well_pick_dict[horizon]["TVDSS"],
               color= well_pick_dict[horizon]["color"], marker= well_pick_dict[horizon]["marker"],
               s= well_pick_dict[horizon]["s"], linewidths= well_pick_dict[horizon]["linewidths"],
               label= well_pick_dict[horizon]["label"], alpha = well_pick_dict[horizon]["alpha"]
               )

    sm = ScalarMappable(
        norm = norm,
        cmap = horizon_plot_dict[horizon]["cmap"]
    )
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=f"{horizon_plot_dict[horizon]["label"]} Z Depth (TVDSS)", shrink= 0.5, pad = 0.08, aspect = 25)
    cbar.ax.invert_yaxis()

ax.set_xlabel("X")
ax.set_ylabel("Y")

#scientifc notation x,y axis
scale_x = 1e5
scale_y = 1e6

formatter_x = FuncFormatter(lambda x, pos: f"{x/scale_x:.2f}" )
formatter_y = FuncFormatter(lambda x, pos: f"{x/scale_y:.2f}" )

ax.xaxis.set_major_formatter(formatter_x)
ax.yaxis.set_major_formatter(formatter_y)

ax.set_xlabel(r"X ($\times10^5$)")
ax.set_ylabel(r"Y ($\times10^6$) ")

#horizon depth limits in TVDSS : Top = [2723.3371582, 3393.9101562] Base =[2741.1989746, 3486.7712402]
depth_min= min([horizon_plot_dict[horizon]["depth_min"] for horizon in hugin_horizons_files])
depth_max = max([horizon_plot_dict[horizon]["depth_max"] for horizon in hugin_horizons_files])

easting_min = min([horizon_plot_dict[horizon]["easting_min"] for horizon in hugin_horizons_files])
easting_max = max([horizon_plot_dict[horizon]["easting_max"] for horizon in hugin_horizons_files])

northing_min= min([horizon_plot_dict[horizon]["northing_min"] for horizon in hugin_horizons_files])
northing_max= max([horizon_plot_dict[horizon]["northing_max"] for horizon in hugin_horizons_files])

ax.invert_zaxis()
plt.show()