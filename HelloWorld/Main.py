# coding=utf-8
import math
import datetime


def arithmetic(fValue, sValue, operation):
    if operation == "+":
        print fValue + sValue
    elif operation == "-":
        print fValue - sValue
    elif operation == "*":
        print fValue * sValue
    elif operation == "/":
        print fValue / sValue
    else:
        print "Неизвестная операция"


def is_year_leap(year):
    if (year % 4 == 0) and (year % 100 != 0) and (year % 400 != 0):
        # if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print "високосный"
    else:
        print "обычный"


def square(side):
    P = side * 4
    S = side ** 2
    d = math.sqrt(2) * side
    return P, S, d


def season(mouth):
    numMouth = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    if numMouth[0:3].count(mouth):
        print "Зима"
    elif numMouth[3:6].count(mouth):
        print "Весна"
    elif numMouth[6:9].count(mouth):
        print "Лето"
    elif numMouth[9:12].count(mouth):
        print "Осень"
    else:
        print "Нет такого месяца"


def bank(a, years):
    for i in range(0, years):
        a = a * 1.1
    return a


def is_prime(num):
    return num


def date(year, month, day):
    try:
        datetime.datetime(year, month, day)
    except Exception:
        return False
    else:
        return True
