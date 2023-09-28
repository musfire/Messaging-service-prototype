from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple list to store messages
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        message = request.form['message']
        if message:
            messages.append(message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    from from waitress import serve
    serve(app, host="0.0.0.0", port=8080)waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    # app.run(debug=True)
