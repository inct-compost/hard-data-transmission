def get_jwt_token(id: str, passwd: str):
  """
  発行されたJWTトークンを検証し、Idトークンを含んだjsonファイルを生成する

  Parameters:
    `id`: デバイスに個々に割り振られたID
    `passwd`: データベースにアクセスするためのパスワード

  Returns:
    検証成功: True
    失敗: False

  Notes:
    run command | `python main.py get_jwt_token -i [id] [passwd]`
  """
  import json
  import requests
  import os
  import netifaces

  def dumpJson(data):
    with open(os.getcwd() + '\json\id_token.json', 'w') as f:
      json.dump(data, f, ensure_ascii=False, indent=2)

  # TODO: ラズパイでテストする際にコメントアウトを外す
  """ interface_data = netifaces.ifaddresses('eth0')

  payload = {
    'id': id,
    'mac': interface_data[netifaces.AF_LINK][0]['addr'],
    'pass': passwd
  } """

  payload = {
    'id': '0MkJJN50KeAeELphQgEq',
    'mac': '4c:bb:97:a7:30:6e',
    'pass': 'admin-pass'
  }

  res = requests.get('http://localhost:5001/research2022-5j/us-central1/generateCustomToken', params = payload)
  print(res.text)

  if (res.status_code == 200):
    json_data = {
      'jwt_token': res.text,
    }
    dumpJson(json_data)
    return True
  else:
    json_data = {
      'jwt_token': 'NULL',
    }
    dumpJson(json_data)
    return False