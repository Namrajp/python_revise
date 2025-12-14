import sys

def main():
    try:
        say_hello(sys.argv[1])
    except IndexError:
        print("too few or many arguments.")





def say_hello(name):
    print(f"Hello, {name}!")



main()
