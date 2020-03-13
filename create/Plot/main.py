from _invert import *
from _scale_data import *
from create_scenario_map import * 
from create_shot_map import * 
from create_shot_maps import *
from draw_court import * 
from getrange import * 
from load_frames import * 
from plot_pie_charts import * 
from plot_radar import * 
from plot_season_graphs import * 
from plot_shot_timings import *

import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import pandas as pd
import seaborn as sns
import csv
import requests
from sys import *

import IPython
import matplotlib as mpl

import matplotlib
import matplotlib.gridspec as gridspec
from matplotlib.offsetbox import OffsetImage
from matplotlib.patches import Circle, Rectangle, Arc

def main():

    """
    This is the main function to call for analysis.
    
    """
    # Return needed Data Frames to analyze
    data_frame, seasons, col, labels, stats, kaggle = load_frames()

    # Create the maps now
    create_shot_maps(data_frame,seasons)
    create_scenario_map()
    
    # Create the Plots
    plot_season_graphs(stats)
    plot_pie_charts(kaggle)
    plot_shot_timings(kaggle)
    plot_radar(stats, col, labels)
