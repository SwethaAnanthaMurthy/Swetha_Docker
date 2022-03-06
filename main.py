from flask import Flask
app = Flask(__name__)

@app.route('/')
def swetha():
        return '<body style="background-color:powderblue;"><h2>Welcome to IFT510-Project by Swetha</h2></body>'


@app.route('/next')
def swetha1():
        return '<body style="background-color:tomato;"><h2> Publishing the docker container to GITHUB</h2> </body>'
	

if __name__ == '__main__':	
	app.run(host="0.0.0.0", debug=True)
