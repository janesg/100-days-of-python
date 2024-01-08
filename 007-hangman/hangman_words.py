import random
from english_words import get_english_words_set

big_word_list: list[str] = list(get_english_words_set(['web2'], lower=True))
word_list = random.sample(big_word_list, 300)
