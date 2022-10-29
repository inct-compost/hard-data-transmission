def verify_custom_token(jwt_token):
  """
  発行されたJWTトークンを検証し、

  Parameters:

  Returns:

  Notes:
    run command | `python main.py add_sensing`
  """
  import requests

  payload = {
    'token': jwt_token,
    'returnSecureToken': 'true'
  }

  r = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=AIzaSyBS5YJp8t7SMdQK-A3h8kW8gIdQy0iRzdM', params = payload)
  print(r.json()['idToken'])
