from firebase_admin import firestore

class FiguraQuery:

    @staticmethod
    def insertar_figura(nombre, serie, precio, anio):
        # Acceder a la instancia de Firestore
        db = firestore.client()

        # Verificar si ya existe una figura con la misma serie
        figura_existente = db.collection('figuras').document(serie).get()
        if figura_existente.exists:
            # Aquí puedes manejar el caso de que ya exista una figura con la misma serie
            # Por ejemplo, puedes mostrar un mensaje de error al usuario o actualizar los datos existentes
            return "Ya existe una figura con la misma serie"
        else:
            # Si no existe, procede con la inserción
            db.collection('figuras').document(serie).set({
                'nombre': nombre,
                'serie': serie,
                'precio': precio,
                'anio': anio
            })
            return "Figura insertada exitosamente"

    @staticmethod
    def buscar_por_valor(valor):
        # Acceder a la instancia de Firestore
        db = firestore.client()

        # Inicializar una lista para almacenar los resultados de la consulta
        figuras_encontradas = []

        # Realizar la consulta para buscar documentos que contengan el valor en el campo 'nombre'
        resultados_nombre = db.collection('figuras').where('nombre', '==', valor).get()
        for documento in resultados_nombre:
            figura = documento.to_dict()
            if figura not in figuras_encontradas:
                figuras_encontradas.append(figura)

        # Realizar la consulta para buscar documentos que contengan el valor en el campo 'serie'
        resultados_serie = db.collection('figuras').where('serie', '==', valor).get()
        for documento in resultados_serie:
            figura = documento.to_dict()
            if figura not in figuras_encontradas:
                figuras_encontradas.append(figura)

        # Realizar la consulta para buscar documentos que contengan el valor en el campo 'precio'
        resultados_precio = db.collection('figuras').where('precio', '==', valor).get()
        for documento in resultados_precio:
            figura = documento.to_dict()
            if figura not in figuras_encontradas:
                figuras_encontradas.append(figura)

        # Realizar la consulta para buscar documentos que contengan el valor en el campo 'anio'
        resultados_anio = db.collection('figuras').where('anio', '==', valor).get()
        for documento in resultados_anio:
            figura = documento.to_dict()
            if figura not in figuras_encontradas:
                figuras_encontradas.append(figura)

        return figuras_encontradas

    @staticmethod
    def buscar_todas_figuras():
        # Acceder a la instancia de Firestore
        db = firestore.client()

        # Realizar la consulta para buscar todos los documentos en la colección "figuras"
        resultados = db.collection('figuras').get()

        # Inicializar una lista para almacenar los resultados de la consulta
        figuras_encontradas = []

        # Iterar sobre los resultados y agregarlos a la lista
        for documento in resultados:
            figuras_encontradas.append(documento.to_dict())

        return figuras_encontradas

    @staticmethod
    def borrar_figura_por_serie(serie):
        # Acceder a la instancia de Firestore
        db = firestore.client()

        # Borrar el documento en la colección "figuras" con la serie proporcionada
        db.collection('figuras').document(serie).delete()

    @staticmethod
    def modificar_figura_por_serie(serie, nombre=None, precio=None, anio=None):
        # Acceder a la instancia de Firestore
        db = firestore.client()

        # Crear un diccionario que contenga solo los campos que se proporcionan
        campos_actualizar = {}
        if nombre is not None:
            campos_actualizar['nombre'] = nombre
        if precio is not None:
            campos_actualizar['precio'] = precio
        if anio is not None:
            campos_actualizar['anio'] = anio

        # Verificar si hay campos para actualizar
        if campos_actualizar:
            # Actualizar el documento en la colección "figuras" con la serie proporcionada
            db.collection('figuras').document(serie).update(campos_actualizar)
            return "Figura modificada exitosamente"
        else:
            return "No se proporcionaron campos para actualizar"

