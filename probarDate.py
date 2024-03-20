from date import Date
def main():
    fecha1 = Date(30, 3, 2024)
    fecha2 = Date(20, 3, 2024)
    print(f"Días desde el 1/1/1900: {fecha1.get_delta_days()}") 
    print(f"Día de la semana: {fecha1.weekday}")
    print(f"¿Fin de semana? {fecha1.is_weekend}")
    print(f"Fecha corta: {fecha1.short_date}")
    print(f"Fecha larga: {fecha1.__str__()}")
    print(f"Sumar días a la fecha: {fecha1.__add__(265)}")
    print(f"¿Fecha 1 < que fecha 2? {fecha1 < fecha2}")
    print(f"¿Fecha 1 > que fecha 2? {fecha1 > fecha2}")
    print(f"¿Fecha 1 = que fecha 2? {fecha1 == fecha2}")

    


main()