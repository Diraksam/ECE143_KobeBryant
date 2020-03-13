def getrange(stats,col):
    '''Get the range of data'''
    out = [(0,np.ceil(max(stats[name]))) for name in col]
    return out
