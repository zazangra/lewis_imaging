from create_worlds import universe

n_ant_worlds=[]
ant_worlds=[]
def valuations():
    for i in universe:
        if (i.world['a']==0 or i.world['b']==0) and i.world['c']==1:
            ant_worlds.append(i)
        else:
            n_ant_worlds.append(i)
    return ant_worlds




    # insert the formula, e. g. if the formula is (a=0 \land b=0) \lor c=0 then write (i.world['a']==0 or i.world['b']==0) and i.world['c']==1


