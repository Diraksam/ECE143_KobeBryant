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
