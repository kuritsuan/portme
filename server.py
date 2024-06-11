from flask import Flask, render_template, url_for, request, redirect
import csv
import os

app = Flask(__name__)

def adding_database_csv(dictionary):


    with open("database.csv", mode='a') as my_file:
        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(my_file, fieldnames=fieldnames)
        if os.path.getsize("database.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerow(dictionary)
def adding_database_file(dictionary):
    print("This is file\n")
    with open("database.txt", mode='a') as my_file:
        for key, item in dictionary.items():
            my_file.write(f"{item}")
            if (key != 'message'):
                my_file.write(f',')
        my_file.write('\n')


@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:name_page>")
def page(name_page):
    return render_template(name_page)

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            adding_database_csv(data)
            return redirect('/thankyou.html')
        except:
            return "database was intercepted, Please Try Again Later!!!"
    else :
        return "something went wrong"