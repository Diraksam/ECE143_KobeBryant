def plot_shot_timings(kaggle):
    '''
    The function plots the histogram of shot attempts vs the time of the shot
    '''
    lakers_yellow = (253/255,186/255,33/255)
    lakers_purple = (85/255,32/255,132/255)
    # Plot shot attempts as a function of time remaining during the game
    kaggle['seconds_from_period_start'] = 720 - 60*kaggle['minutes_remaining'] - kaggle['seconds_remaining']
    
    plt.rcParams['figure.figsize'] = (8,8)
    plt.rcParams['font.size'] = 8
    
    bin_size = 24
    
    for p in range(4):
        plt.figure();
        timeBins = np.arange(0,60*12+bin_size,bin_size)+0.01
        attemptsAsFunctionOfTime, b = np.histogram(kaggle[kaggle['period'] == p+1]['seconds_from_period_start'], bins=timeBins)     
            
        maxHeight = max(attemptsAsFunctionOfTime) + 30
        barWidth = 0.999*(timeBins[1]-timeBins[0])
        plt.subplot(4,1,p+1);
        plt.bar(timeBins[:-1],attemptsAsFunctionOfTime, align='edge', width=barWidth,color=lakers_purple)
        plt.vlines(x=[0,12*60],ymin=0,ymax=maxHeight,colors=lakers_yellow)
        plt.xlim((-20,740)); plt.ylim((0,maxHeight)); plt.ylabel('Shot attempts')
        plt.xlabel('Seconds Remaining Until End of Quarter ' + str(p+1))    



