from datetime import date, datetime as dt, timedelta as td


def month_to_num(month):
    RU_MONTH_VALUES = (('января', '1'),
                       ('ферваля', '2'),
                       ('марта', '3'),
                       ('апреля', '4'),
                       ('мая', '5'),
                       ('июня', '6'),
                       ('июля', '7'),
                       ('августа', '8'),
                       ('сентября', '9'),
                       ('октября', '10'),
                       ('ноября', '11'),
                       ('декабря', '12'))
    for old, new in RU_MONTH_VALUES:
        if old == month:
            return new


def convert_date(date_str):
    old_date = date_str.split(' ')
    new_date = f"{old_date[0]} {month_to_num(old_date[1])} {date.today().year}"
    return dt.strptime(new_date, '%d %m %Y').date()


def last_friday():
    today = date.today()
    return today - td(days=(int(today.strftime('%w')) + 2))


def get_old_charts(weeks=1):
    if isinstance(weeks, int) and weeks<6:
        week_list = []
        lf = last_friday()
        while weeks>=0:
            if weeks == 0:
                week_list.append('')
                break
            week_list.append(str(lf - td(days=7*weeks)))
            weeks -= 1
        return week_list
    return None