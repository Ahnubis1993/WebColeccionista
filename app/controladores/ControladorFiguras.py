from flask import render_template, request, redirect
from modelos.FiguraQuery import FiguraQuery

class ControladorFiguras:
    @staticmethod
    def rutasFiguras(app):

        # Para que te lleve al html TemplateFiguras
        @app.route('/TemplateFiguras')
        def templateFigurasPaginaPrincipal():
            return render_template('templates/templateFiguras/TemplateFiguras.html')

        # Para que te lleve al html TemplateFigurasAlta
        @app.route('/TemplateFiguras/AltaFigura') # se llama desde pagina principal figuras
        def templateFigurasAltaPagina():
            return render_template('templates/templateFiguras/TemplateFigurasAlta.html')

        # Ejecuta Query desde html TemplateFigurasAlta. Si ya existe, sale mensaje
        # y te lleva de vuelta a TemplateFigurasAlta
        @app.route('/TemplateFiguras/AltaFigurasQuery', methods=['POST'])
        def templateFigurasAlta():
            if request.method == 'POST':
                # Obtener los datos del formulario
                nombre = request.form['nombre']
                serie = request.form['serie']
                precio = float(request.form['precio'])
                anio = int(request.form['anio'])

                # Verificar si se ha marcado la casilla de confirmación
                if 'check' in request.form:
                    # Intentar insertar la figura
                    resultado = FiguraQuery.insertar_figura(nombre, serie, precio, anio)
                    if resultado == "Figura insertada exitosamente":
                        # Si la inserción es exitosa, redireccionar a la página de éxito
                        return redirect('/TemplateFiguras')
                    else:
                        # Si ya existe una figura con la misma serie, mostrar un mensaje de error al usuario
                        return render_template('templates/templateFiguras/TemplateFigurasAlta.html', mensaje=resultado)


        # Para que te lleve al html TemplateFigurasBuscar
        @app.route('/TemplateFiguras/Baja')
        def templateFigurasBaja():
            return render_template('templates/templateFiguras/TemplateFigurasBaja.html')

        @app.route('/TemplateFiguras/BajaBusqueda', methods=['POST'])
        def bajaBusquedaFiguras():
            if request.method == 'POST':
                # Obtener el valor de búsqueda del formulario
                valor = request.form['valor']

                # Ejecutar la búsqueda por valor
                cartas_encontradas = FiguraQuery.buscar_por_valor(valor)

                # Renderizar el resultado en el template correspondiente
                return render_template('templates/templateFiguras/TemplateFigurasBaja.html',
                                       resultados=cartas_encontradas)

        @app.route('/TemplateFiguras/Borrar/<nombre_figura>', methods=['POST'])
        def borrarFiguras(nombre_figura):
            if request.method == 'POST':
                # No es necesario obtener el nombre de la carta del formulario, ya que está incluido en la URL

                # Intentar borrar la carta por su nombre
                FiguraQuery.borrar_figura_por_serie(nombre_figura)

                # Redirigir a la página principal o a alguna otra página de confirmación
                return render_template('templates/templateFiguras/TemplateFiguras.html')

        # Para que te lleve al html TemplateFigurasMostrar
        @app.route('/TemplateFiguras/MostrarTodos')
        def templateFigurasMostrarTodos():
            figuras = FiguraQuery.buscar_todas_figuras()
            return render_template('templates/templateFiguras/TemplateFigurasMostrarTodos.html', resultado=figuras)
        
        # Para que te lleve al html TemplateFigurasBuscar
        @app.route('/TemplateFiguras/Buscar')
        def templateFigurasBuscar():
            return render_template('templates/templateFiguras/TemplateFigurasBuscar.html')

        @app.route('/TemplateFiguras/BuscarQuery', methods=['POST'])
        def buscarFiguras():
            if request.method == 'POST':
                # Obtener el valor de búsqueda del formulario
                valor_busqueda = request.form['valor']

                # Ejecutar la consulta de búsqueda en la base de datos utilizando el método estático de la clase FiguraQuery
                resultados_busqueda = FiguraQuery.buscar_por_valor(valor_busqueda)

                # Renderizar el template con los resultados de la búsqueda
                return render_template('templates/templateFiguras/TemplateFigurasBuscar.html', resultados=resultados_busqueda)


        # Para que te lleve al html TemplateFigurasModificar
        @app.route('/TemplateFiguras/Modificar')
        def templateFigurasModificar():
            return render_template('templates/templateFiguras/TemplateFigurasModificar.html')

        @app.route('/TemplateFiguras/ModificarBusqueda', methods=['POST'])
        def modificarBusquedaFiguras():
            if request.method == 'POST':
                # Obtener el valor de búsqueda del formulario
                valor = request.form['valor']

                # Ejecutar la búsqueda por valor
                figuras_encontradas = FiguraQuery.buscar_por_valor(valor)

                # Renderizar el resultado en el template correspondiente
                return render_template('templates/templateFiguras/TemplateFigurasModificar.html',
                                       resultados=figuras_encontradas)

        @app.route('/TemplateFiguras/ModificarQuery', methods=['POST'])
        def modificarFigura():
            if request.method == 'POST':
                # Obtener los datos del formulario
                serie = request.form['serie']
                nuevo_nombre = request.form['nuevo_nombre']
                nuevo_precio = float(request.form['nuevo_precio'])
                nuevo_anio = int(request.form['nuevo_anio'])

                # Modificar la figura
                resultado = FiguraQuery.modificar_figura_por_serie(serie, nuevo_nombre, nuevo_precio, nuevo_anio)
                if resultado == "Figura modificada exitosamente":
                    # Si la modificación es exitosa, redireccionar a la página principal
                    return redirect('/TemplateFiguras')
                else:
                    # Si ocurre un error, mostrar un mensaje de error
                    return render_template('templates/templateFiguras/TemplateFigurasModificar.html')
            else:
                return render_template('templates/templateFiguras/TemplateFigurasModificar.html')