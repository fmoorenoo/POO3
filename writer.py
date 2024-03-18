class FileWriter:
    def __init__(self, fileName):
        self.fileName = fileName
        try:
            self.i = open(self.fileName, "r+")
        except Exception:
            self.i = open(self.fileName, "w+")

    def write(self, mensaje:str):
        self.i.write(mensaje)


    def read(self)->str:
        return self.i.readlines()


    def close(self):
        self.i.close()


if __name__ == '__main__':
    def main():
        pruebaw = FileWriter("fileWriter.txt")
        pruebaw.write("Hola")

        pruebaw.close()

        pruebar = FileWriter("fileWriter.txt")
        print(pruebar.read())
        pruebar.close()

    main()