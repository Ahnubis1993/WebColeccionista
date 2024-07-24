from flask import render_template, request, redirect
from modelos.CartaQuery import CartaQuery

class ControladorCartas:
    @staticmethod
    def rutasCartas(app):

        # Para que te lleve al html TemplateCartas
        @app.route('/TemplateCartas')
        def templateCartasPaginaPrincipal():
            return render_template('templates/templateCartas/TemplateCartas.html')

        # Para que te lleve al html TemplateCartas
        @app.route('/TemplateCartas/AltaCarta')
        def templateCartasAltaPagina():
            return render_template('templates/templateCartas/TemplateCartasAlta.html')

        # Ejecuta Query en html TemplateCartasAlta. Si ya existe, regresa a la misma pagina
        # y sale mensaje ya existe.
        @app.route('/TemplateCartas/AltaCartaQuery', methods=['POST'])
        def templateCartasAlta():
            if request.method == 'POST':
                # Obtener los datos del formulario
                nombre = request.form['nombre']
                juego = request.form['juego']
                coleccion = request.form['coleccion']
                numero = int(request.form['numero'])
                precio = float(request.form['precio'])

                # Verificar si se ha marcado la casilla de confirmación
                if 'check' in request.form:
                    # Intentar insertar la carta
                    resultado = CartaQuery.insertar_carta(nombre, juego, coleccion, numero, precio)
                    if resultado == "Carta insertada exitosamente":
                        # Si la inserción es exitosa, redireccionar a la página de éxito
                        return redirect('/TemplateCartas')
                    else:
                        # Si ya existe una carta con el mismo nombre, mostrar un mensaje de error al usuario
                        return render_template('templates/templateCartas/TemplateCartasAlta.html', mensaje=resultado)


        # Para que te lleve al html TemplateCartasError
        @app.route('/TemplateCartas/Baja')
        def bajaCarta():
            cartas_encontradas = CartaQuery.buscar_todas_cartas()
            if not cartas_encontradas:  # Si no se encontraron cartas
                return render_template('templates/templateCartas/TemplateCartasError.html')
            else:
                return render_template('templates/templateCartas/TemplateCartasBaja.html')

        @app.route('/TemplateCartas/BajaBusqueda', methods=['POST'])
        def bajaBusqueda():
            if request.method == 'POST':
                # Obtener el valor de búsqueda del formulario
                valor = request.form['valor']

                # Ejecutar la búsqueda por valor
                cartas_encontradas = CartaQuery.buscar_por_valor(valor)

                # Renderizar el resultado en el template correspondiente
                return render_template('templates/templateCartas/TemplateCartasBaja.html',
                                       cartas=cartas_encontradas)

        @app.route('/TemplateCartas/Borrar/<nombre_carta>', methods=['POST'])
        def borrarCarta(nombre_carta):
            if request.method == 'POST':
                # No es necesario obtener el nombre de la carta del formulario, ya que está incluido en la URL

                # Intentar borrar la carta por su nombre
                CartaQuery.borrar_carta_por_nombre(nombre_carta)

                # Redirigir a la página principal o a alguna otra página de confirmación
                return render_template('templates/templateCartas/TemplateCartas.html')

        # Para que te lleve al html TemplateCartasBuscarApi
        @app.route('/TemplateCartas/TemplateCartasBuscarApi')
        def templateCartasBuscarTodo():
            return render_template('templates/templateCartas/TemplateCartasBuscarApi.html')

        # Para que te lleve al html TemplateCartasBuscar
        @app.route('/TemplateCartas/Buscar')
        def templateCartasBuscar():
            return render_template('templates/templateCartas/TemplateCartasBuscar.html')

        # Ejecuta Query buscar_por_valor desde html TemplateCartasBuscar
        @app.route('/TemplateCartas/BuscarQuery', methods=['POST'])
        def templateCartasBuscarQuery():
            if request.method == 'POST':
                # Obtener el valor de búsqueda del formulario
                valor = request.form['valor']

                # Ejecutar la búsqueda por valor
                cartas_encontradas = CartaQuery.buscar_por_valor(valor)

                # Renderizar el resultado en el template correspondiente
                return render_template('templates/templateCartas/TemplateCartasBuscar.html',
                                       cartas=cartas_encontradas)

        @app.route('/TemplateCartas/MostrarTodos', methods=['GET'])
        def templateCartasMostrarTodos():
            # Llamar al método buscar_todas_cartas de tu clase
            cartas = CartaQuery.buscar_todas_cartas()
            return render_template('templates/templateCartas/TemplateCartasMostrar.html', cartas=cartas)


        @app.route('/TemplateCartas/Modificar')
        def templateCartasModificar():
            return render_template('templates/templateCartas/TemplateCartasModificar.html')


        @app.route('/TemplateCartas/ModificarBusqueda', methods=['POST'])
        def modificarBusqueda():
            if request.method == 'POST':
                # Obtener el valor de búsqueda del formulario
                valor = request.form['valor']

                # Ejecutar la búsqueda por valor
                cartas_encontradas = CartaQuery.buscar_por_valor(valor)

                # Renderizar el resultado en el template correspondiente
                return render_template('templates/templateCartas/TemplateCartasModificar.html',
                                       cartas=cartas_encontradas)

        @app.route('/TemplateCartas/ModificarQuery', methods=['POST'])
        def modificarCarta():
            if request.method == 'POST':
                try:
                    # Obtener los datos del formulario
                    nombre_actual = request.form['nombre_actual']
                    nuevo_nombre = request.form['nuevo_nombre']
                    nuevo_juego = request.form['nuevo_juego']
                    nueva_coleccion = request.form['nueva_coleccion']
                    nuevo_numero = int(request.form['nuevo_numero'])
                    nuevo_precio = float(request.form['nuevo_precio'])

                    # Modificar la carta
                    resultado = CartaQuery.modificar_carta_por_nombre(nombre_actual, nuevo_nombre, nuevo_juego,
                                                                      nueva_coleccion, nuevo_numero, nuevo_precio)

                    if resultado == "Carta modificada exitosamente":
                        # Si la modificación es exitosa, redireccionar a la página principal
                        return redirect('/TemplateCartas')
                    else:
                        # Si ocurre un error, mostrar un mensaje de error
                        return render_template('templates/templateCartas/TemplateCartasModificar.html', error=resultado)
                except Exception as e:
                    # Si ocurre algún error, mostrar un mensaje de error
                    return render_template('templates/templateCartas/TemplateCartasModificar.html', error=str(e))
            else:
                return render_template('templates/templateCartas/TemplateCartasModificar.html')


