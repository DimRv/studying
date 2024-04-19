from django.shortcuts import render
from django.http import Http404
from io import StringIO
import sys
import importlib
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
    return render(request, 'builtin_functions/functions.html', {'f_list': context})


def detail(request, func_name):
    """Отображение детальной информации о функции"""
    # Путь к файлам с примерами и добавление в path
    path = 'C:\\studying\\python\\built_in_functions'
    sys.path.append(path)
    # Получение отсортированного списка всех встроенных функций в Python для навигации
    func_list = [i for i in __builtins__ if i[0] in [chr(j) for j in range(97, 123)]]
    func_list.sort()
    # Отсортировка запросов которые не относятся к функциям
    if func_name not in func_list:
        raise Http404

    with open(path + f"/_{func_name}.py", encoding='utf-8') as file:
        comment = False
        pos = 'syntax'
        description_string = ''
        file_content = {
            'syntax': [],
            'description': [],
            'example': [],
        }
        for line in file:
            code_str = line.rstrip()
            if code_str == '"""':
                if comment is False:
                    comment = True
                    continue
                else:
                    comment = False
                    file_content[pos].append(description_string)
                    pos = 'example'
                    continue
            if pos == 'syntax':
                if code_str == '':
                    pos = 'description'
                    continue
                else:
                    file_content[pos].append(code_str)
            if pos == 'description':
                if code_str == '':
                    file_content[pos].append(description_string)
                    description_string = ''
                    continue
                else:
                    description_string += code_str
                    if description_string[-1] != '.':
                        description_string += ' '
            if pos == 'example':
                if code_str == '':
                    file_content[pos].append('\n')
                else:
                    file_content[pos].append(code_str)

    # Получение результата выполнения
    with OutputInterceptor() as res:
        """Через exec плохо не работает с aiter:
        with open(path + f"\_{func_name}.py") as file:
            exec(file.read())"""
        i = importlib.import_module(f"_{func_name}")

    if not res:
        with OutputInterceptor() as res:
            importlib.reload(i)


    context = {'func_name': func_name,
               'title': f"Встроенная функция {func_name}",
               'func_list': func_list,
               'syntax': file_content['syntax'],
               'description': file_content['description'],
               'example': file_content['example'],
               'result': res,
               }
    return render(request, 'builtin_functions/detail.html', context)
