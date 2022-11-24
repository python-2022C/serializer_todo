import requests


data = {
    'name': 'task1',
    'description': 'this is task1(update2)',
    'user': 'sanjarbek'
}

r = requests.post('http://127.0.0.1:8000/todo/update/2', json=data)
print(r.text)