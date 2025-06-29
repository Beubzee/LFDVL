from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import tweepy
from datetime import datetime
import os

print('Lancement...')
app = Flask(__name__)
print('App créée.')

@app.route("/robots.txt")
def robots():
    print('\n---------------------------------------------------')
    print(f'Requête robots.txt - {str(datetime.now())}')
    return send_from_directory("static", "robots.txt")

@app.route("/sitemap.xml")
def sitemap():
    print('\n---------------------------------------------------')
    print(f'Requête sitemap.xml - {str(datetime.now())}')
    return send_from_directory("static", "sitemap.xml")

@app.route('/', methods=['GET', 'POST'])
def accueil():
    print('\n---------------------------------------------------')
    print(f'Requête page accueil - {str(datetime.now())}')
    if request.method == 'POST':
        donnee = request.form
        son_dl = donnee.get('son')
        print(f'Formulaire entrant : {donnee}')
        if son_dl == 'HEAD TO THE ROAD':
            print('Métode POST -- téléchargment HEAD TO THE ROAD')
            return send_from_directory('static/music', 'HEAD TO THE ROAD - Les Fous Du Van Lent.mp3', as_attachment=True)
        elif son_dl == 'Wakey Wakey':
            print('Métode POST -- téléchargment Wakey Wakey')
            return send_from_directory('static/music', 'Wakey Wakey - Les Fous Du Van Lent.mp3', as_attachment=True)
    return render_template('Accueil.html')

@app.route('/affiche_road_trip')
def affiche_road_trip():
    print('\n---------------------------------------------------')
    print(f'Requête page affiche - {str(datetime.now())}')
    return render_template('Affiche_road_trip.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
