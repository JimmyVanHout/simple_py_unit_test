import importlib
import os
import sys
import tested

def test_f(test_func):
    inputs = [1, 2, 3]
    outputs = [1, 2, 3]
    test_func(tested.f, inputs, outputs)

def test_g(test_func):
    inputs = [1, 2, 3]
    outputs = [1, 2, 3]
    test_func(tested.g, inputs, outputs)

def test_h(test_func):
    inputs = [1, 2, 3]
    outputs = [1, 2, 3]
    test_func(tested.h, inputs, outputs)

def test_all(test_func):
    test_f(test_func)
    print()
    test_g(test_func)
    print()
    test_h(test_func)

def import_module(file_path):
    file_name = os.path.basename(file_path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Could not locate file " + str(file_name) + "\n")
    module_name = file_name.rstrip(".py")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    test_function_module = import_module("../test_function.py")
    test_all(test_function_module.test_func)
    sys.exit(0)
