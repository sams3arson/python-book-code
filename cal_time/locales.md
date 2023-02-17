# Locales (локали)
Имена дат соответствует локали - региональному набору настроек ОС.
Для вывода других названий можно изменить локааль с помощью функции `setlocale`.

```
set_locale(locale.LC_TIME, locale_string)
```

`locale.LC_TIME` - атрибут модуля `locale`
`locale_string` - строка, соответств. нужной локали. Все локали можно получить из
метода `locale.locale_alias.keys()`.

