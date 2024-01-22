### Currently Incomplete ###


import json
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import multiprocessing
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
import numpy as np


def word_counter():
  with open('20_lectures_1_2.json', 'r') as f:
    texts = json.load(f)
  

def tsne_plotter():
    model = Word2Vec.load('word_vectors/lecture_model_01.model')
    word_vectors = model.wv
    vocabulary = list(word_vectors.index_to_key)
    vectors = [word_vectors[word] for word in vocabulary]
    normalized_vectors = normalize(vectors, norm='l2')

    tsne = TSNE(n_components=2, perplexity=30, random_state=0)
    vectors_2d = tsne.fit_transform(normalized_vectors)
    plt.figure(figsize=(12, 8))
    plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1])
    for i, word in enumerate(vocabulary):
        if 
        plt.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]))

    plt.show()


tsne_plotter()
