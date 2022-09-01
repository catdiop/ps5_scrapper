# Push image on Gcloud

gcloud auth configure-docker \
    europe-west1-docker.pkg.dev
docker tag scrappervenv:latest europe-west1-docker.pkg.dev/ps5scrapper/test/scrappervenv:0.0.1
docker push europe-west1-docker.pkg.dev/ps5scrapper/test/scrappervenv:0.0.1


europe-west1-docker.pkg.dev : l'emplacement régional ou multirégional du dépôt où l'image est stockée