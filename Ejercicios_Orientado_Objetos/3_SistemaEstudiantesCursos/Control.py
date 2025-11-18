from Estudiante import Estudiante
from Curso import Curso

def control():
    curso1 = Curso("POO102", "Programación Orientada a Objetos", 4)
    curso2 = Curso("BD302", "Bases de Datos", 2)
    estudiante1 = Estudiante("3057382", "Valentina", "ADSO")
    estudiante2 = Estudiante("2039589", "Andrés", "Sistemas")

    estudiante1.matricular(curso1)
    estudiante1.matricular(curso2)
    estudiante2.matricular(curso1)
    
    estudiante1.listar_cursos()
    estudiante2.listar_cursos()
    curso1.listar_estudiantes()
    curso2.listar_estudiantes()

control()