

def first_function():
    print("Iam the first")

from second import second_function

print(__name__)

if __name__ == "__main__":
    first_function()
    second_function()