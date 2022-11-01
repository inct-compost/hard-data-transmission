def verify_jwt_token():
  """
  発行されたJWTトークンを検証し、Idトークンを含んだjsonファイルを生成する

  Parameters:
    `jwt_token`: Firebase Functions の `generateCustomToken`で発行したJWT形式のカスタムトークン

  Returns:
    検証成功: True
    失敗: False

  Notes:
    run command | `python main.py verify_jwt_token`
  """
  import requests
  from defs.control_json import load_jwt_token, dump_token_json

  jwt_token = load_jwt_token()

  payload = {
    'token': jwt_token,
    'returnSecureToken': 'true'
  }

  # IDトークンの検証リクエスト
  res = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=AIzaSyBS5YJp8t7SMdQK-A3h8kW8gIdQy0iRzdM', params = payload)

  # 成功時はidTokenをjsonファイルに出力
  if (res.status_code == 200):
    json_data = {
      'jwt_token': jwt_token,
      'id_token': res.json()['idToken'],
    }
    dump_token_json(json_data)
    return True
  else:
    json_data = {
      'jwt_token': jwt_token,
      'id_token': 'NULL',
    }
    dump_token_json(json_data)
    return False