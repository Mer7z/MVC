import mariadb as sql

class ConexionDB():

    def __init__(self):
        self.__host = "localhost" # Cambia si el servidor está en un host remoto
        self.__user = "root"
        self.__password = ""
        self.__port = 3306
        self.__database = "mvc"
        self.__conection = None


    def crearConexion(self):
        self.__conection = sql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            port = self.__port,
            database = self.__database
        )

    def cerrarConexion(self):
        if self.__conection:
            self.__conection.close()
            self.__conection = None

    # poner aquí getters y setters

    def getConexion(self):
        return self.__conection