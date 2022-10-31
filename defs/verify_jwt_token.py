def verify_jwt_token(jwt_token: str):
  """
  発行されたJWTトークンを検証し、Idトークンを含んだjsonファイルを生成する

  Parameters:
    jwt_token: Firebase Functions の `generateCustomToken`で発行したJWT形式のカスタムトークン

  Returns:
    検証成功: True
    失敗: False

  Notes:
    run command | `python main.py verify_jwt_token -i [jwt]`
  """
  import json
  import requests
  import os

  def dumpJson(data):
    with open(os.getcwd() + '\json\id_token.json', 'w') as f:
      json.dump(data, f, ensure_ascii=False, indent=2)

  payload = {
    'token': jwt_token,
    'returnSecureToken': 'true'
  }

  res = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=AIzaSyBS5YJp8t7SMdQK-A3h8kW8gIdQy0iRzdM', params = payload)

  if (res.status_code == 200):
    print(res.json()['idToken'])
    json_data = {
      'jwt_token': jwt_token,
      'id_token': res.json()['idToken'],
    }
    dumpJson(json_data)
    return True
  else:
    json_data = {
      'jwt_token': jwt_token,
      'id_token': 'NULL',
    }
    dumpJson(json_data)
    return False