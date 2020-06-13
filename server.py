from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)


def write_to_file(*data):
    with open('database.txt', 'a') as database:
        email = data[0]
        subject = data[1]
        message = data[2]
        database.write(f'\n{email},{subject},{message}')


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
            return redirect('/thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
