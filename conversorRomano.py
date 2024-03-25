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
    
    
    def romanoAEntero(numRomano):
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        entero = 0
        for i in range(len(numRomano)):
            if i > 0 and romanos[numRomano[i]] > romanos[numRomano[i - 1]]:
                entero += romanos[numRomano[i]] - 2 * romanos[numRomano[i - 1]]
            else:
                entero += romanos[numRomano[i]]
        return entero
    

if __name__ == '__main__':
    print(Romanos.enteroARomano(5))
    print(Romanos.romanoAEntero('IX'))


