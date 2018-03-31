from flask import Flask
from flask import redirect, url_for, request, render_template
import webview
import sys
import threading

app = Flask(__name__)


@app.route('/get-shortest-path/', methods = ['POST','GET'])
def getShortestPath():
	if request.method == 'POST':
		content = request.get_json()
		
		adjacency_matrix = content['adjacency_matrix']
		distance_matrix = content['distance_matrix']



	return "OK"


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
	
	
	