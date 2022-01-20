from flask import Flask, render_template


app = Flask( __name__ )
usuarios = [{
        "nombre":"Alex",
        "apellido":"Martinez",
        "id":1
    },
    {
        "nombre":"Diego",
        "apellido":"Asmat",
        "id":2
    }]
#por Default el methods se pone en GET, pero es mejor colocar siempre
@app.route('/', methods=['GET'])
def paginaInicial():
    hobbies = ["Programar","Leer","Videojuegos","Cantar"]
    return render_template("index.html",nombre="Alex",apellido="Martinez", hobbies=hobbies)

#se puede utilizar la misma ruta si el method es diferente, en la web siempre aparece el GET
#<nombre> es un parametro
@app.route('/datos/<nombre>/<apellido>', methods=['GET'])
def imprimeDatos(nombre,apellido):
    return "Estos son los datos de "+nombre+ " " + apellido

@app.route('/usuarios/<int:id>', methods=["GET"])
def imprimeInformacionDeUsuario( id ):
    print( type( id ))
    usuarioEncontrado = None
    for usuario in usuarios:
        if(usuario["id"]==id):
            usuarioEncontrado=usuario
    return render_template("usuario.html", usuario=usuarioEncontrado, id=id)


if( __name__ )== "__main__":
    app.run( debug=True )