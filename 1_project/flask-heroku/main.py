from flask import Flask
app = Flask(__name__) 

@app.route("/")
def home():
	return "Hello Flask 3"

@app.route("/test")
def test():
	return "This is Test 3"

if __name__=="__main__":
	app.run()


# 佈署heroku教學 https://www.youtube.com/watch?v=wWRYBUzEG6E