from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

def main():
    app.run('localhost', 8000)

if __name__ == '__main__':
    main()
