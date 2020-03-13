def create_shot_maps(data_frame, seasons):
    """
    This function creates the entire shot map needed for the data analysis
    
    Parameters:
    data_frame: The Dataframe to analyze.
    seasons: The list of seasons to name each season in the heatmap
    
    Returns:
    None
    
    """
    
    # Grabs the first season
    kb_first_year_bool = data_frame['season'] =='1996-97'
    kb_first_year_df = data_frame[kb_first_year_bool]

    #Grabs the championship season'''
    # 1999-00 with Los Angeles Lakers : kb_1_c_df
    kb_1_c_bool = data_frame['season'] == '1999-00'
    kb_1_c_df = data_frame[kb_1_c_bool]

    # 2000-01 with Los Angeles Lakers : kb_2_c_df
    kb_2_c_bool = data_frame['season'] == '2000-01'
    kb_2_c_df = data_frame[kb_2_c_bool]

    # 2001-02 with Los Angeles Lakers : kb_3_c_df
    kb_3_c_bool = data_frame['season'] == '2001-02'
    kb_3_c_df = data_frame[kb_3_c_bool]

    # 2008-09 with Los Angeles Lakers : kb_4_c_df
    kb_4_c_bool = data_frame['season'] == '2008-09'
    kb_4_c_df = data_frame[kb_4_c_bool]

    # 2009-10 with Los Angeles Lakers : kb_5_c_df
    kb_5_c_bool = data_frame['season'] == '2009-10'
    kb_5_c_df = data_frame[kb_5_c_bool]

    # Grabs the last season
    # 2015-16 with Los Angeles Lakers : kb_15_c_df
    kb_15_c_bool = data_frame['season'] == '2015-16'
    kb_15_c_df = data_frame[kb_15_c_bool]

    #00-01, 05-06, 10-11, 15-16
    kb_5_bool = data_frame['season'] == '2005-06'
    kb_5_df = data_frame[kb_5_bool]

    kb_10_bool = data_frame['season'] == '2010-11'
    kb_10_df = data_frame[kb_10_bool]

    kb_15_bool = data_frame['season'] == '2015-16'
    kb_15_df = data_frame[kb_15_bool]
    
    # 1st, 5th, 10th, 15th, 20th seasons
    create_shot_map(kb_first_year_df, "Kobe Bryant - First Season 1996-97")
    create_shot_map(kb_2_c_df, "Kobe Bryant - 5th Season 2000-01")
    create_shot_map(kb_5_df, "Kobe Bryant - 10th Season 2005-06")
    create_shot_map(kb_10_df, "Kobe Bryant - 15th Season 2010-11")
    create_shot_map(kb_15_df, "Kobe Bryant - 20th Season 2015-16")
    create_shot_map(data_frame, "Kobe Bryant - All Seasons")
    #create_shot_map(kb_15_c_df, "Kobe Bryant Last Season 2015-16")    
    
    # Championship seasons
    create_shot_map(kb_1_c_df, "Kobe Bryant - First Championship 1999-00")
    create_shot_map(kb_2_c_df, "Kobe Bryant - Second Championship 2000-01")
    create_shot_map(kb_3_c_df, "Kobe Bryant - Third Championship ( Three Peat ) 2001-02")
    create_shot_map(kb_4_c_df, "Kobe Bryant - Fourth Championship 2008-09")
    create_shot_map(kb_5_c_df, "Kobe Bryant - Fifth Championship 2009-10")
