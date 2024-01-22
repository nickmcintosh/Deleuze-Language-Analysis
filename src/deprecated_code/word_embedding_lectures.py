# DISAMBIGUATED SEVERAL FUNCTIONS IN THIS FILE


import json
from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import multiprocessing
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
import numpy as np


def training(model_name):
    with open('20_lectures_1_2.json', 'r') as f:
        texts = json.load(f)
    sentences = texts
    cores = multiprocessing.cpu_count()
    w2v_model = Word2Vec(min_count=2,
                         window=4,
                         vector_size=1000,
                         sample=6e-4,
                         alpha=.03,
                         min_alpha=0.0007,
                         negative=20,
                         workers=cores-1)

    w2v_model.build_vocab(texts)
    w2v_model.train(texts, total_examples=w2v_model.corpus_count, epochs=500)
    w2v_model.save(f'word_vectors/{model_name}.model')
    w2v_model.wv.save_word2vec_format(
        f'word_vectors/word2vec_{model_name}.txt')


# training('full_lecture_model_01')


def gen_similarity(word):
    model = KeyedVectors.load_word2vec_format(
        'word_vectors/word2vec_lecture_model_01.txt', binary=False)
    results = model.most_similar(positive=[word])
    print(results)


def tsv_converter(model):
    word_vectors = model.wv
    vocabulary = list(word_vectors.index_to_key)
    vectors = [word_vectors[word] for word in vocabulary]
    with open('word_vectors.tsv', 'w', encoding='utf-8') as tsv_file:
        for word, vector in zip(vocabulary, vectors):
            vector_str = '\t'.join(map(str, vector))
            tsv_file.write(f'{word}\t{vector_str}\n')


def pca_plotter():
    model = Word2Vec.load('word_vectors/full_lecture_model_01.model')
    word_vectors = model.wv
    vocabulary = list(word_vectors.index_to_key)
    vectors = [word_vectors[word] for word in vocabulary]
    pca = PCA(n_components=2)
    vectors_2d = pca.fit_transform(vectors)
    plt.figure(figsize=(12, 8))
    plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1])
    for i, word in enumerate(vocabulary):
        plt.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]))
    plt.show()


# pca_plotter()


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
        plt.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]))

    plt.show()


tsne_plotter()

# gen_similarity('Merleau')
