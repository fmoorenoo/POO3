class Romanos:
    def enteroARomano(numEntero):
        numeros = [1000, 900, 500, 400,  100,  90,  50,  40,   10,   9,    5,    4,   1]
        letras =  ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        romano = ''
        i = 0
        while numEntero > 0:
            for x in range(numEntero // numeros[i]):
                romano += letras[i]
                numEntero -= numeros[i]
            i += 1
        return romano

