"""
sys.path - пути где python осуществляет поиск переменных
sys.exc_info - информация о возникшем исключении (type, value, traceback)
sys.getdefaultencoding() - кодировка по умолчанию
sys.argv - список переданных параметров .py - скрипт
sys.exit() - завершение работы
"""
import sys

print('before exit')
print(sys.path)
print(sys.exc_info())
print(sys.getdefaultencoding())
print(sys.argv)
sys.exit()
print('after exit')