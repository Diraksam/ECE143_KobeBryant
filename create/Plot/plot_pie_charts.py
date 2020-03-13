def plot_pie_charts(kaggle):
    '''
    The function plots the pie charts of shot type distribution and quarter distribution.
    '''
    lakers_yellow = (253/255,186/255,33/255)
    lakers_purple = (85/255,32/255,132/255)
    # Number of shot attempts per quarter whole career
    first_q = (kaggle['period'] == 1).sum()
    second_q = (kaggle['period'] == 2).sum()
    third_q = (kaggle['period'] == 3).sum()
    fourth_q = (kaggle['period'] == 4).sum()
    total_q = first_q + second_q + third_q + fourth_q
    sizes_pie = [100*first_q,100*second_q,100*third_q,100*fourth_q] / total_q
    
    # Plot pie chart of shot selection by quarter
    labels = ['1st Qtr.','2nd Qtr','3rd Qtr','4th Qtr']
    sizes = sizes_pie
    fig3, ax3 = plt.subplots(figsize=(10,10))
    _, texts, autotexts =ax3.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, 
            colors = (lakers_yellow,lakers_purple,lakers_yellow,lakers_purple))
    for autotext in autotexts:
        autotext.set_fontsize(20)
    autotexts[1].set_color('white')
    autotexts[3].set_color('white')
    for text in texts:
        text.set_fontsize(20)
    ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Distribution of Shot Attempts per Quarter',fontsize=25)
    plt.show()

    # Shot distance throughout whole career
    labels = ['Close Range','Mid Range','Three Pointer']
    close_range = (kaggle['shot_zone_range'] == 'Less Than 8 ft.').sum()
    mid_range = (kaggle['shot_type'] == '2PT Field Goal').sum() - close_range
    three_pt = (kaggle['shot_type'] == '3PT Field Goal').sum()
    total_shot = close_range + mid_range + three_pt
    sizes_shots_pie = [100*close_range,100*mid_range,100*three_pt] / total_shot
    sizes = sizes_shots_pie
    
    # Plot pie chart of shot distance
    fig1, ax1 = plt.subplots(figsize=(10,10))
    patches, texts, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, 
            colors=(lakers_yellow,lakers_purple,(211/255,211/255,211/255)))
    plt.legend(patches, ['Close range: <8 ft.','Mid range: 8-16 ft.','Three Pointer: >24 ft.'], loc=(-0.2,0),fontsize=15)
    for autotext in autotexts:
        autotext.set_fontsize(20)
    autotexts[1].set_color('white')
    for text in texts:
        text.set_fontsize(20)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Distribution of Shot Distance',fontsize=25)
    plt.show()
    
    # Shot types
    shottype = np.array(list(set(kaggle['combined_shot_type'])))
    attempts = []
    for type in shottype:
        nshot = len(kaggle[kaggle['combined_shot_type']==type])
        attempts.append(nshot)

    # Plot pie chart of shot types
    import plotly.graph_objects as go
    grey='rgb(211,211,211)'
    yellow = 'rgb(253,186,33)'
    purple = 'rgb(85,32,132)'
    fig = go.Figure(data=[go.Pie(labels=shottype, values=attempts, pull=[0, 0, 0, 0.2,0,0])])
    fig.update_traces(textinfo='percent+label',marker=dict(colors=[purple,grey,yellow,purple,grey,yellow]))
    fig.update_layout(title={'text': 'Shot Types',
                             'y':0.85,
                             'x':0.52,
                             'xanchor': 'center',
                             'yanchor': 'top'})
    fig.show()
