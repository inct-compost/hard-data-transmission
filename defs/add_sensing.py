def add():
  """
  データを追加する

  Parameters:

  Returns:

  Notes:
    run command | `python main.py add_sensing`
  """
  print('hello')

def add_admin(id: str, temperature: float, humidity: float):
  """
  アドミン権限を利用してデータを追加する

  Parameters:

  Returns:

  Notes:
    run command | `python main.py add_admin -i hardwareID 1 1`
  """
  import datetime
  from firebase_admin import firestore

  if (isinstance(id, str) and isinstance(temperature, float) and isinstance(humidity, float)):
    # 今日の日時を取得し保存
    nowDate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    # nowDate = datetime.datetime(2017, 4, 4, 9, 5, 28)

    # 今日の年月日を取得し保存(YYYYMMDD)
    month = '0' + str(nowDate.month)
    day = '0' + str(nowDate.day)
    date = str(nowDate.year) + month[-2:] + day[-2:]
    print(date)

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
    print(time)

    print(f'Add to sensingData/{id}/{date}/{time}')

    db = firestore.client()
    ref = db.collection('sensingData').document(id).collection(date).document(time)
    ref.set({
      u'date': nowDate,
      u'temperature': temperature,
      u'humidity': humidity,
    })
  else:
    print('input variables type not match')