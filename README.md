# Istoki catalog

Source of truth: `input/istoki.xlsx`

Build script: `scripts/build_catalog.py`

Published via GitHub Pages from `docs/`:
https://aleyakim.github.io/istoki-catalog/


rules for xls:
"Правила заполнения songs :
обязательные для каждой строки: id, title, hub, lyrics
themes — список через ; (пример: служба; дорога; товарищество)
externalLinks — список ссылок через ;
altTitles — просто строка (можешь тоже через ;, но это останется строкой как есть)
lyrics — многострочный текст 

Правила versions:
songId должен совпадать с songs.id
id — идентификатор версии (например v1, short, choir)
остальные поля могут быть пустыми

Правила glossary:
songId должен совпадать с songs.id
term и definition не пустые
если у песни нет глоссария — просто нет строк для этой песни"

пушить через xls через cmd:
git status
git add input/istoki.xlsx
git commit -m "Catalog: update workbook"
git push
Если git push отклонит (remote впереди), тогда добавляется:
Bash
git pull --rebase origin main
git push

/////////////////////////////////////////////////////////////

## Сборка каталога

### Ручная сборка через GitHub Actions
1. Перейти на вкладку [Actions](../../actions)
2. Выбрать **Manual Build Catalog**
3. Нажать **Run workflow**
4. Опционально указать причину
5. Нажать зелёную кнопку **Run workflow**

Каталог обновится автоматически через ~30 секунд.

### Локальная сборка
Требования:
- Python 3.8+
- Библиотеки: `pandas`, `openpyxl`

```bash
# Установка зависимостей (один раз)
pip install pandas openpyxl

# Сборка каталога
cd istoki-catalog
python scripts/build_catalog.py

# Коммит и отправка
git add docs/
git commit -m "Обновлён каталог"
git push
