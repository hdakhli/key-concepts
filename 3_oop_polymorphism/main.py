from animals import Cat, Dog
from shape import Shape, Square, Circle

"""
Polymorphisme de méthodes
"""
def polymorphic_methods():
    print(len("CentraleCasa"))
    print(len(["Python", "Java", "C"]))
    print(len({"name": "John", "address": "Nepal"}))


"""
Polymorphisme de méthodes de classe
"""
def polymorphic_class_methods():
    cat1 = Cat("Kitty", 2.5)
    dog1 = Dog("Fluffy", 4)
    for animal in [cat1, dog1]:
        animal.info()
        animal.make_sound()


"""
Quand on hérite d'une classe, nous pouvons redéfinir certaines méthodes et attributs 
spécifiquement pour s'adapter à la classe enfant, connue sous le nom : Method Overriding.
Le polymorphisme nous permet d'accéder à ces méthodes et attributs surchargés 
qui portent le même nom que la classe parent.
"""
def polymorphic_inheritence(shape: Shape):
    print(f"{shape.name}: ")
    print(f"{shape.fact()}")
    print(f"area = {shape.area()}")


if __name__ == "__main__":
    circle = Circle(2)
    polymorphic_inheritence(circle)
    print("----------------")
    carre = Square(2)
    polymorphic_inheritence(carre)
