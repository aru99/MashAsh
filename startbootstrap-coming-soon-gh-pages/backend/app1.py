from flask import Flask, render_template, request,redirect,url_for
import requests
app = Flask(__name__)
import csv


@app.route('/')
def student():

	return render_template('index.html')

@app.route('/forms',methods = ['POST'])
def result():
	
	if request.method == 'POST':
		Sname =request.form['Sname']
		name  =request.form['name']
		email =request.form['email']
		phone =request.form['phone']
		news  =request.form['news']
		news1 =request.form['news1']
		date  =request.form['date']
		

		row = [name, Sname ,email,phone,news,news1,date]
		with open('exampleCsv.csv','a') as f:
			writer=csv.writer(f)
			writer.writerow(row)
			
 			f.close()
 			#return "thanks for submission"
 			return redirect(url_for('student'))

 		

@app.route('/querry',methods = ['POST'])
def result1():
	if request.method == 'POST':
		name1  =request.form['name1']
		email1 =request.form['email1']
		phone1 =request.form['phone1']
		message=request.form['message']

		row1 = [name1,email1,phone1,message]
		with open('exampleCsv1.csv','a') as f1:
			writer=csv.writer(f1)
			writer.writerow(row1)
			
 			f1.close()
 			#return "thanks for submission"
 			return redirect(url_for('student'))




if __name__ == '__main__':
	app.run(debug = True)

