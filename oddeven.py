def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    print("Even and odd",check_even_odd(10))