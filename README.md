# mail-header-cutomizer
Script whose purpose is to send e-mails by freely changing the headers, making it possible to test the security of a domain, and to check DMARC records.

## [EN]

### Installation path:

Before taking any action with the script, you MUST enter your SMTP Server and your mail server identifiers.
![image](https://github.com/ThomasDuke/mail-header-customizer/assets/51382343/bacabbd8-95cf-4d01-8460-7d338783433c)

Save the file and close.

You will also need to install python libraries:

```
pip install -r requirements.txt
```

You then have two choices:

Either run the script in python:
```
python sender.py
```
Or create a Windows executable:
```
pyinstaller --onefile sender.py
```
Once finished, the executable file is located in the "dist" folder.

## A few things you need to know

Once you've registered your SMTP server credentials in the source file, you're ready to start sending e-mails.

First of all, the DMARC Check feature doesn't require any SMTP server registration in the code, so you can use this tool at any time.

To send mail from a domain you may or may not own, the IP address or DNS resolution of your mail server must be entered in the SPF record. If this is not the case (in the situation where you wish to spoof a domain), then the domain must have either no DMARC record, or a record with a permissive policy ("p= none"). Otherwise, if the registration has a restrictive policy ("p=quarantine" or "p=reject"), your e-mail will be unable to reach the recipient.
The DMARC Check feature would therefore be a quick way of finding out whether or not your e-mail would be delivered.

## How to use the script?

![2023-12-06_17h16_21](https://github.com/ThomasDuke/mail-header-customizer/assets/51382343/a74685b4-5f30-43ad-85c9-e60bb322ad5d)


### From :
Enter the e-mail address which will be the source of the e-mail. As this address will be hard-coded in the e-mail headers, you can either enter an e-mail address only, or in the format ```Thomas <test@example.com>```. In the former case, the recipient will only see "test" as the source username, whereas in the latter, the username will be "Thomas".
For DMARC Check functionality, you need to enter an address, not just a domain name.

### To :
 As you can see, you need to enter the e-mail recipient.

### Subject:
As you may have guessed, the subject of the e-mail.

### Text/HTML selection :
#### Text:
You write a classic message, as if you were sending an e-mail from an Outlook client or similar.

#### HTML:
You pre-configure your e-mail in HTML, if you wish for example to format it with particular tags, insert images etc... Note that I've only tested with basic text, but you can try with image tags.
Then enter your message.

### Option Add Headers :
This option lets you add special headers to your e-mail. For example, if you want the e-mail to look as if it's being sent from an Outlook client:
Enter "X-Mailer: Outlook Client".
Here's a list of headers you can add to your e-mail (with examples):
```
MIME-Version: 1.0
X-Mailer: Outlook Client
X-Spam-Flag: YES/NO
X-Spam-Status: No hits=-1.2 required=4.7
X-Country: code=US country="United States" ip=0.0.0.0
X-LangGuess: English
X-Verify-Helo: -ERR missmatch: mail.test.com->0.0.0.0->.fake_nodots
X-Dmarc: reject/quarantine/none
```
For more headers, please refer to this link: https://www.iana.org/assignments/message-headers/message-headers.xhtml

## [FR]

### Chemin d'installaion:

Avant toute action avec le script, vous DEVEZ enregistrer votre serveur SMTP et les identifiants.
![image](https://github.com/ThomasDuke/mail-header-customizer/assets/51382343/bacabbd8-95cf-4d01-8460-7d338783433c)

Vous aurez besoin d'installer les bibliothèques python:

```
pip install -r requirements.txt
```

Ensuite, vous avez deux choix:

Soit vous exécutez le script en python:
```
python sender.py
```
Soit vous voulez créer un exécutable Windows:
```
pyinstaller --onefile sender.py
```
Dès que c'est fini, le fichier exécutable est localisé dans le dossier "dist".

## Quelques informations à connaitre

Dès que vous avez enregistré vos identifiants de serveur SMTP dans le fichier source, vous êtes prêts pour envoyer des mails.

Tout d’abord, sachez que la fonctionnalité DMARC Check ne nécessite d’aucun enregistrement de serveur SMTP dans le code, vous pouvez donc utiliser cet outil n’importe quand.

Pour envoyer des mails depuis un domaine vous appartenant ou pas, il faut que l’adresse IP ou bien la résolution DNS de votre serveur de mail soit inscrite dans l’enregistrement SPF. S’il n’est pas le cas (dans la situation où vous souhaitez usurper un domaine), il faut donc que le domaine ait soit aucune enregistrement DMARC, soit un enregistrement avec une politique permissive (« p= none »). Sinon, si l’enregistrement possède une politique restrictive (« p=quarantine » ou bien « p=reject »), votre mail sera dans l’incapacité d’être reçu à votre destinataire.
La fonctionnalité DMARC Check serait donc un moyen rapide de savoir si votre mail partirait ou non.

## Comment utiliser le script ?
 
![2023-12-06_17h16_21](https://github.com/ThomasDuke/mail-header-customizer/assets/51382343/01d6cf9a-cc33-4575-9d85-2554c076e443)

### From :
Entrez l’adresse mail qui sera en source du mail. Etant donné que cette adresse sera inscrite en dur dans les en-têtes du mail, vous pouvez soit entrer uniquement une adresse mail, soit sous un format ```Thomas <test@example.com>```. Dans le premier cas, le destinataire verra en nom d’utilisateur source uniquement « test », alors que dans le second cas, le nom d’utilisateur sera « Thomas ».
Pour la fonctionnalité DMARC Check, il faut entrer une adresse et non seulement un nom de domaine.

### To :
 Vous l’aurez compris, il faut entrer le destinataire du mail.

### Subject :
Vous l’aurez compris aussi, le sujet du mail.

### Sélection Text/HTML :
#### Text :
Vous écrivez un message classique, comme si vous envoyiez un mail depuis un client Outlook ou autre.

#### HTML :
Vous préconfigurez votre mail en HTML, si vous souhaitez par exemple formater avec des balises particulières, introduire des images etc… A savoir que j’ai testé qu’avec tu texte basique, mais vous pouvez essayer avec des balises d’image.
Vous entrez ensuite votre message.

### Option Add Headers :
Cette option permet d’ajouter des en-têtes particulières dans votre mail. Par exemple, vous voulez faire croire que le mail est envoyé depuis un client Outlook :
Entrez « X-Mailer: Outlook Client »
Voici une liste d’en-têtes que vous pouvez ajouter dans votre mail (avec des exemples en valeur):
```
MIME-Version: 1.0
X-Mailer: Outlook Client
X-Spam-Flag: YES/NO
X-Spam-Status: No hits=-1.2 required=4.7
X-Country: code=US country="United States" ip=0.0.0.0
X-LangGuess: English
X-Verify-Helo: -ERR missmatch: mail.test.com->0.0.0.0->.fake_nodots
X-Dmarc: reject/quarantine/none
```
Pour plus d'en-têtes, veuillez vous référer à ce lien: https://www.iana.org/assignments/message-headers/message-headers.xhtml
