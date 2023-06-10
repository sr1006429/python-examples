# пример https://pypi.org/project/gTTS/
# есть еще один модуль - pyttsx3 для преобразования текста в речь 

from gtts import gTTS
tts = gTTS('Добрый день. Это сообщение озвучивается и записывается в файл hello.mp3', lang='ru')
tts.save('hello.mp3')