def create_scenario_map():
    """
    This function creates the neccessary Scenario Map for our Game 7 Finals Championship.
    
    Parameters:
    None
    
    Returns:
    None
    """
      
    # For scenario map
    kobePic = urllib.request.urlretrieve('https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/1610612747/2015/260x190/977.png',
                                    "977.png")
    kobe = plt.imread(kobePic[0])

    leBronPic = urllib.request.urlretrieve('https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/1610612747/2019/260x190/2544.png', "2544.png")
    leBron = plt.imread(leBronPic[0])

    michaelPic = urllib.request.urlretrieve('https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/893.png',
                           "893.png")
    michael = plt.imread(michaelPic[0])

    shaqPic = urllib.request.urlretrieve('https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/406.png',
                                     "406.png")
    shaq = plt.imread(shaqPic[0])

    anonymousPic = urllib.request.urlretrieve('http://s3.amazonaws.com/37assets/svn/765-default-avatar.png',
                                          "765-default-avatar.png")
    anonymous = plt.imread(anonymousPic[0])
        
    #Draw Court
    fig, ax = plt.subplots(figsize=(12, 11))
    ax = draw_court()

    # Kobe Image
    kobeImg = OffsetImage(kobe, zoom=0.4)
    kobeImg.set_offset((500,350))

    # Lebron Image
    leBronImg = OffsetImage(leBron, zoom=0.4)
    leBronImg.set_offset((100,500))

    # Michael Image
    michaelImg = OffsetImage(michael, zoom=0.4)
    michaelImg.set_offset((130,350))

    # Shaq Image
    shaqImg = OffsetImage(shaq, zoom=0.4)
    shaqImg.set_offset((400,500))

    # player image
    anonymousImg = OffsetImage(anonymous, zoom=0.15)
    anonymousImg.set_offset((325,220))

    ax.add_artist(kobeImg)
    ax.add_artist(leBronImg)
    ax.add_artist(michaelImg)
    ax.add_artist(shaqImg)
    ax.add_artist(anonymousImg)

    plt.xlim(-250,250)
    plt.ylim(422.5, -47.5)

    plt.show()
