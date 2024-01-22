import matplotlib.pyplot as plt
import pickle


def load_tsne_plot(model_name):
    with open(f'outputs/model_outputs/pickled_tsne_results/{model_name}_figure.pkl', 'rb') as fig_file:
        fig = pickle.load(fig_file)
        # Display the figure
        plt.figure(fig.number)  # Make the loaded figure active
        plt.show()  # Display the active figure


load_tsne_plot('top_words_model_1.0')
