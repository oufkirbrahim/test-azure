# Azure Function - Contrat PDF Parser

Cette Azure Function accepte deux fichiers PDF (contrat et mandat), en extrait les champs clés à l'aide d'OpenAI et retourne un JSON.

## Utilisation
Envoyer une requête POST à l'endpoint avec :
- `contrat` : le fichier PDF du contrat
- `mandat` : le fichier PDF du mandat

## Déploiement GitHub → Azure
Configurer GitHub Actions avec le secret `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` pour un déploiement automatique.
