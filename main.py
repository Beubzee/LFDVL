from flask import Flask, render_template, request, redirect, url_for
import tweepy
from datetime import datetime
import os

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

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
