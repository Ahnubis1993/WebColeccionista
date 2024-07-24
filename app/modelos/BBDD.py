import firebase_admin
from firebase_admin import credentials, db
from flask import render_template


class BBDD:
    def __init__(self):
        # Carga el certificado
        self.cred = credentials.Certificate("modelos/bbddgustavo-firebase-adminsdk-j9f9g-51fb5cfdf2.json")
        firebase_admin.initialize_app(self.cred)
