
def create_palindrome(value):

    for i in range(len(value)-1, 0, -1):
        if str[i] != str[i+1]:
            break

    value






def main():

    base_str = "test"

    palindrome = create_palindrome(base_str)

    print("str: %s, palindrome: %s" % (base_str, palindrome))



if __name__ == "__main__":
    main()
