import platform


class Gizmo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):

        if id(self) == id(other):
            return True

        if not isinstance(other, Gizmo):
            return False

        return self.name == other.name \
               and self.age == other.age


def main():
    x = Gizmo("max", 31)
    y = Gizmo("max", 30)

    if x == y:
        print("Equal")

    print("Main done.. python-%s." % platform.python_version())


if __name__ == "__main__":
    main()
