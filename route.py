from flask import Flask,render_template,request,user
from module import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to my pokemon app'


@app.route('/pokemon',methods=['get','post'])
def pokemon():
    if requests.method == 'post':
        name = requests.form['name']
        return render_template ('pokemon.html', pokemon = pokemon_data)
    return render_template('index.html')
url = f'https://pokeapi.co/'
response = requests.get('https://pokeapi.co/')
pokemon_data = response.json()
# return render_template ('pokemon.html', pokemon = pokemon_data)
# return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
