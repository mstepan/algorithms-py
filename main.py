import platform


def main():
    data = {"one": 1, "two": 2}

    for k, v in data.items():
        print("%s=%s" % (k, v))

    print("Main done.. python-%s." % platform.python_version())


if __name__ == "__main__":
    main()
