"""
sys.path - пути где python осуществляет поиск переменных
sys.exc_info - информация о возникшем исключении (type, value, traceback)
sys.getdefaultencoding() - кодировка по умолчанию
sys.get
"""
import sys

print('before exit')
print(sys.path)
print(sys.exc_info())
print(sys.getdefaultencoding())
sys.exit()
print('after exit')