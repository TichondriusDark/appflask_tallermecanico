from flask import Flask

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



@taller.route("/stockrepuestos")
def cant_stock():
    repuestos = {
        "Bujía": 15,
        "Manguera de Agua": 13,
        "Llantas": 22,
        "Válvulas": 5,
        "Pistones": 8,
        "Inyectores": 10
    }
    return repuestos

if __name__=="__main__":
    taller.run(debug=True)