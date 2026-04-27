from flask import Flask
@taller.route("/infovehiculos/<int:id>")
def infovehiculo(id):
    vehiculo={
        "id": id,
        "marca": "Peugeot",
        "modelo": "208",
        "color": "blanco",
        "matricula": "AG642GQ"
    }
    return vehiculo


taller= Flask(__name__)
@taller.route("/infoempleado/<int:id>")
def infoempleado(id):
    empleado={
        "id": id,
        "nombre": "Carlos",
        "apellido": "Gómez",
        "edad": "40"
    }
    return empleado

if __name__=="__main__":
    taller.run(debug=True)
