from date import Date
def main():
    unDia = Date(1, 1, 2005)
    print(f"Días desde el 1/1/1900: {unDia.get_delta_days()}\n Día de la semana: {unDia.weekday}")
    print(f"¿Fin de semana? {unDia.is_weekend}\n Fecha corta: {unDia.short_date}\n Fecha larga: {unDia.__str__()}")


main()