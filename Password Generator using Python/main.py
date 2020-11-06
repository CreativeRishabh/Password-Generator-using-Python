import string #here we have imported string
import random #here we have imported random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)

    s2 = string.ascii_uppercase
    # print(s2)

    s3 = string.digits
    # print(s3)

    s4 = string.punctuation
    # print(s4)a

    passwordLength = int(
        input("Enter Number of characters for your password\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # print(s)

    random.shuffle(s)
    # print(s)

    print("Your Password is: ")
    print("".join(random.sample(s, passwordLength))) #This is another way to generate password

    # print("".join(s[0:passwordLength])) This is one way to generate password
