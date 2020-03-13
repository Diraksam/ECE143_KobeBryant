# single shot map, might not need.
def create_shot_map(dataframe, title):
    """
    This function Creates a single Heat Map of shot locations from dataframe
    
    Parameters:
    dataframe: pd.DataFrame for shot map locations of x and y coordinates
    title: string that gives the heat map the current title.
    
    Returns:
    None
    
    """
    
    
    x = dataframe['loc_x']
    y = dataframe['loc_y']
    xmin = x.min()
    xmax = x.max()
    ymin = y.min()
    ymax = y.max()


    fig, ax = plt.subplots(figsize=(8, 6))

    # Set axis
    # Set legend

    hb = ax.hexbin(x, y, gridsize=30, bins='log', cmap='YlOrRd',mincnt = 1, edgecolor='grey')
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
    cb = fig.colorbar(hb, ax=ax)
    ax = draw_court(outer_lines = True)
    ax.set_title(title)


    plt.xlim(-250,250)
    plt.ylim(422.5, -47.5)
    plt.show()
