from flask import Flask
app = Flask(__name__)

@app.route('/')
def swetha():
        return '<body style="background-color:powderblue;"><h2>Welcome to IFT510-Project by Swetha</h2></body>'


@app.route('/hello')
def swetha1():
        return '<p style="background-color:tomato;"> Welcome to the second page </p>'
	

if __name__ == '__main__':	
	app.run(host="0.0.0.0", debug=True)
