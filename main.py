from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import threading

app = Flask(__name__)
CORS(app)

# Charger les données à partir du fichier JSON initial
with open('apps.json', 'r', encoding='utf-8') as file:
    apps = json.load(file)

@app.route('/api/apps')
@app.route('/api/apps')
def get_apps():
    category = request.args.get('category')  # Récupérer la catégorie de la requête
    if category and category.lower() != 'all':  # Vérifier si une catégorie est spécifiée et n'est pas 'all'
        filtered_apps = [app for app in apps if app.get('category') == category]
        return jsonify(filtered_apps)
    else:
        return jsonify(apps)


def update_apps():
    global apps
    # Charger les nouvelles données à partir du fichier JSON
    with open('apps.json', 'r', encoding='utf-8') as file:
        new_apps = json.load(file)
    # Mettre à jour les données globales
    apps = new_apps
    # Planifier la prochaine mise à jour dans 5 secondes
    threading.Timer(5, update_apps).start()

# Lancer la mise à jour initiale des applications
update_apps()

if __name__ == '__main__':
    app.run(debug=True)
