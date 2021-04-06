# -*- coding: utf-8 -*-
"""Recommendation System

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CiQ4QrSRIODiLjCcdICeEDibYUjkf-ln
"""

import pandas as pd
df = pd.read_csv('file3.csv')

index = {}
movies = {}
for i in range(len(df)):
    index[i] = df['title'][i]
    movies[df['title'][i].lower()] = i

from sklearn.feature_extraction.text import TfidfVectorizer
fea_tfidf = TfidfVectorizer(stop_words='english')
fea_matrix = fea_tfidf.fit_transform(df['fea'])

from sklearn.metrics.pairwise import linear_kernel
cosine_sim2 = linear_kernel(fea_matrix, fea_matrix)

def Similar_Movies(title, Cos_sim):
    if title in movies:
        similar = []
        for i in range(0,4803):
            if i!=movies[title]: similar.append((cosine_sim2[movies[title]][i],i))
        top10 = []
        for i,j in sorted(similar,reverse = True)[:10]:
            top10.append(index[j])
        return top10
    else:
        return 'Movie is not found in the database'

Similar_Movies('iron man',cosine_sim2)