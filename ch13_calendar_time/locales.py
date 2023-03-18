import locale
from datetime import date

halloween = date(2014, 10, 31)
for lang_contry in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is']:
    locale.setlocale(locale.LC_TIME, lang_contry)
    print(lang_contry + ":", halloween.strftime("%A, %B, %d"))

names = locale.locale_alias.keys()
# самый распротраненный формат локали = 2-символьный код языка, подчеркивание,
# 2-символьный код страны

good_names = [name for name in names if len(name) == 5 and name[2] == "_"]
print(good_names[:5])
german = [name for name in good_names if name[:2] == "de"]
print(german)

# внимание: некоторые локали могут не поддерживаться ОС (или нужно их
# установить), тогда будет выведена ошибка locale.Error: unsupported locale

