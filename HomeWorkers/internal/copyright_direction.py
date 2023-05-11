import re

import REGEX
import typing


def is_copyright_UWORK(message: str) -> str:
    """
    TODO: get link from message (event.message.text)
    text - **Дизайнер** — 15 000р
Дизайн офисного помещения.
[Откликнуться](https://kwork.ru/projects/2037343/view?ref=607680)

**Смм-специалист **— 10 000р
Разместить книги на сайте.
[Откликнуться](https://kwork.ru/projects/2036538/view?ref=607680)

**Звукорежиссер** — 3 000р
Написать саундтрек для моей игры длительность 3:00.
[Откликнуться](https://kwork.ru/projects/2037290/view?ref=607680)

**Тех.специалист** — 3 000р
Написать ТГ-бота по примеру - Прогноз погоды.
[Откликнуться](https://kwork.ru/projects/2037449/view?ref=607680)

**Копирайтер** — 2 000р
Подготовить новостной дайджест по Wildberries
[Откликнуться](https://kwork.ru/projects/2037343/view?ref=607680)

➖➖➖
✏️ [Вакансии для копирайтеров](https://t.me/+24yrS3lIQJNmYjAy)
🎨 [Вакансии для дизайнеров](https://t.me/+-fpZTUM9CXk4ZGFi)
🧑‍💻 [HR вакансии](https://t.me/+LvtcwqsQdqFmM2U6)
    :param message:
    :return:
    """
    if 'Откликнуться' not in message:
        return ''
    orders = re.findall(REGEX.regex_copyright, message)
    if not orders:
        return ''
    return f'#Копирайт\n' \
           f'Количество заказов - {len(orders)}'



