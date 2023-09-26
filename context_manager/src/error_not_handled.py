from context_manager import ContextManagerExample

if __name__ == '__main__': 
    # this would raise error because the error (div by text) is not handled
    with ContextManagerExample(id='001') as obj:
        obj.some_method()
        obj.divide_number(5, "a")

    print(f"result is {obj.result}")