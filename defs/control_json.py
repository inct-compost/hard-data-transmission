def load_login_params():
  """
  json/login_params.json から id と password を返す

  Returns:
    `login_params`: login_params.jsonの中身
  """
  import json
  import os

  # login_params.jsonを開く
  with open(os.getcwd() + '/json/login_params.json') as f:
    # jsonデータを取得
    load_data = json.load(f)
    return load_data

def load_jwt_token():
  """
  json/token.json から jwt_token を取得する

  Returns:
    `jwt_token`: id_tokenを発行する際の認証に必要なトークン
  """
  import json
  import os
  from defs.get_jwt_token import get_jwt_token

  # token.jsonを開き、データを取得
  with open(os.getcwd() + '/json/token.json') as f:
    load_data = json.load(f)

  # jwt_token が存在する場合その値を返す
  if ('load_data["jwt_token"]' in locals()):
    return load_data['jwt_token']
  # 存在しなかった場合は get_jwt_token を実行し、jwt_token を発行処理を行う
  else:
    get_jwt_token()
    # token.jsonを開き、データを取得し返す
    with open(os.getcwd() + '/json/token.json') as f:
      load_data = json.load(f)
      return load_data['jwt_token']

def load_id_token():
  """
  json/token.json から id_token を返す

  Returns:
    `id_token`: APIを叩くために必要な認証情報トークン
  """
  import json
  import os
  from defs.get_jwt_token import get_jwt_token
  from defs.verify_jwt_token import verify_jwt_token

  # token.jsonを開き、データを取得
  with open(os.getcwd() + '/json/token.json') as f:
    load_data = json.load(f)

  # id_token が存在する場合その値を返す
  if ('load_data["id_token"]' in locals()):
    return load_data['id_token']
  # 存在しなかった場合は get_jwt_token と verify_jwt_token を実行し、id_token を発行処理を行う
  else:
    get_jwt_token()
    verify_jwt_token()
    # token.jsonを開き、データを取得し返す
    with open(os.getcwd() + '/json/token.json') as f:
      load_data = json.load(f)
      return load_data['id_token']

def dump_token_json(data):
  """
  引数のjsonデータを`token.json`ファイルに出力する

  Parameters:
    `data`: jsonデータ
  """
  import json
  import os

  # token.jsonをを編集状態で開き、引数をjsonファイルにエクスポート
  with open(os.getcwd() + '/json/token.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
