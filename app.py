from flask import Flask, render_template
app = Flask(__name__)

tasks = []
@app.route('/')
def index():
    return render_template('tasks.html', tasks=tasks)

def main():
    tasks.append('task 1')
    tasks.append('task 2')
    app.run('localhost', 8000)

if __name__ == '__main__':
    main()
