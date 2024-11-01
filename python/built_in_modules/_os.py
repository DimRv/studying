"""
import os
os.sep - отображает сепаратор текущей OS (разделение папок в пути)
os.listdir() - список, содержимое директории
os.makedirs() - создание папок
os.unlink(path) - удаление файла по указанному пути
os.rmdir(path) - удаление папки по указанному пути
os.walk(path) - обход древа каталогов (имя папки, список папок, список файлов)

os.path.join(*dir_names:str) - создает путь в зависимости от OS
os.path.abspath(path) - строка абсолютного пути аргумента
os.path.isabs() - True если аргумент - абсолютный путь
os.path.relpath(end, start) - возвращает относительный путь от start до end
os.path.basename(path) - отcекает папки в имени path
os.path.dirname(path) - отсекает имя файла, оставляя путь
os.path.split(path) - кортеж из пути и имени
os.path.exists(path) - проверка наличия файла или папки
os.path.isfile(path) - является ли файлом path
os.path.isdir(path) - является ли каталогом path и если существует
os.path.getsize(path) - размер файла
"""

if __name__ == "__main__":
    import os

    print([item for item in dir(os) if not item.startswith("_")])
    print(os.sep, os.path.sep)
    print(os.getcwd())
    print(os.listdir("C:\\"))
    print(os.path.abspath(".."))
    print(os.path.relpath(r'C:\Games', os.getcwd()))
    print(os.path.basename(r"C:\Windows\System32\cmd.exe"))
    print(os.path.dirname(r"C:\Windows\System32\cmd.exe"))
    #os.makedirs(r'C:\bla\bla\bla')
    #os.mkdir(r'C:\blablabla')
    print(os.path.join("one", 'two', "three"))
    print(os.path.getsize(r"C:\Windows\System32\cmd.exe"))
    print(os.walk('dir_for_tests'))
    for folder, subfolder, filename in os.walk('dir_for_tests'):
        print(folder, subfolder, filename)
