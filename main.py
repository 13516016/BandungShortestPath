from flask import Flask
from flask import redirect, url_for, request, render_template
import webview
import sys
import threading

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
	amazing_list = [i**2 for i in range(1,20)]
	return render_template('success.html', name=name, list=amazing_list)

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect( url_for('success',name = user) )
   else:
   	return render_template('index.html')


if __name__ =='__main__':
    app.debug=True
    app.run()
	
	
	