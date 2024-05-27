# Projet Stage 2024 - Extraction de Données via OCR


## Installation

### Prérequis
- Python 3.6 ou supérieur
- `pip` doit être installé

### Étapes d'installation
1. Clonez le dépôt de ce projet sur votre machine locale :
    ```bash
    git clone <URL_DE_VOTRE_DÉPÔT>
    cd <NOM_DU_RÉPERTOIRE_DU_PROJET>
    ```

2. Installez les dépendances nécessaires à partir du fichier `requirements.txt` :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation
1. À partir de l'image `Genova.png` dans le dossier `Data`.

2. Exécutez le script principal pour effectuer l'extraction de texte :
    ```bash
    python main.py
    ```

3. Les résultats seront sauvegardés dans le fichier `TextOutput/textOutputResult.json`.


### Explications des Fichiers
- `main.py` : Script principal pour l'extraction de texte et la sauvegarde des résultats.
- `utils/ocr.py` : Contient la fonction pour effectuer l'OCR à l'aide de EasyOCR.
- `utils/image.py` : Contient les fonctions pour charger et prétraiter l'image.
- `data/Genova.png` : Image d'entrée contenant les noms des villes à extraire.
- `TextOutput/textOutputResult.json` : Fichier de sortie contenant les résultats de l'extraction de texte.

## Dépendances
Le fichier `requirements.txt` contient les dépendances nécessaires pour ce projet :
easyocr
opencv-python
numpy
pillow
