import json
from gensim.models.word2vec import Word2Vec
import multiprocessing


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
    w2v_model.save(f'outputs/model_outputs/models/{model_name}.model')
    w2v_model.wv.save_word2vec_format(
        f'outputs/model_outputs/txt_models/word2vec_{model_name}.txt')
