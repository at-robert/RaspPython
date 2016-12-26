 # coding=UTF-8

from flask import Flask
from flask import render_template   

app = Flask(__name__)  
@app.route('/pi')  
def hello(name=None):  
    return render_template('hello.html')
#http://192.168.1.4:5000/pi

@app.route("/ho")  
def helloa():  
    return "Hello World!"
#http://192.168.1.4:5000/ho


@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID
#http://192.168.1.4:5000/blog


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


#http://192.168.1.4:5000/hello/rob
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello_name.html', name = user)

if __name__ == "__main__":  
    app.run('0.0.0.0') 


