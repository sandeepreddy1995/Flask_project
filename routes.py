# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:29:18 2018

@author: sandeep
"""

from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")

if __name__=='__main__':
    app.run(debug=True)