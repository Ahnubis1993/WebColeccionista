from flask import render_template, redirect, request, url_for
from modelos.LoginQuery import LoginQuery


class Controlador:

    @staticmethod
    def registrar_rutas(app):
        @app.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
                return redirect(url_for('mainpage'))
            return render_template('templates/Login.html')

        @app.route('/mainpage', methods=['GET', 'POST'])
        def mainpage():
            return render_template('templates/MainPage.html')
            
        @app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']
                
                login_query = LoginQuery()
                if (not login_query.autenticar_usuario(email, login_query.hash_password(password))):
                    return render_template('templates/Login.html', login_error='Credenciales incorrectas', loginEmail = email, loginPassword = password)
                return redirect(url_for('mainpage'))
        
        @app.route('/register', methods=['GET','POST'])
        def register():
            if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']
                repeated_password = request.form['repeatedPassword']
                
                login_query = LoginQuery()
                if (login_query.existe_usuario(email)):
                    return render_template('templates/Login.html', login_error='El usuario ya existe', register_error='El usuario ya existe', registerEmail=email, registerPassword=password, registerRepeatedPassword=repeated_password)
                elif (password != repeated_password):
                    return render_template('templates/Login.html', login_error='La contraseña no coincide' , register_error='La contraseña no coincide' , registerEmail=email, registerPassword=password, registerRepeatedPassword=repeated_password)
                else:
                    login_query.insertar_usuario(email, login_query.hash_password(password))
                    return render_template('templates/Login.html')

        @app.route('/mainpageMetodo')
        def mainpageSinGetYPost():
            return render_template('templates/MainPage.html')
        
    