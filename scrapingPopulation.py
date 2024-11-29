# Importation des bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL cible
url = "https://www.worldometers.info/world-population/population-by-country/"

''' En-têtes HTTP pour éviter d'être bloqué : En effet, nous avons essayé de scraper de manière 
classique et nous avons pas pu récupérer les informations, d'après nos recherches, le premiers niveau 
de protection anti-scraping est d'utiliser les headers et s'ils ne marchent pas, nous pourrons passer
au 2ème niveau en utilisant selenium,... Dans le cas présent, le "user-agent" sera récupéré en allant 
dans "inspecter" puis dans "network" '''

# En-têtes HTTP pour éviter d'être bloqué

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# Récupérer la page
response = requests.get(url, headers=HEADERS)

# Vérifier si la requête est réussie 
if response.status_code != 200:
    raise Exception(f"Erreur de requête : {response.status_code}")

# Parseur HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Scraper les données de la table
def scrape_population_data(soup):
    """
    Scrape les données de population par pays depuis la table HTML.
    """
    table = soup.find("table")  # Trouver la première table
    rows = table.find("tbody").find_all("tr")  # Récupérer toutes les lignes
    
    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) > 1:  # Ignorer les lignes sans données
            country_data = {
                "Rank": int(cols[0].text.strip()),  # Rang du pays
                "Country": cols[1].text.strip(),
                "Population (2024)": int(cols[2].text.strip().replace(",", "")),
                "Yearly Change (%)": cols[3].text.strip(),
                "Net Change": cols[4].text.strip(),
                "Density (P/Km²)": cols[5].text.strip(),
                "Land Area (Km²)": cols[6].text.strip(),
                "Migrants (net)": cols[7].text.strip(),
                "Fertility Rate": cols[8].text.strip(),
                "Median Age": cols[9].text.strip(),
                "Urban Pop (%)": cols[10].text.strip(),
                "World Share (%)": cols[11].text.strip(),
            }
            data.append(country_data)
    return data

# Exécution
data = scrape_population_data(soup)
df = pd.DataFrame(data)

# Aperçu des données
print(df.head())

# Convertir des colonnes en types numériques
df['Population (2023)'] = pd.to_numeric(df['Population (2024)'], errors='coerce')
df['Density (P/Km²)'] = pd.to_numeric(df['Density (P/Km²)'], errors='coerce')

# Remplacer les valeurs manquantes
df.fillna("XXX", inplace=True)

# Afficher les statistiques descriptives
print(df.describe())

# Sauvegarde des données dans un fichier CSV
df.to_csv("current_population_by_country2.csv", index=False)

print("Les données ont été scrappées et enregistrées dans 'current_population_by_country.csv'.")
