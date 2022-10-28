from flask import Flask, request

app = Flask(__name__)

#Creación del diccionario usado como base de datos
stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Apple",
                "price": 5.00
            },{
                "name":"Banana",
                "price":1.67
            }
        ]
    }
]

#Aquí vemos como establecemos un endpoitn para acceder al contenido del servidor
#Usamos el método GET para traer la información
@app.get("/store")
def get_stores():
    return {"stores": stores}

#Se usa el mismo endpoint, pero ahora con el método POST
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

#Creamos un nuevo endpoint para agregar objetos a la colección
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

#Un endpint que nos el contenido de un documento con sus articulos
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

#Un endpoint que antes habiamos usado, solo que ahora nos permite ver solo los articulos de una colección
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)