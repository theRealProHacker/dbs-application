# dbs-application
A simple full-stack application to show the power of sql

# How to run

Assuming you have Python installed on your computer

## Windows

```shell
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py app.py
```

## Unix

```shell
py -m venv venv
venv\Lib\activate
pip install -r requirements.txt
py app.py
```

## Datenbank 

1. Insalliere PostgreSQL
2. Setze einen Server auf
3. Erstelle neue Datenbank
4. Importiere die 'biketheft_berlin.sql' Datenbank mit "Restore"
5. Ändere falls notwendig den Username, Passwort, Port und Name der Datenbank in der db.py Datei:  
    engine = sa.create_engine('postgresql://USERNAME:PASSWORT@localhost:PORT/NAME_DER_DATENBANK')