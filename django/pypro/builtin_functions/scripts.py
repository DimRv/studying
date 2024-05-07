import re
from io import StringIO
import sys


def get_syntax(func_name):
    """Получение синтаксиса функции c помощью help()"""
    class OutputInterceptor(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO()
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio
            sys.stdout = self._stdout

    with OutputInterceptor() as output:
        help(func_name)
    if output[0].startswith('Help on class'):
        r = re.compile(f".*\|.*{func_name}\(.*\).*")
    else:
        r = re.compile(f'{func_name}\(.*\)')
    output = list(filter(r.match, output))
    if output[0].endswith(", /)"):
        output[0] = output[0].replace(", /)", ')')
    return output


def replace_func(m):
    functions = [i for i in dir(__builtins__) if i[0] in [chr(j) for j in range(97, 123)]]
    if m[0] in functions:
        return f'<span class="code-func">{m[0]}</span>'
    else:
        return m[0]


def makeColoderCode(code):
    code = re.sub(r'(\b\w{2,})', replace_func, code)
    return code


if __name__ == "__main__":
    print(makeColoderCode('print(sep=" ")'))
    print(makeColoderCode('abs()'))
    print(makeColoderCode('bla()'))
    print(get_syntax('print'))
    print(get_syntax('abs'))
    print(get_syntax('list'))