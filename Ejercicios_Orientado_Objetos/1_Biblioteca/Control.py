from Libro import Libro
Libro1 = Libro("Harry Potter", "JK Rowling", 1997, 450, True)
print(f"El libro es: {Libro1.get_titulo()}, su autor es: {Libro1.get_autor()}, el año de su publicación es: {Libro1.get_anioPublicacion()}, y su estado es: {Libro1.get_Estado()}")

Libro1.loan()                     
Libro1.returnBook()             