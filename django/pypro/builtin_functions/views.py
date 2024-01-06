from django.shortcuts import render
from django.http import Http404
from io import StringIO
import sys
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
    func_list = [i for i in __builtins__ if i[0] in [chr(j) for j in range(97, 123)]]
    if func_name not in func_list:
        raise Http404
    with OutputInterceptor() as output:
        help(func_name)
    description = []
    for i in output[3:]:
        if len(i) > 0:
            description.append(i)
    context = {'func_name': func_name,
               'syntax': output[2],
               'description': description,
               'func_list': func_list,
               }
    return render(request, 'builtin_functions/detail.html', context)
