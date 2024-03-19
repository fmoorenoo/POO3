from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        if day <= 0 and day > 31:
            day = 1
        if month <= 0 and month > 12:
            month = 1
        if year < 1900 and year > 2050:
            year = 1900


    @staticmethod
    def is_leap_year(year: int) -> bool:
        resultado = False
        if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            resultado = True


    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month == 2:
            if Date.is_leap_year(year):
                return 29  
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31


    def get_delta_days(self) -> int:
        days = 0
        for y in range(1900, self.year):
            if Date.is_leap_year(y):
                days += 366
            else:
                days += 365
        for m in range(1, self.month):
            days += Date.days_in_month(m, self.year)
        days += self.day - 1
        return days


    @property
    def weekday(self) -> int:
        days = self.get_delta_days()
        return (days + 1) % 7


    @property
    def is_weekend(self) -> bool:
        if self.weekday > 5:
            return True
        else:
            return False


    @property
    def short_date(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"


    def __str__(self):
        weeks = ["DOMINGO", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO"]
        months = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
        return f"{weeks[self.weekday]} {self.day} DE {months[self.month - 1]} DE {self.year}"


    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __eq__(self, other) -> bool:
        ...
