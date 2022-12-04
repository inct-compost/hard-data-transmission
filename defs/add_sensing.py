def add(temp: float, hum: float):
  """
  データを追加する

  Parameters:

  Returns:

  Notes:
    run command | `python main.py add -i [temp] [hum]`
  """
  import datetime
  import requests
  from defs.control_json import load_id_token

  def req(req_body: object):
    """
    データを追加リクエストを行う

    Parameters:
      req_body: センシングデータや追加先のドキュメントアドレス

    Returns:
      res: データ追加が成功したかの情報

    Notes:
    """
    return requests.post('https://us-central1-research2022-5j.cloudfunctions.net/addSensingData', json=req_body)

  id_token = load_id_token()

  if (id_token != 'NULL' and isinstance(temp, float) and isinstance(hum, float)):
    # 今日の日時を取得し保存
    nowDate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

    # 今日の年月日を取得し保存(YYYYMMDD)
    month = '0' + str(nowDate.month)
    day = '0' + str(nowDate.day)
    date = str(nowDate.year) + month[-2:] + day[-2:]
    # print(date)

    # 現在の時間（時）を取得し2桁で保存
    hour = '0' + str(nowDate.hour)
    # 現在の時間（分）を取得し、15の倍数でどの値に一番近いかを求め2桁で保存
    minute = '0' + str(int((round(nowDate.minute / 15, 0) * 15)))
    if(minute == '060'):
      # もし minute が '060' だった場合は hour をインクリメントし、minute を '00'にする
      hour = '0' + str(nowDate.hour + 1)
      minute = '00'

    # 現在の時分を保存(HHMM)
    time = hour[-2:] + minute[-2:]
    # print(time)

    print(f'RUN | Add to sensingData/[id]/{date}/{time}')

    req_body={
      'token': id_token,
      'datetime': {
        'date': date,
        'time': time
      },
      'data': {
        'date': nowDate.isoformat(),
        'temperature': temp,
        'humidity': hum,
      }
    }

    res = req(req_body)
    print(f'STATUS | {res.status_code}: {res.text}')
  else:
    print('WARN | input variables type not match')
