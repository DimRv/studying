"""Протоколирование процесса выполнения программы

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='log.txt')
logging.debug() - вывод протоколируемой информации
logging.disable(logging.critical)

УРОВНИ протоколирования:
DEBUG       logging.debug()     - самй низкий. Подробные сведения
INFO        logging.info()      - обычные сообщения о нормальной работе
WARNING     logging.warning()   - индикация потенциально опасных ситуаций
ERROR       logging.error()     - запись от ошибке, программа не смогла выполнить действия
CRITICAL    logging.critical()  - фатальные ошибки, могут привести к полному прекращению программы
"""


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug("DEBUG message")
    logging.info("INFO message")
    logging.warning('WARNING message')
    logging.error('ERROR message')
    logging.critical('CRITICAL message')