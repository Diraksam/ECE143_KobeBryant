def plot_radar(stats, col, labels):
    '''Compute radar charts'''
    seasons = stats['Season']
    for i in range(len(stats)-1):
        if i==17:
            continue
        if i in [3,4,5,12,13]:
            seasoncolor = (253/255,186/255,33/255)
        else:
            seasoncolor = (85/255,32/255,132/255)
        #getting data
        plotstats=stats.loc[i,col]
        #getting ranges of axes
        ranges = getrange(stats,col)
        #plotting
        fig1 = plt.figure(figsize=(4,4))
        radar = ComplexRadar(fig1, labels, ranges, title ='Season {}'.format(seasons[i]),color=seasoncolor)
        radar.plot(plotstats)
        radar.fill(plotstats, alpha=0.2)
        plt.show()

