from flask import Flask , render_template
app= Flask(__name__)
@app.route('/index.html')
def index():
	return render_template("index.html")
@app.route('/hobbies.html')
def hob():
	return render_template("hobbies.html")
@app.route("/about.html")
def about():
	return render_template("about.html")
@app.route("/contact.html")
def contact():
	return render_template("contact.html")
@app.route("/projects.html")
def projects():
	return render_template("projects.html")
@app.route("/lists")
def list():
	list={"markzuck" , "Amin Hijaz" , "steve jobs" , "Messi" }
	display = True
	return render_template("lists.html" , list=list , display=display)
if __name__== '__main__':
	app.run()
