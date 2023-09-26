from context_manager import ContextManagerExample

if __name__ == '__main__':
    # this would NOT raise error because the error (div by zero) is handled
    with ContextManagerExample(id='000') as obj:
        obj.some_method()
        obj.divide_number(5, 0)

    print(f"result is {obj.result}")