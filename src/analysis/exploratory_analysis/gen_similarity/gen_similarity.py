from gensim.models.keyedvectors import KeyedVectors


def gen_similarity(model_name):
    model = KeyedVectors.load_word2vec_format(
        f'outputs/model_outputs/txt_models/{model_name}.txt', binary=False)
    word = input('What word would you like to query? ')
    results = model.most_similar(positive=[word])
    print(results)
