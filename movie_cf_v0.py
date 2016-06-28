import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from sklearn.metrics.pairwise import cosine_similarity

def get_sim_data(data):
    sim = DataFrame()
    for i in data.columns:
        sim[i] = DataFrame(cosine_similarity([data[guest_id]], [data[i]]))

    return sim.T.sort_values(by=0, ascending=False).head(11).T

def get_rec_data(top10_near):
    mult_rec = DataFrame()
    for i in top10_near.columns:
        if i != guest_id:
            mult_rec[i] = data[i] * (1 + top10_near[i][0])

    return mult_rec.T.sum().sort_values(ascending=False).to_frame('recommend rate').head(10)

guest_id = int(input('insert a user id : '))

data = pd.read_table('data/u.data', sep='\t', usecols=['user id', 'movie id', 'rating'])
data = data.pivot_table(index='movie id', columns='user id', values='rating', fill_value=0)
data = get_rec_data(get_sim_data(data))

item = pd.read_table('data/u.item', sep='|', usecols=['movie id', 'movie title', 'release date'])
item = item.set_index(['movie id'])
pd.concat([data, item], axis=1, join_axes=[data.index])

#data[data[guest_id] > 0][guest_id].to_frame('user id')