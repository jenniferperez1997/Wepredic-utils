import requests
import json
import csv

# token d'accès de l'API LinkedIn
access_token = "yof59ZyMk4fFVAET"

# mot-clé de recherche
search_query = "Thomas_Darde"

# URL de recherche
url = "https://api.linkedin.com/v2/search?q=" + search_query + "&count=10&start=0&sort=best"

# En-têtes de demande avec le token d'accès
headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}

# Faire une demande GET à l'API LinkedIn
response = requests.get(url, headers=headers)

# Extraire les résultats de la réponse
results = json.loads(response.text)

# Extraire les informations pertinentes et les stocker dans un tableau
data = []
print(results)
for result in results["elements"]:
    name = result.get("title")
    email = result.get("emailAddress")
    position = result.get("headline")
    company = result.get("orgainzation")
    data.append([name, email, position, company])

# Stocker les informations dans un fichier CSV
with open("informations.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nom", "Adresse e-mail", "Poste", "Entreprise"])
    writer.writerows(data)
