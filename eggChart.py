import numpy as np
import matplotlib.patheffects as path_effects
from matplotlib import pyplot
from pandas import read_csv

BG_COLOR="#3b3b3b"
TOGGLE_SHADOWS = True
THICK_LINES=3

# CSV Column Names
ALTITUDE_COL_NAME = "Alt"
APOGEE_COL_NAME = "Apogee"
DROGUE_COL_NAME = "Drogue"
MAIN_COL_NAME = "Main"
NOSE_OVER_COL_NAME = "N-O"
TIME_COL_NAME = "T"
VELOCITY_COL_NAME = "Veloc"

# Chart Colors
ALTITUDE_COLOR = "darkorange"
APOGEE_COLOR = "mediumspringgreen"
DROGUE_COLOR = "yellow"
MAIN_COLOR = "palegreen"
NOSE_OVER_COLOR = "deepskyblue"
VELOCITY_COLOR = "crimson"


## Style Config  ##
pyplot.style.use('dark_background')
##

input_file = "dtl5.csv"
eggtimer_data = read_csv(input_file)

altitude = eggtimer_data[ALTITUDE_COL_NAME].tolist()
apogee = eggtimer_data[APOGEE_COL_NAME].tolist()
drogue = eggtimer_data[DROGUE_COL_NAME].tolist()
main = eggtimer_data[MAIN_COL_NAME].tolist()
nose_over = eggtimer_data[NOSE_OVER_COL_NAME].tolist()
time = eggtimer_data[TIME_COL_NAME].tolist()
velocity = eggtimer_data[VELOCITY_COL_NAME].tolist()


# Function to plot
figure, axis1 = pyplot.subplots(facecolor=BG_COLOR)
axis1.set_facecolor(BG_COLOR)
y_scale_max = np.max(altitude)
axis1.set_ylim(ymin=0, ymax=y_scale_max)
axis1.set_xlabel("time (sec)")
axis1.set_ylabel("altitude (ft)", color=ALTITUDE_COLOR)
axis1.grid(True, axis="y", ls="--", alpha=0.3, color=ALTITUDE_COLOR)


axis1.plot(time, altitude, color=ALTITUDE_COLOR, label="Altitude", alpha=0.75, linewidth=THICK_LINES,
           path_effects=[path_effects.SimpleLineShadow(linewidth=THICK_LINES), path_effects.Normal()])
axis1.vlines(time, 0, apogee, label="Apogee", color=APOGEE_COLOR, ls="dotted", zorder=50)
axis1.vlines(time, 0, nose_over, label="Nose Over", color=NOSE_OVER_COLOR, ls="dashed", zorder=40)
axis1.vlines(time, 0, drogue, label="Drogue", color=DROGUE_COLOR, ls="dashdot", zorder=30)
axis1.vlines(time, 0, main, label="Main", color=MAIN_COLOR, ls="dashdot", zorder=30)


axis2 = axis1.twinx()
v_scale_max = np.max(velocity)
axis2.set_ylim(ymin=0, ymax=v_scale_max)
axis2.set_ylabel("veloc (ft/sec)", color=VELOCITY_COLOR)
axis2.plot(time, velocity, color=VELOCITY_COLOR, label="Velocity", zorder=0, alpha=0.5, linewidth=THICK_LINES,
           path_effects=[path_effects.SimpleLineShadow(linewidth=THICK_LINES), path_effects.Normal()])


#build legend and display Plot
lines, labels = axis1.get_legend_handles_labels()
lines2, labels2 = axis2.get_legend_handles_labels()
axis2.legend(lines + lines2, labels + labels2, loc=0)
pyplot.show()