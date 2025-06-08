from flask import Flask, render_template, request, redirect, url_for
import tweepy
from datetime import datetime

print('Lancement...')
app = Flask(__name__)
print('App créée.')

@app.route('/')
def accueil():
    print('---------------------------------------------------')
    print(f'Requête page accueil - {str(datetime.now())}')
    return render_template('Accueil.html')

@app.route('/affiche_road_trip')
def affiche_road_trip():
    print('---------------------------------------------------')
    print('Requête page affiche')
    return render_template('Affiche_road_trip.html')

#if __name__ == '__main__':
#    print('Entrée dans la boucle.')
#    app.run(debug=True, host="0.0.0.0")

#app.run(host="0.0.0.0")
#app.run(debug=True)
