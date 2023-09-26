class ContextManagerExample:
    def __init__(self, id) -> None:
        self.id = id
        self.result = None

    def some_method(self):
        print(f"object ({self.id}) is doing something")

    def divide_number(self, n1, n2):
        self.result = n1 / n2

    def __enter__(self):
        print("(enter) doing extra stuff when entering context")
        print("(enter) returning the class object")
        return self

    def __exit__(
        self,
        exc_type,  # is the Exception class raised within the context
        exc_value,  # is the Exception message
        exc_tb,  # is the trace back of Exception
    ):
        print("(exit) doing extra stuff when exiting context")

        # if returning True, errors are suppressed
        # we can use this to catch acceptable Exception and do a "finally"
        if exc_type is ZeroDivisionError:
            self.result = 0
            return True

        # if returning False, errors are raised
        return False




