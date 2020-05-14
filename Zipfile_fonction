from zipfile import ZipFile

# spécifiant le nom du fichier zip
file = "archive.zip"

# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip:
    # afficher tout le contenu du fichier zip
    zip.printdir()

    # extraire tous les fichiers
    print('extraction...')
    zip.extractall()
    print('Terminé!')
