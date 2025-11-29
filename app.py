from flask import Flask, render_template, url_for, abort
import os
from threading import Timer

app = Flask(__name__)

@app.route('/')
def index():
    model_dir = app.static_folder
    models = sorted([f for f in os.listdir(model_dir) if f.endswith('.glb')])
    return render_template('index.html', models=models)

@app.route('/view/<model_name>')
def view(model_name):
    model_path = os.path.join(app.static_folder, model_name)
    if not os.path.isfile(model_path) or not model_name.endswith('.glb'):
        abort(404)
    return render_template('view.html', model_name=model_name)

@app.route('/home')
def home():
    model_path = os.path.join(app.static_folder)
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
