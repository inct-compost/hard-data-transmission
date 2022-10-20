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
    run command | `python main.py add_sensing`
  """
  import datetime
  from firebase_admin import firestore

  if (isinstance(id, str) and isinstance(temperature, float) and isinstance(humidity, float)):
    nowDate = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    #nowDate = datetime.datetime(2017, 11, 12, 9, 5, 28)
    date = str(nowDate.year) + str(nowDate.month) + str(nowDate.day)
    print(date)
    hour = '0' + str(nowDate.hour)
    minute = '0' + str(nowDate.minute)
    time = hour[-2:] + minute[-2:]
    print(time)
    db = firestore.client()
    #ref = db.collection(id).document(date).collection(time)
    #ref.set({
    #  u'date': datetime.datetime(),
    #  u'temperature': temperature,
    #  u'humidity': humidity,
    #})
  else:
    print('input variables type not match')