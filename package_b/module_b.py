from package_a.module_a import function_in_module_a

def function_in_module_b():
    return f"Function b from module_b calling: {function_in_module_a()}"
