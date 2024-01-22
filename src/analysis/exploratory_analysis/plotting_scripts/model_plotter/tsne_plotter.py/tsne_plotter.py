from gensim.models.word2vec import Word2Vec
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
import pickle


def tsne_plotter(model_name):
    # Load model and vectors
    model = Word2Vec.load(f'outputs/model_outputs/models/{model_name}.model')
    word_vectors = model.wv
    vocabulary = list(word_vectors.index_to_key)
    vectors = [word_vectors[word] for word in vocabulary]
    # Reduce complexity for 2d representation
    normalized_vectors = normalize(vectors, norm='l2')
    tsne = TSNE(n_components=2, perplexity=30, random_state=0)
    vectors_2d = tsne.fit_transform(normalized_vectors)
    # Create Plot
    plt.figure(figsize=(12, 8))
    plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1])
    for i, word in enumerate(vocabulary):
        plt.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]))

    # Save as PNG
    plt.savefig(
        f'outputs/data_outputs/plots/word_embedding_plots/png_files/{model_name}.png', dpi=300, bbox_inches='tight')

    # Pickle data for Matplotlib
    with open(f'outputs/model_outputs/pickled_tsne_results/{model_name}_figure.pkl', 'wb') as fig_file:
        pickle.dump(plt.gcf(), fig_file)

    plt.show()


tsne_plotter('top_words_model_1.0')
