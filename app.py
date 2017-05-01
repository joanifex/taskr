from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

tasks = []
@app.route('/')
def index():
    return render_template('tasks.html', tasks=tasks)

@app.route('/create/', methods=['POST'])
def create():
    name = request.form['name']
    date = request.form['date']
    tasks.append({'name': name, 'date': date})
    return redirect('/')

@app.route('/update/<i>/', methods=['GET', 'POST'])
def update(i):
    if request.method == 'GET':
        return render_template('task.html', task=tasks[int(i)], index=i)
    elif request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        tasks[int(i)] = {'name': name, 'date': date}
        return redirect('/')

@app.route('/delete/<i>/')
def delete(i):
    del tasks[int(i)]
    return redirect('/')

def main():
    tasks.append({'name': 'task 1', 'date': '2017-05-01'})
    tasks.append({'name': 'task 2', 'date': '2017-05-01'})
    app.run('localhost', 8000, debug=True)

if __name__ == '__main__':
    main()
