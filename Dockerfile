# Verwende ein offizielles Python-Image als Basis
FROM animcogn/face_recognition

# Setze das Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere die Anwendungsdateien in das Arbeitsverzeichnis
COPY trainig_script.py /app/
COPY images /app/images
COPY test /app/test
RUN mkdir /app/result

# Installiere die erforderlichen Python-Bibliotheken
RUN pip install face_recognition
RUN ls -r /
# Führe das Gesichtserkennungsskript aus
CMD ["python", "trainig_script.py"]
