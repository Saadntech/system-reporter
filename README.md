# 🔍 System Info Reporter

Un outil DevOps écrit en Python qui scanne les ressources système (CPU, RAM, disque) et identifie les processus les plus gourmands. Le tout s'exécute dans un container Docker.

&gt; 🎯 **Objectif pédagogique** : Apprendre les fondations du DevOps — Python système, containerisation, et bonnes pratiques de développement.

---

## 🚀 Fonctionnalités

- 📊 **Monitoring système** : CPU, mémoire, disque, et informations plateforme
- 🔥 **Top processus** : Identification des 5 processus les plus gourmands en CPU
- 📁 **Rapports JSON** : Export structuré avec horodatage dans `reports/`
- 🐳 **Containerisation** : Exécution identique sur n'importe quelle machine via Docker

---

## 🛠️ Stack technique

| Technologie | Usage |
|-------------|-------|
| **Python 3.12** | Langage principal |
| **psutil** | Accès aux métriques système |
| **pathlib + json** | Manipulation de fichiers et sérialisation |
| **Docker** | Containerisation et déploiement portable |
| **Git** | Versioning et collaboration |

---

## 📦 Installation

### Prérequis
- Python 3.10+
- Docker
- Git

### Local

```bash
# Cloner le repo
git clone https://github.com/TON_USER/system-reporter.git
cd system-reporter

# Environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Dépendances
pip install -r requirements.txt

# Lancer
python src/main.py
