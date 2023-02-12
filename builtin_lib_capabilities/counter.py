from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)

print(breakfast_counter)
print(breakfast_counter.most_common())  # все в убывающем порядке
print(breakfast_counter.most_common(1))  # в убывающем порядке, больше чем указанный аргумент

# счетчики можно складывать, вычитать, объединять, пересекать
lunch = ["eggs", "eggs", "bacon"]
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(breakfast_counter & lunch_counter)  # только те ключи, которые есть в обоих, наименьш. значение
print(breakfast_counter | lunch_counter)  # выбирает максимальный счетчик для ключа


