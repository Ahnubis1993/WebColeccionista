from firebase_admin import firestore

class CartaQuery:

    @staticmethod
    def insertar_carta(nombre, juego, coleccion, numero, precio):
        db = firestore.client()

        # Verificar si ya existe una carta con el mismo nombre
        carta_existente = db.collection('cartas').document(nombre).get()
        if carta_existente.exists:
            # Aquí puedes manejar el caso de que ya exista una carta con el mismo nombre
            # Por ejemplo, puedes mostrar un mensaje de error al usuario o actualizar los datos existentes
            return "Ya existe una carta con el mismo nombre"
        else:
            # Si no existe, procede con la inserción
            db.collection('cartas').document(nombre).set({
                'nombre': nombre,
                'juego': juego,
                'coleccion': coleccion,
                'numero': numero,
                'precio': precio
            })
            return "Carta insertada exitosamente"

    @staticmethod
    def buscar_por_valor(valor):
        db = firestore.client()
        cartas_encontradas = []

        # Buscar documentos que contengan el valor en el campo 'nombre'
        resultados_nombre = db.collection('cartas').where('nombre', '==', valor).get()
        for documento in resultados_nombre:
            carta = documento.to_dict()
            if carta not in cartas_encontradas:
                cartas_encontradas.append(carta)

        # Buscar documentos que contengan el valor en el campo 'juego'
        resultados_juego = db.collection('cartas').where('juego', '==', valor).get()
        for documento in resultados_juego:
            carta = documento.to_dict()
            if carta not in cartas_encontradas:
                cartas_encontradas.append(carta)

        # Buscar documentos que contengan el valor en el campo 'coleccion'
        resultados_coleccion = db.collection('cartas').where('coleccion', '==', valor).get()
        for documento in resultados_coleccion:
            carta = documento.to_dict()
            if carta not in cartas_encontradas:
                cartas_encontradas.append(carta)

        # Buscar documentos que contengan el valor en el campo 'numero'
        resultados_numero = db.collection('cartas').where('numero', '==', valor).get()
        for documento in resultados_numero:
            carta = documento.to_dict()
            if carta not in cartas_encontradas:
                cartas_encontradas.append(carta)

        # Buscar documentos que contengan el valor en el campo 'precio'
        resultados_precio = db.collection('cartas').where('precio', '==', valor).get()
        for documento in resultados_precio:
            carta = documento.to_dict()
            if carta not in cartas_encontradas:
                cartas_encontradas.append(carta)

        return cartas_encontradas

    @staticmethod
    def buscar_todas_cartas():
        db = firestore.client()
        resultados = db.collection('cartas').get()
        cartas_encontradas = []
        for documento in resultados:
            cartas_encontradas.append(documento.to_dict())
        return cartas_encontradas

    @staticmethod
    def borrar_carta_por_nombre(nombre):
        db = firestore.client()
        db.collection('cartas').document(nombre).delete()

    @staticmethod
    def modificar_carta_por_nombre(nombre, nuevo_nombre, nuevo_juego, nueva_coleccion, nuevo_numero, nuevo_precio):
        db = firestore.client()

        # Verificar si la carta existe
        carta_ref = db.collection('cartas').document(nombre)
        carta = carta_ref.get()

        if carta.exists:
            # Modificar los campos de la carta
            carta_ref.update({
                'nombre':nuevo_nombre,
                'juego': nuevo_juego,
                'coleccion': nueva_coleccion,
                'numero': nuevo_numero,
                'precio': nuevo_precio
            })
            return "Carta modificada exitosamente"
        else:
            return "No se encontró la carta"
