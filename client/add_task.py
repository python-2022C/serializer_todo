import requests


data = {
    'name': 'task1',
    'description': 'this is task1',
    'user': 'diyor'
}

r = requests.post('http://127.0.0.1:8000/todo/', json=data)
print(r.text)