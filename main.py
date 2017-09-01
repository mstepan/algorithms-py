import platform

import sys


def main():
    index = 10

    print(dir(sys))
    print(locals())
    print(globals())

    print("Main done.. python-%s." % platform.python_version())

if __name__ == "__main__":
    main()
