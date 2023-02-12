import itertools

print("#chain")
# itertools.chain(*iterable_args) - проходит по аргументам, как если бы они были единым итерабельным объектом
for item in itertools.chain([1, 2], ("a", "b"), {"FREE": "TOP G"}):
    print(item)

print("#cycle")
# itertools.cycle(iterable) - бесконечный цикл по итерабельному аргументу
for item in itertools.cycle([1, 2]):
    print(item)
    break

print("#accumulate-sum")
# itertools.accumulate(iterable) - проходится по iterable, накапливая значение функцией, принимающей накопленное
# значение и следующее значение итератора; возвращает iterable из результатов функции
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

print("#accumulate-multiply")
for item in itertools.accumulate([1, 2, 3, 4], lambda x, y: x * y):
    print(item)


