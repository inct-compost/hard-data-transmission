def get_jwt_token():
  """
  IDとパスワードを元にIDベースのJWTトークンを発行する

  Returns:
    発行成功: True
    失敗: False

  Notes:
    run command | `python main.py get_jwt_token`
  """
  import requests
  import netifaces
  from defs.control_json import load_login_params, dump_token_json

  login_params = load_login_params()

  # TODO: ラズパイでテストする際にコメントアウトを外す
  """ interface_data = netifaces.ifaddresses('eth0')

  payload = {
    'id': id,
    'mac': interface_data[netifaces.AF_LINK][0]['addr'],
    'pass': passwd
  } """

  payload = {
    'id': login_params['id'],
    'mac': '4c:bb:97:a7:30:6e',
    'pass': login_params['pass']
  }

  res = requests.get('http://localhost:5001/research2022-5j/us-central1/generateCustomToken', params = payload)
  # print(res.text)

  if (res.status_code == 200):
    json_data = {
      'jwt_token': res.text,
    }
    dump_token_json(json_data)
    return True
  else:
    json_data = {
      'jwt_token': 'NULL',
    }
    dump_token_json(json_data)
    return False