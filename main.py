class Persona():
    def __init__(self, nombre=''):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    def funcionalidad(self):
        return 'Funcionalidad de persona'


class Alumno(Persona):
    def __init__(self, nombre='', legajo=0):
        super().__init__(nombre)
        self.legajo = legajo

    @property
    def legajo(self):
        return self.__legajo

    @legajo.setter
    def legajo(self, value):
        self.__legajo = value

    def funcionalidad(self):
        return super().funcionalidad() + ' Necesito que haga otra cosa'


if __name__ == '__main__':
    persona = Persona('Sandro')
    print("Diccionario de persona", persona.__dict__)

    otra_persona = Persona("Michael")
    print("Diccionario de otra_persona", otra_persona.__dict__)

    alumno = Alumno('Washington', 2000)
    print("Diccionario de alumno", alumno.__dict__)

    print(persona.funcionalidad())
    print(otra_persona.funcionalidad())
    print(alumno.funcionalidad())
