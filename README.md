# Projet Formation - Gestion du processus de formation des employés

Projet de fin de module en **Modélisation UML** : conception et réalisation d'une application web permettant de modéliser puis d'informatiser une partie du processus de formation des employés d'une entreprise.

L'application sert de support concret aux modèles UML du projet : acteurs, cas d'utilisation, classes métier, enchaînements de traitement, états d'une demande et règles de gestion.

## Objectif du projet

Une entreprise souhaite gérer le processus de formation de ses employés. Le processus commence lorsqu'un employé transmet une demande de formation au responsable formation. L'employé peut consulter le catalogue des formations proposées par les organismes agréés par l'entreprise avant de formuler sa demande.

Le responsable formation instruit ensuite la demande. Il peut donner son accord ou refuser la demande. En cas d'accord, il recherche une formation adéquate dans le catalogue qu'il tient à jour, informe l'employé du contenu de la formation, lui propose les prochaines sessions disponibles, puis procède à l'inscription auprès de l'organisme de formation concerné.

Si l'employé a un empêchement, il doit avertir rapidement le responsable formation afin que celui-ci demande l'annulation de l'inscription. A la fin de la formation, l'employé transmet une appréciation sur le stage suivi ainsi qu'un document attestant sa présence.

Ce projet met donc en pratique une démarche de modélisation orientée objet, depuis l'analyse du cahier des charges jusqu'à l'implémentation d'un modèle relationnel avec Flask et SQLAlchemy.

## Cahier des charges initial

Le système à modéliser couvre les actions suivantes :

- réception d'une demande de formation formulée par un employé ;
- consultation possible du catalogue des formations agréées ;
- instruction de la demande par le responsable formation ;
- notification de l'accord ou du refus à l'employé ;
- recherche d'une formation adéquate en cas d'accord ;
- information de l'employé sur le contenu de la formation ;
- proposition des prochaines sessions disponibles ;
- choix d'une session par l'employé ;
- inscription à la session retenue auprès de l'organisme concerné ;
- annulation possible en cas d'empêchement ;
- transmission d'une appréciation et d'une attestation de présence à la fin de la formation.

## Fonctionnalités principales

### Espace employé

- Création de compte et connexion sécurisée.
- Consultation du catalogue des formations disponibles.
- Soumission d'une demande de formation.
- Suivi de l'état des demandes : en attente, approuvée ou rejetée.
- Choix d'une session disponible après validation.
- Annulation d'une inscription en cas d'empêchement.
- Marquage d'une formation comme terminée.
- Envoi d'une appréciation avec possibilité de joindre une attestation ou un fichier justificatif.

### Espace responsable formation

- Tableau de bord global des demandes, factures, formations, sessions et utilisateurs.
- Création ou réinitialisation de comptes employés/managers.
- Validation ou rejet des demandes de formation.
- Recherche et affectation d'une formation adéquate à une demande.
- Inscription d'un employé à une session.
- Annulation d'une inscription.
- Ajout de formations au catalogue.
- Création de sessions avec date, lieu et capacité.
- Vérification des factures liées aux formations.
- Statistiques simples sur les demandes en attente, approuvées et rejetées.

## Acteurs UML

- **Employé** : consulte le catalogue, crée une demande, suit son inscription, choisit une session et transmet une appréciation.
- **Responsable formation** : instruit les demandes, tient à jour le catalogue, propose les sessions, inscrit les employés et gère les annulations.
- **Organisme de formation agréé** : propose des formations et des sessions, reçoit les inscriptions ou les demandes d'annulation.
- **Système** : contrôle les droits d'accès, applique les règles métier, persiste les données et protège les formulaires.

## Règles métier implémentées

- Un utilisateur possède un rôle : `EMPLOYEE` ou `MANAGER`.
- Un employé ne peut accéder qu'aux pages de l'espace employé.
- Un responsable formation ne peut accéder qu'aux pages de gestion.
- Une demande de formation commence avec le statut `PENDING`.
- Le responsable formation peut passer une demande à `APPROVED` ou `REJECTED`.
- En cas de refus, le processus s'arrête après information de l'employé.
- En cas d'accord, une session doit être choisie avant l'inscription définitive.
- Une session ne peut pas dépasser sa capacité maximale.
- Une demande déjà inscrite ne peut pas être inscrite une deuxième fois.
- Une inscription ne peut être terminée que si elle est encore active (`REGISTERED`).
- Les fichiers justificatifs acceptés sont limités aux extensions `pdf`, `png`, `jpg` et `jpeg`.

## Modèle de données

Les principales classes métier sont :

- `User` : représente un utilisateur avec nom, email, mot de passe hashé et rôle.
- `Training` : représente une formation du catalogue, associée à un organisme.
- `Session` : représente une session planifiée pour une formation.
- `TrainingRequest` : représente une demande de formation créée par un employé.
- `Enrollment` : représente l'inscription d'un employé à une session.
- `Feedback` : représente l'appréciation d'un employé après une formation, avec document justificatif optionnel.
- `Invoice` : représente une facture associée à une formation.

Relations principales :

- Un `User` employé peut avoir plusieurs `TrainingRequest`.
- Une `Training` peut avoir plusieurs `Session`, `Feedback`, `Invoice` et `TrainingRequest`.
- Une `TrainingRequest` peut donner lieu à une seule `Enrollment`.
- Une `Session` peut recevoir plusieurs `Enrollment` dans la limite de sa capacité.

## Technologies utilisées

