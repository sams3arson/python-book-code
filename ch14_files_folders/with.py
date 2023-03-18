# with - менеджер контекста, удобен для очистки таких объектов, как открытые файлы
# syntax =  with [experssion] as [variable_name]:
# файл будет закрыт автоматически после выхода из блока with

with open("relativity", "r") as fout:
    poem = fout.read()
print("read w\\ 'with':", len(poem))

