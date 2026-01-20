# Global variable
x = 10

def outer_function():
    # Nonlocal variable
    y = 20

    def inner_function():
        nonlocal y
        global x

        z = 30   # Local variable

        x = x + 5
        y = y + 5
        z = z + 5

        print("Inside inner function:")
        print("Global variable x:", x)
        print("Nonlocal variable y:", y)
        print("Local variable z:", z)

    inner_function()
    print("\nInside outer function:")
    print("Nonlocal variable y:", y)

outer_function()

print("\nOutside all functions:")
print("Global variable x:", x)
