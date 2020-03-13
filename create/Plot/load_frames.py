# Read the statsr
def load_frames():
    """
    This function loads all the necessary frames for the upcoming data analysis.
    
    Parameters:
    None
    
    Returns:
    List: The list of required dataframes
    """
    data_frame = pd.read_csv('./create/CSV/data.csv')
    seasons = pd.read_csv('./create/CSV/nba-players-stats/Seasons_Stats.csv')
    col=np.array(['TRB', 'PTS', 'STL','BLK','AST'])
    labels = np.array(['                Rebound', 'Points', 'Steal','Block','Assist'])
    careerstats = pd.read_csv('./create/CSV/careerstats.csv')
    shotselection = pd.read_csv('./create/CSV/shotselection.csv')
    
    return [data_frame, seasons, col, labels,careerstats, shotselection ]
