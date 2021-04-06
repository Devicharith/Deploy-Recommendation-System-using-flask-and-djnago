from flask import Flask, request, render_template
from recommendation_system import Similar_Movies
import pickle
import pandas as pd

# create an instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('rec.html')

# Set the URL for the Function
@app.route('/movies' , methods = ["POST"])
def TOP10():
    if request.method == 'POST':
        name = request.form['movie']
        cosine = pickle.load(open('cos_sim.pickle','rb'))
        ans = Similar_Movies(name.lower(),cosine)
        if isinstance(ans,list): return render_template('rec.html', recommend = ans)
        else: return render_template('rec.html', absent = ans)

if __name__ == '__main__':
    app.run(debug=True)
