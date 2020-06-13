from flask import Flask, render_template, request, url_for
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('index.html')


@app.route('/works', methods=['POST', 'GET'])
def works():
    return render_template('works.html')


@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template('contact.html')


@app.route('/work', methods=['POST', 'GET'])
def work():
    return render_template('work.html')


def write_to_csv(*data):
    with open('database.csv', 'a', newline='') as database2:
        email = data[0]
        subject = data[1]
        message = data[2]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form['email']
            data2 = request.form['subject']
            data3 = request.form['message']
            write_to_csv(data, data2, data3)
            return render_template('thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
