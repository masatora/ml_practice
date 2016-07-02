import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from sklearn.metrics.pairwise import cosine_similarity

def get_recommend_data(sim):
    def wrap():
        top10_near = sim()
        drop_data  = drop_movie_data()
        mult_rec   = DataFrame()
        for i in top10_near.columns:
            if i != guest_id:
                mult_rec[i] = data[i] * (1 + top10_near[i][0])

        mult_rec = mult_rec.drop(drop_data)
        return mult_rec.T.sum().sort_values(ascending=False).to_frame('recommend rate').head(10)
    return wrap

@get_recommend_data
def get_cos_similarity_data():
    sim = DataFrame()
    for i in data.columns:
        sim[i] = DataFrame(cosine_similarity([data[guest_id]], [data[i]]))

    return sim.T.sort_values(by=0, ascending=False).head(11).T

def drop_movie_data():
    return data[data[guest_id] > 0][guest_id].to_frame('rating').T

guest_id = int(input('insert a user id : '))

data = pd.read_table('data/u.data', sep='\t', usecols=['user id', 'movie id', 'rating'])
data = data.pivot_table(index='movie id', columns='user id', values='rating', fill_value=0)
data = get_cos_similarity_data()

item = pd.read_table('data/u.item', sep='|', usecols=['movie id', 'movie title', 'release date'])
item = item.set_index(['movie id'])
print(pd.concat([data, item], axis=1, join_axes=[data.index]))