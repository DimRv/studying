"""
pip install gtts

Модуль позволяет воспроизвести текст в голосовом виде
Гугл переводчик в деле!
"""

from gtts import gTTS
import os


help(gTTS)

txt = "Гугл переводчик в деле!"
audio = gTTS(text=txt, lang='ru', slow=True)
#audio.stream()
audio.save('gtts_file.mp3')

os.system('gtts_file.mp3')
