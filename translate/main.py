# pip install googletrans
# or if the problem is in the code
#       pip uninstall googletrans
#       pip install googletrans==4.0.0rc1 

from googletrans import Translator


translator = Translator()

def translator_translate(word):
    result = translator.translate(word, src = 'ru', dest = 'en')
    return result.text    

word = 'Здравствуйте. Это проверка перевода с русского языка на английский'
text = translator_translate(word)

print(word)
print('перевод :')
print(text)


