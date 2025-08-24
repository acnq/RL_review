import importlib
import sys
import os.path as osp


def load(name):
    pathname = osp.join(osp.dirname(__file__), name)
    # return importlib.load_source('', pathname)
    module_name = osp.splitext(osp.basename(name))[0]   # e.g. "simple_adversary"
    
    spec = importlib.util.spec_from_file_location(module_name, pathname)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
