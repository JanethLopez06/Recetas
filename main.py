import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk


class Pizza:
    def __init__(self, nombre, ingredientes, precio):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Pedido:
    def __init__(self):
        self.pizzas = []

    def agregar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def eliminar_pizza(self, indice):
        if 0 <= indice < len(self.pizzas):
            self.pizzas.pop(indice)

    def total_pagar(self):
        return sum(p.precio for p in self.pizzas)

    def pagar(self):
        messagebox.showinfo(
            "Pago", "Pedido pagado con éxito.\n\n¡Truco activado! La pizza es gratis hoy.")
        self.pizzas.clear()
        actualizar_carrito()


pizzas_disponibles = [
    Pizza("Margarita", ["Tomate", "Mozzarella", "Albahaca"], 100),
    Pizza("Pepperoni", ["Tomate", "Mozzarella", "Pepperoni"], 120),
    Pizza("Cuatro Quesos", ["Mozzarella", "Cheddar",
          "Parmesano", "Gorgonzola"], 130),
    Pizza("Hawaiana", ["Tomate", "Mozzarella", "Jamón", "Piña"], 125)
]

pedido = Pedido()


def agregar_al_pedido(indice):
    pedido.agregar_pizza(pizzas_disponibles[indice])
    actualizar_carrito()


def eliminar_del_pedido():
    seleccion = carrito_listbox.curselection()
    if seleccion:  # Verifica si hay algo seleccionado
        indice = seleccion[0]  # Obtiene el inice seleccionado
        pedido.eliminar_pizza(seleccion[0])
        actualizar_carrito()
    else:
        messagebox.showwarning(
            "Eliminar", "Atención.\n\n¡Por favor, selecciona una pizza para eliminar.")


def actualizar_carrito():
    carrito_listbox.delete(0, tk.END)
    for pizza in pedido.pizzas:
        carrito_listbox.insert(tk.END, str(pizza))
    total_label.config(text=f"Total: ${pedido.total_pagar()}")


def pagar_pedido():
    pedido.pagar()


root = tk.Tk()
root.title("Pizzería Perfecta")
root.geometry("900x1000")
root.resizable(False, False)
root.configure(bg="#f4a261")

# Cargar imagen del logo
# Asegúrate de tener un archivo 'logo.png' en el mismo directorio
original_img = Image.open("Recetas\logo.png")
resized_img = original_img.resize((500, 200), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_img)

# Mostrar la imagen en la interfaz
logo_label = tk.Label(root, image=logo_img, bg="#f4a261")
logo_label.pack(pady=5, anchor="n")  # Reduce el espacio alrededor de la imagen

# Crear un Frame para organizar mejor el contenido
content_frame = tk.Frame(root, bg="#f4a261")
content_frame.pack(pady=5)  # Permite que el contenido se ajuste mejor


frame_pizzas = tk.Frame(content_frame, bg="#f4a261")
frame_pizzas.pack(side=tk.LEFT, padx=10, pady=5)

frame_carrito = tk.Frame(content_frame, bg="#e76f51")
frame_carrito.pack(side=tk.RIGHT, padx=10, pady=5)

tk.Label(frame_pizzas, text="Menú de Pizzas", font=(
    "Arial", 14, "bold"), bg="#f4a261").pack()
for i, pizza in enumerate(pizzas_disponibles):
    tk.Button(frame_pizzas, text=f"{pizza.nombre} - ${pizza.precio}\nIngredientes: {', '.join(pizza.ingredientes)}",
              command=lambda i=i: agregar_al_pedido(i), bg="#6A994E", fg="white", font=("Arial", 10, "bold"),
              padx=10, pady=5, relief=tk.RAISED).pack(pady=5)

tk.Label(frame_carrito, text="Carrito de Compras", font=(
    "Arial", 14, "bold"), bg="#e76f51", fg="white").pack()
carrito_listbox = tk.Listbox(
    frame_carrito, width=40, height=10, bg="#264653", fg="white", font=("Arial", 10))
carrito_listbox.pack()

total_label = tk.Label(frame_carrito, text="Total: $0", font=(
    "Arial", 12, "bold"), bg="#e76f51", fg="white")
total_label.pack()

tk.Button(frame_carrito, text="Eliminar", command=eliminar_del_pedido, bg="#d62828",
          fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=5)
tk.Button(frame_carrito, text="Pagar", command=pagar_pedido, bg="#00A878",
          fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=5)

tk.Button(root, text="Salir", command=root.quit, bg="#e63946",
          fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=10)

root.mainloop()
