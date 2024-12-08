def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(42)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [3.14, 'hello', False]
values_dict = {'a': 100, 'b': 'dict_string', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

