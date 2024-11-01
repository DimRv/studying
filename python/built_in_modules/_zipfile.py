"""Чтение и создание зип-файлов
zf = ZipFile('name', [w]) - подключение файла
zf.namelist() - формирование списка фалов
zf.extractall() - извлечение zip в текущий рабочий каталог
zf.extract(file, path) - извлечение файла из каталога, возвращает путь
zf.write(file, compress_type=zipfile.ZIP_DEFLATED) - добавление данных в архив
zf.close() - закрытие zip-файла
zf.getinfo() - инфо о файле (ZipInfo)
zi.file_size - исходный размер файла
zi.compress_size - сжатый размер файла

"""
