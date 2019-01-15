#!/usr/bin/python3
from flask import Flask, jsonify, abort, make_response
import requests as r
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

splash = ",---------. .--.      .--.   ____       ____       .-'''-.\r\n\
\          \|  |_     |  | .'  __ `.  .'  __ `.   / _     \ \r\n\
 `--.  ,---'| _( )_   |  |/   '  \  \/   '  \  \ (`' )/`--' \r\n\
    |   \   |(_ o _)  |  ||___|  /  ||___|  /  |(_ o _).    \r\n\
    :_ _:   | (_,_) \ |  |   _.-`   |   _.-`   | (_,_). '.  \r\n\
    (_I_)   |  |/    \|  |.'   _    |.'   _    |.---.  \  : \r\n\
   (_(=)_)  |  '  /\  `  ||  _( )_  ||  _( )_  |\    `-'  | \r\n\
    (_I_)   |    /  \    |\ (_ o _) /\ (_ o _) / \       /  \r\n\
    '---'   `---'    `---` '.(_,_).'  '.(_,_).'   `-...-'   \r\n"

tasks = [
    {
        'id': 1,
        'title': u'Buy geoceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/')
def index():
    return "Goodbye cruel world!\n"

@app.route('/twice/api/v1.0', methods=['GET'])
def twice_index():
    return splash

@app.route('/twice/api/v1.0/members')
def members():
    result = ''
    html = r.get('http://twice.wikia.com/wiki/Category:Members').text
    soup = bs(html, 'html.parser')
#m = soup.find_all(attrs={"class": "category-page__member-link"})
        
    m = soup.findAll(True, {'class': ['category-page__member-link']})
    for member in m:
        result += f'{member.get_text()}\n'
    return result

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)

