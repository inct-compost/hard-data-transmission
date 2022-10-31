def verify_jwt_token(jwt_token: str):
  """
  発行されたJWTトークンを検証し、Idトークンを含んだjsonファイルを生成する

  Parameters:
    `jwt_token`: Firebase Functions の `generateCustomToken`で発行したJWT形式のカスタムトークン

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
    """
    引数のjsonデータをjsonファイルとして出力する

    Parameters:
      `data`: jsonデータ
    """
    with open(os.getcwd() + '\json\id_token.json', 'w') as f:
      json.dump(data, f, ensure_ascii=False, indent=2)

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
    dumpJson(json_data)
    return True
  else:
    json_data = {
      'jwt_token': jwt_token,
      'id_token': 'NULL',
    }
    dumpJson(json_data)
    return False