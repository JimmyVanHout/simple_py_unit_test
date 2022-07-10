import importlib
import os
import sys

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
