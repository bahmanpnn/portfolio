from datetime import date, datetime

from django import template

register = template.Library()


@register.filter()
def age(value):
    today_year = datetime.today().year
    birthday_year = value
    agee = int(today_year) - int(birthday_year)
    return agee


@register.filter()
def seprate_digits(value):
    value = str(value)
    value = value[-1::-1]
    new_string = ''
    counter = 1
    for i in range(len(value)):
        new_string += value[i]
        if counter % 3 == 0:
            if i != (len(value) - 1):
                new_string += ','
        counter += 1
    new_string = new_string[-1::-1]
    return new_string
