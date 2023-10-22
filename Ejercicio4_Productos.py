import json
{
    "productos": [
        {
            "name": "Coca-Cola 1.5L",
            "price": 120,
            "stock": 100
        },
        {
            "name": "Coca-Cola 2.25L",
            "price": 150,
            "stock": 50,
            "discount": 5
        },
        {
            "name": "Coca-Cola 3L",
            "price": 200,
            "stock": 25,
            "discount": 10
        }
    ]
}

class Product :

    def __init__(self,name,price,stock,discount=0):
      """Inicializa una instancia de la clase product
      Parámetros:
      name: Nombre del produco
      price: Precio
      stock: cantidad del producto en stock
      discount: porcentaje de descuento, por defecto es 0
      """
      self.name=name
      self.price=price
      self.stock=stock
      self.discount=discount

    def __repr__(self):
       """Devuelve una representación de un producto como str"""

       return f"Product({self.name} Descuento: %{self.discount})"

def deseralizar(**kwargs):
  return produtc(**kwargs)

with open("./productos.json", "r") as file:
  datos= json.load(file)
  print(datos)


coca= Product("Coca-Cola 1.5L",120,100)
print(coca)
