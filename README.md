# mail-header-cutomizer
Script whose purpose is to send e-mails by freely changing the headers, making it possible to test the security of a domain, and to check DMARC records.

### [EN]
installation path:

run script python_and_pip_install.ps1, which automatically installs python and pip, as well as the python libraries needed to run the program.

Before taking any action with the script, you MUST enter your mail server identifiers in line 68 and 69 ("sender_email" and "password" variables). Save the file and close.

You then have two choices:

Either run the script in python:
```bash
python sender.py
```
Or create a Windows executable:
```bash
pyinstaller --onefile sender.py
```
Once finished, the executable file is located in the "dist" folder.


### [FR]
chemin d'installaion:

exécuter le script python_and_pip_install.ps1, qui va installer automatiquement python et pip, ainsi que les bibliotèques python nécessaires pour le focntionnement du programme.

Avant toute action avec le script, il FAUT mettre vos identifiants de serveur mail dans les variables lignes 68 et 69 (variables "sender_email" et "password"). Sauvegardez le fichier et fermez.

Ensuite, vous avez deux choix:

Soit vous exécutez le script en python:
```bash
python sender.py
```
Soit vous voulez créer un exécutable Windows:
```bash
pyinstaller --onefile sender.py
```
Dès que c'est fini, le fichier exécutable est localisé dans le dossier "dist".

