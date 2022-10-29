import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import argparse
from defs.add_sensing import add_admin, add
from defs.get_sensing import get
from defs.decode_token import check_token

cred = credentials.Certificate("./keys/serviceAccountKey.key.json") # ダウンロードした秘密鍵
options = {
  'serviceAccountId': 'firebase-adminsdk-6hx2q@research2022-5j.iam.gserviceaccount.com',
}
firebase_admin.initialize_app(cred)

uid = '5GU5x3Bi4LYR7pSOOkiofS0s24H2'
custom_token = auth.create_custom_token(uid)

#print(custom_token)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('function_name', type=str, help='set fuction name in this file')
  parser.add_argument('-i', '--func_args', nargs='*', help='args in functioFn', default=[])
  args = parser.parse_args()

  func_dict = {k: v for k, v in locals().items() if callable(v)}
  func_args = [float(x) if x.isnumeric() else x for x in args.func_args]
  ret = func_dict[args.function_name](*func_args)
