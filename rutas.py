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

if __name__=="__main__":
    taller.run(debug=True)