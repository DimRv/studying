from django.shortcuts import render
from django.http import Http404
from io import StringIO
import sys
import importlib
import inspect
# Create your views here.


class OutputInterceptor(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


def index(request):
    context = {}
    alphabetic_list = []
    functions = [i for i in __builtins__ if i[0] in [chr(j) for j in range(97, 123)]]
    functions.sort()
    for i in functions:
        if len(alphabetic_list) > 0:
            if alphabetic_list[0][0] == i[0]:
                alphabetic_list.append(i)
            else:
                context[alphabetic_list[0][0]] = alphabetic_list
                alphabetic_list = []
        else:
            alphabetic_list.append(i)
    return render(request, 'builtin_functions/index.html', {'f_list': context})


def detail(request, func_name):
    """Отображение детальной информации о функции"""
    # Путь к файлам с примерами и добавление в path
    path = 'C:\\studying\\python\\built_in_functions'
    sys.path.append(path)
    # Получение отсортированного списка всех встроенных функций в Python
    func_list = [i for i in __builtins__ if i[0] in [chr(j) for j in range(97, 123)]]
    func_list.sort()
    # Отсортировка запросов которые не относятся к функциям
    if func_name not in func_list:
        raise Http404

    with open(path + f"/_{func_name}.py", encoding='utf-8') as file:
        n = 0
        comment = False
        content = [[], [], []]
        string = ''
        for line in file:
            code_line = line.rstrip()
            if code_line == '"""':
                if comment is True:
                    comment = False
                    n += 1
                else:
                    comment = True
                continue
            if comment:
                if code_line == '':
                    if n == 0:
                        n += 1
                        continue
                    if n == 1:
                        content[n].append(string)
                        string = ''
                else:
                    string += code_line
        print(content)





    # Получение синтаксиса функции с помощью help
    """with OutputInterceptor() as output:
        help(func_name)"""
    # Получение данных из файла примера
    """with OutputInterceptor() as res:
        # Импорт модуля, чтобы записать результат выполнения в res
        mod = importlib.import_module(f'_{func_name}')
        print(inspect.getsource(mod).removeprefix(mod.__doc__))"""
    # Получение данных из загруженного модуля:
    """doc_split = mod.__doc__.split('\n\n')
    syntax = doc_split[0]
    description = doc_split[1:]
    with open(path + f"/_{func_name}.py", encoding='utf-8') as file:
        comment = False
        example = []
        for line in file.readlines():
            if line.find('COMMENTADD') >= 0:
                if comment:
                    comment = False
                    continue
                else:
                    comment = True
            if comment:
                continue
            else:
                if len(line.rstrip()) > 0:
                    example.append(line.rstrip())
                else:
                    example.append(" ")"""
    context = {'func_name': func_name,
               'func_list': func_list,
               #'syntax': syntax,
               #'description': description,
               #'title': f"Встроенная функция {func_name}",
               #'example': example,
               #'result': res,
               }
    return render(request, 'builtin_functions/detail.html', context)
