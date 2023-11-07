from launcher import launcher
from pizzaGIU import *

if __name__ == "__main__":

    root = tk.Tk()
    app = PizzaApp(root)
    root.mainloop()

    #Ejecuta el programa por la terminal
    #launcher()