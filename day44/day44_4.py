from    deckofcards import DeckOfCards
from    pathlib import Path
import  matplotlib.pyplot as plt
import  matplotlib.image as mpimg

deck = DeckOfCards()

path = Path('.').joinpath('cards')

figure, axes_list = plt.subplots(nrows=4, ncols=13)
deck.shuffle()
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)
figure.tight_layout()

plt.show()