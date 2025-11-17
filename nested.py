def outer():
    def inner():
        print("nested function example ")
    inner()
outer()
