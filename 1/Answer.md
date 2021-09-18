# Ответы

Проблемы: 
* при парсинге в колонке Fair часть данных имеют некорректный тип данных, так как загрузился делимитер “.”. Как починить: нужно заменить все значения точки “.” на запятую “,” в колонке Fair.

Сводная таблица:
* Значения: survived (sum), survived (average)
* Строки: sex
* Столбцы: Pclass

Query: 

```
=QUERY(train!A1:L892;"SELECT SUM(B) WHERE E = 'female'")
```

Ссылка на гугл-док:

https://docs.google.com/spreadsheets/d/10swNfFEf2sH6Zu2aE_XE32djqRcMjE1f-M3zGxEYh7k/edit?usp=sharing
