import argparse
from defs.add_sensing import add
from defs.get_sensing import get
from defs.verify_jwt_token import verify_jwt_token
from defs.get_jwt_token import get_jwt_token

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('function_name', type=str, help='set fuction name in this file')
  parser.add_argument('-i', '--func_args', nargs='*', help='args in functioFn', default=[])
  args = parser.parse_args()

  func_dict = {k: v for k, v in locals().items() if callable(v)}
  func_args = [float(x) if x.isnumeric() else x for x in args.func_args]
  ret = func_dict[args.function_name](*func_args)
