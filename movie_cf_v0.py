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

    return (mult_rec.T.sum().sort_values(ascending=False)).head(10)

guest_id = int(input('insert a user id : '))
data = pd.read_table('data/u.data', sep='\t', usecols=['user id', 'item id', 'rating'])
data = data.pivot_table(index='item id', columns='user id', values='rating', fill_value=0)
top10_near = get_sim_data(data)
print(get_rec_data(top10_near))