# Verwendung
Per Dockerfile kann ein Docker Image erstellt werden
```console
docker build -t icaldownload .
```

Ausführung des Docker Images
```console
docker run -d --name icaldownload -p 8000:80 icaldownload
```

## Mappings
Standard-Port der Anwedung 8000