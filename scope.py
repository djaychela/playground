GLOBAL_CONSTANT = 42
print(GLOBAL_CONSTANT)
def outer_scope_function():
    some_value = hex(0x0)
    print(some_value)

    def inner_scope_function():
        nonlocal some_value
        some_value = hex(0xDEADBEEF)

    inner_scope_function()
    print(some_value)
    global GLOBAL_CONSTANT  
    GLOBAL_CONSTANT = 31337

outer_scope_function()
print(GLOBAL_CONSTANT)

