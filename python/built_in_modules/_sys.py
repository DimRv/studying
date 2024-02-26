"""
sys.path - пути где python осуществляет поиск переменных
sys.exc_info - информация о возникшем исключении (type, value, traceback)

"""
import sys

print('before exit')
print(sys.path)
sys.exit()
print('after exit')