from firebase_admin import firestore
import hashlib

class LoginQuery:
    
    @staticmethod
    def autenticar_usuario(email, password):
        db = firestore.client()
        user_ref = db.collection('usuarios').where('email', '==', email).where('password', '==', password).get()
        if (user_ref):
            return True
        return False
    
    @staticmethod
    def existe_usuario(email):
        db = firestore.client()
        user_ref = db.collection('usuarios').where('email', '==', email).get()
        if (user_ref):
            return True
        return False
    
    @staticmethod
    def insertar_usuario(email, password):
        db = firestore.client()

        db.collection('usuarios').document(email).set({
            'email': email,
            'password': password
        })
        
    @staticmethod
    def hash_password(password):
        salt = "abcdefghijklmnopqrstuvwxyz"
        hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
        return hashed_password
    