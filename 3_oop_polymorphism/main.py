from animals import Cat, Dog
from shape import Shape, Square, Circle


def polymorphic_methods():
    """
    Polymorphisme de méthodes
    """
    print(len("CentraleCasa"))
    print(len(["Python", "Java", "C"]))
    print(len({"name": "John", "address": "Nepal"}))


def polymorphic_class_methods():
    """
    Polymorphisme de méthodes de classe
    """
    cat1 = Cat("Kitty", 2.5)
    dog1 = Dog("Fluffy", 4)
    for animal in [cat1, dog1]:
        animal.info()
        animal.make_sound()


def polymorphic_inheritence(shape: Shape):
    """
    Quand on hérite d'une classe, nous pouvons redéfinir certaines méthodes et
    attributs spécifiquement pour s'adapter à la classe enfant, connue sous
    le nom : Method Overriding. Le polymorphisme nous permet d'accéder à ces
    méthodes et attributs surchargés qui portent le même nom que la classe
    parent.
    """
    print(f"{shape.name}: ")
    print(f"{shape.fact()}")
    print(f"area = {shape.area()}")


if __name__ == "__main__":
    circle = Circle(2)
    polymorphic_inheritence(circle)
    print("----------------")
    carre = Square(2)
    polymorphic_inheritence(carre)
