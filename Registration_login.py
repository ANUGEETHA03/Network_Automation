from flask import Flask, render_template, redirect, url_for, request

data = {}
app=Flask(__name__,template_folder="templates")

@app.route('/')
#Function for displaying the Initial Webpage
def intro():
	return render_template('intro.html')

@app.route('/register.html')
#Function for displaying the Register page after clicking register button
def register():
	return render_template('register.html')

@app.route('/login.html')
#Function for displaying the Login page after clicking Login button
def login():
        return render_template('login.html')

@app.route('/register_data.html', methods = ['GET','POST'])
#Function which GET or retrieves the data(username and password)once we enter the credentials and stores it in register_data.html(virtual location)
def register_data():
	if request.method == 'GET' :
		user_name = request.args.get('username','')
		if user_name not in data.keys():
			pass_word = request.args.get('password','')
			print('Username :' + user_name + ' Password: ' + pass_word)
			data.update({user_name : pass_word})
			print(data)
			return("Registered Successfully")
		else:
			print("Username already exists!!")
			return("This username is already taken")

@app.route('/login_data.html', methods = ['GET','POST'])
#Function which check whether the user is already registerd by retrieving data from vitual location login_data.html
def login_data():
	if request.method == 'GET' :
		user_name = request.args.get('username','')
		pass_word = request.args.get('password','')
		print('Username :' + user_name + ' Password: ' + pass_word)
		if user_name not in data.keys():
			return("This username does not exist,Do you want to register now?")

		elif(data[user_name] != pass_word):
			return("Invalid username or password")

		elif(data[user_name] == pass_word):
			return render_template('loginSuccess.html', user = user_name)
		else:
			return("Internal server error 500")

if __name__=='__main__':
	app.debug =True
	app.run(host='192.168.44.159',port=80)
