from gensim.models.keyedvectors import KeyedVectors


def gen_similarity(model_name):
    model = KeyedVectors.load_word2vec_format(
        f'outputs/model_outputs/txt_models/{model_name}.txt', binary=False)

    while True:
        word = input('What word would you like to query? ')
        results = model.most_similar(positive=[word])
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result}")
        another_query = input(
            "Would you like to query another word? (y/n): ").strip().lower()
        if another_query != 'y':
            break


gen_similarity('top_words_model_1.0')
