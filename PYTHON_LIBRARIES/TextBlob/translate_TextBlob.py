# - *- coding: utf- 8 - *-
from textblob import TextBlob
import textblob

word = TextBlob('hello')
t_word = word.translate(from_lang = 'en',to = 'te')#ex: hi,ta etc...
print(t_word)