- **Python**
- **Flask** pour l'application web.
- **Flask-SQLAlchemy** pour l'ORM et la persistance.
- **SQLite** comme base de données locale.
- **Flask-Login** pour l'authentification.
- **Flask-WTF** pour les formulaires et la protection CSRF.
- **Werkzeug** pour le hashage des mots de passe et la sécurisation des fichiers.
- **HTML / CSS / JavaScript** pour l'interface utilisateur.

## Structure du projet

```text
Projet-Formation-L3/
├── app/
│   ├── forms/              # Formulaires WTForms
│   ├── models/             # Modèles SQLAlchemy
│   ├── routes/             # Routes Flask par espace fonctionnel
│   ├── services/           # Logique métier du workflow
│   ├── static/             # Fichiers CSS et JavaScript
│   ├── templates/          # Pages HTML Jinja
│   ├── utils/              # Sécurité, upload et données de démonstration
│   └── __init__.py         # Factory Flask et initialisation des extensions
├── uploads/                # Fichiers envoyés par les utilisateurs
├── app.db                  # Base SQLite locale
├── config.py               # Configuration de l'application
├── requirements.txt        # Dépendances Python
├── run.py                  # Point d'entrée
└── README.md
```

## Installation

Cloner ou ouvrir le dossier du projet, puis installer les dépendances dans un environnement virtuel.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Sur macOS ou Linux, l'activation de l'environnement virtuel se fait plutôt avec :

```bash
source .venv/bin/activate
```

## Lancement

```bash
python run.py
```

L'application démarre en mode debug et devient accessible à l'adresse :

```text
http://127.0.0.1:5000
```

Au démarrage, Flask crée automatiquement les tables de la base de données si elles n'existent pas. Des données de démonstration sont également insérées si la base est vide.

## Déploiement sur Vercel

Le projet contient une configuration Vercel prête à l'emploi :

- `api/index.py` expose l'application Flask comme fonction serverless ;
- `vercel.json` redirige toutes les routes vers cette fonction ;
- `pyproject.toml` indique explicitement à Vercel le point d'entrée Flask ;
- `.vercelignore` exclut les fichiers locaux inutiles au déploiement ;
- `config.py` utilise automatiquement `/tmp/app.db` et `/tmp/uploads` lorsque l'application tourne sur Vercel.

Commandes possibles :

```bash
npm install -g vercel
vercel
```

Pour un déploiement de production :

```bash
vercel --prod
```

Sur Vercel, la base SQLite stockée dans `/tmp` est temporaire. Elle convient pour une démonstration, mais pas pour une vraie application persistante. Pour conserver les données durablement, il faut définir une variable `DATABASE_URL` vers une base externe compatible SQLAlchemy.

## Comptes de démonstration

| Rôle | Email | Mot de passe |
| --- | --- | --- |
| Responsable formation | `manager@company.com` | `password` |
| Employé | `employee@company.com` | `password` |

## Données de démonstration

La base initiale contient notamment :

- deux utilisateurs : un responsable formation et un employé ;
- deux formations : `Python Avancé` et `Gestion de Projet` ;
- trois sessions de formation ;
- une facture en attente de vérification.

## Configuration

Les valeurs importantes sont définies dans `config.py`.

| Variable | Description | Valeur par défaut |
| --- | --- | --- |
| `SECRET_KEY` | Clé utilisée par Flask et Flask-WTF | `dev-secret-key` |
| `DATABASE_URL` | URL de connexion à la base de données | `sqlite:///app.db` |
| `UPLOAD_FOLDER` | Dossier de stockage des fichiers envoyés | `uploads/` |

Exemple :

```bash
set SECRET_KEY=ma-cle-secrete
set DATABASE_URL=sqlite:///app.db
python run.py
```

## Parcours utilisateur recommandé

1. Se connecter en responsable formation avec `manager@company.com`.
2. Ajouter ou mettre à jour une formation et ses sessions.
3. Se déconnecter puis se connecter en employé avec `employee@company.com`.
4. Consulter le catalogue et soumettre une demande de formation.
5. Revenir en responsable formation pour instruire la demande.
6. Approuver ou refuser la demande.
7. En cas d'accord, inscrire l'employé à une session ou laisser l'employé choisir sa session.
8. En cas d'empêchement, annuler l'inscription.
9. Revenir en employé, terminer la formation et envoyer une appréciation avec attestation.

## Apport pour la Modélisation UML

Ce projet permet d'illustrer les diagrammes suivants :

- **Diagramme de cas d'utilisation** : interactions entre employé, responsable formation, organisme agréé et système.
- **Diagramme de classes** : structure des entités `User`, `Training`, `Session`, `TrainingRequest`, `Enrollment`, `Feedback` et `Invoice`.
- **Diagramme de séquence** : scénario de demande, instruction, accord, choix de session et inscription.
- **Diagramme d'activité** : cycle complet d'une demande de formation, avec les branches accord/refus et annulation.
- **Diagramme d'états** : évolution d'une demande (`PENDING`, `APPROVED`, `REJECTED`) et d'une inscription (`REGISTERED`, `CANCELLED`, `COMPLETED`).

## Limites et améliorations possibles

- Ajouter des tests automatisés pour les routes et les services métier.
- Ajouter une interface dédiée à la consultation des appréciations par le responsable formation.
- Modéliser les organismes agréés dans une table séparée au lieu de les stocker comme un champ de formation.
- Générer automatiquement les factures depuis les inscriptions.
- Ajouter des notifications email lors de la validation ou du rejet d'une demande.
- Renforcer la configuration de production : clé secrète obligatoire, serveur WSGI et base de données externe.
- Ajouter un dossier `docs/` contenant les diagrammes UML exportés en image ou en PDF.

## Auteur

Projet réalisé dans le cadre du module **Modélisation UML**.

