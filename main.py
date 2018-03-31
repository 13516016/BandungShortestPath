from flask import Flask
from flask import redirect, url_for, request, render_template
import webview
import sys
import threading

app = Flask(__name__)
debug = True


@app.route('/get-shortest-path/', methods = ['POST'])
def getShortestPath():
	if request.method == 'POST':
		content = request.get_json()

		source = content['source_point']
		destination = content['destination_point']
		adjacency_matrix = content['adjacency_matrix']
		distance_matrix = content['distance_matrix']
		
		if (debug):
			print(source)
			print(destination)
			
			for adj in adjacency_matrix:
				print(adj)	

			print()

			for distance in distance_matrix:
				print(distance)

		# IMPLEMENT IN **a_star.py** file
		
		# solution = a_star(source,destination,adjacency_matrix, distance_matrix)
		# return JSON.parse(solution)
		
		return "NICE"


@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect( url_for('success',name = user) )
   else:
   	return render_template('index.html')

if __name__ =='__main__':
    app.debug=debug
    app.run()
	
	
	