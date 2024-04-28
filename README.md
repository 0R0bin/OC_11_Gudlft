# eleventhProject
Pour installer ce projet, téléchargez ou clonez le repository à l'aide du lien suivant
```
https://github.com/0R0bin/OC_11_Gudlft.git
```
Placez vous dans le dossier du repository, puis, exectuez les commandes suivantes :
Sous Unix/macOS
```
python3 -m venv env
```
```
source env/bin/activate
```
Sous Windows
```
py -m venv env
```
```
.\env\Scripts\activate
```
Ensuite, installez les packages nécessaires :
```
pip install -r requirements.txt
```
Pour exécuter le projet
```
flask run
```
Rendez-vous ensuite sur votre navigateur à l'adresse suivante :
```
http://127.0.0.1:5000
Pour effectuer les tests à l'aide de pytest
Sous Unix/MacOS
```
python3 -m pytest .\tests\
```
Sous Windows
```
python -m pytest .\tests\
```
Pour avoir la couverture de test
```
coverage run -m pytest tests
coverage report
```
Pour lancer locust, avec le serveur Flask lancé exécutez la commande suivante
Unix/MacOS : 
```
python3 -m locust
```
Windows : 
```
python -m locust
```
Vous êtez prêt !
