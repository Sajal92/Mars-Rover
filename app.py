from flask import Flask, request, render_template, url_for, redirect
from navigate import MarsRover

app = Flask(__name__)
port = 5000
msg = []


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        inp = request.form

        tst = MarsRover(inp)
        msg.clear()
        msg.append(tst.run())

        return redirect(url_for('output'))

    return render_template('index.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        return redirect(url_for('homepage'))
    return render_template('output.html', msg_list=msg[0])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
    # app.run(debug=True)
