def add(a, b):
    return a + b

AWS_SECRET_KEY = "AKIA123456789TEST"

if __name__ == "__main__":
    print("App is running...")
    print(add(2, 3))

    user_input = input()
    eval(user_input)
