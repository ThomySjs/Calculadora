import tkinter as tk

# Esta funcion sirve para hacer los calculos, evalua la entrada y realiza la operación
def calcular(): 
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

#Con estos comandos creamos la ventana, le asignamos el tamaño y el titulo
window = tk.Tk()
window.geometry("300x200")
window.title("Calculator") 
#La linea 15 asigna el resultado de la operación a la variable result, StringVar es una variable diseñada para contener cadenas de texto 
result = tk.StringVar()
#Crea un widget de entrada que esta anclado a la variable result
entry = tk.Entry(window, textvariable=result)
entry.grid(row=0, column=0, columnspan=4)
#Operadores
operators = ['7', '8', '9', '/',
             '4', '5', '6', '*',
             '1', '2', '3', '-',
             'C', '0', '=', '+']
# Basicamente define las acciones al clickear "=" y "C" (que seria borrar) 
def button_click(value):
    if value == "=":
        calcular()
    elif value == "C":
        entry.delete(0, "end")   
    else:
        entry.insert("end", value)
row = 1
column = 0
for operator in operators: 
    button = tk.Button(window, text=operator, width=5, height=2, command=lambda val=operator: button_click(val))
    button.grid(row=row, column=column)
    column += 1
    if column > 3:
        column=0
        row += 1
window.mainloop()

