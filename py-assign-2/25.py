#25.	Write a function that accepts any number of arguments using *args.
def print_all_arguments(*args):
    """Accepts any number of arguments and prints them out."""
    print(f"Arguments received as a tuple: {args}")
    
    # You can loop through the arguments individually
    for index, arg in enumerate(args):
        print(f"Argument {index}: {arg}")

# Examples of calling the function with different numbers of arguments:
print_all_arguments()                                # 0 arguments
print_all_arguments("Apple", "Banana")               # 2 arguments
print_all_arguments(10, [1, 2, 3], True, "Python")   # 4 mixed-type arguments
