from firebase_admin import firestore

def get(uid):
  """
  データを追加する

  Parameters:

  Returns:

  Notes:
    run command | `python main.py get_sensing`
  """
  print('get data')
  db = firestore.client()
  ref = db.collection('sensingData').document(uid)
  doc = ref.get()
  if doc.exists:
    print(f'Document data: {doc.to_dict()}')
  else:
    print(u'No such document!')
