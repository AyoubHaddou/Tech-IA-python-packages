from first import first_function

def second_function():
    print("Iam the second")

print(__name__)

if __name__ == "__main__":
    first_function()
    second_function()