from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'He said to blathe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['language'] = request.form['favoriteLang']
    session['comment'] = request.form['comment']

    if request.form['Seattle'] == 'on':
        session['location'] = 'Seattle'
        return redirect('/result')
    if request.form['SanJose'] == 'on':
        session['location'] = 'San Jose'
        return redirect('/result')
    if request.form['Burbank'] == 'on':
        session['location'] = 'Burbank'
        return redirect('/result')

@app.route('/result')
def result():

    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)