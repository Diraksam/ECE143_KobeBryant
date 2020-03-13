def plot_season_graphs(stats):
    '''
    The function plots FG%, Personal Foul and 3 Points Attempted per season.
    '''
    lakers_yellow = (253/255,186/255,33/255)
    lakers_purple = (85/255,32/255,132/255)
    # Plot FG% per season
    ax = plt.figure(figsize=(12, 6))
    plt.plot(stats['Season'].iloc[:-1],stats['FG%'].iloc[:-1],'o-',color = lakers_purple, markersize=10)
    plt.plot(stats['Season'].iloc[[3,4,5,12,13]],stats['FG%'].iloc[[3,4,5,12,13]],'o',color = lakers_yellow, markersize=15)
    plt.xticks(rotation=30)
    plt.legend(('Regular Season','Champion Season'),fontsize=14)
    plt.title('Field Goal% vs. Season',fontsize=20)
    plt.ylabel('Field Goal%')
    plt.xlabel('Season')
    plt.grid()
    
    # Plot Personal Foul per season
    ax = plt.figure(figsize=(12, 6))
    plt.plot(stats['Season'].iloc[:-1],stats['PF'].iloc[:-1],'-o',color = lakers_purple)
    plt.xticks(rotation=30)
    plt.title('Personal Foul vs. Season',fontsize=20)
    plt.ylabel('Personal Foul')
    plt.xlabel('Season')
    plt.grid()
    
    # Plot Three Points Attempted per season
    nba3pa = [16.8,12.7,13.2,13.7,13.7,14.7,14.7,14.9,15.8,16,16.9,18.1,18.1,18.1,18,18.4,20,21.5,22.4,24.1]
    plt.figure(figsize = (12,7))
    plt.xticks(rotation = 30)
    plt.title('3 Points Attempted per Game by Kobe Bryant and NBA Teams',fontsize = 20)
    plt.plot(stats['Season'].iloc[:-1],stats['3PA'].iloc[:-1],'-o',color=lakers_purple)
    plt.plot(stats['Season'].iloc[:-1],nba3pa,'-o',color=lakers_yellow)
    plt.legend(('Kobe Bryant','NBA Average'),loc='upper left',fontsize=16)
    plt.grid()
    plt.show()
