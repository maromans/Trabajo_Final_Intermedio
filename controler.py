from tkinter import Tk
from vista import Aplicacion


class AppPrincipal:
    """Clase para iniciar la app."""

    def __init__(self, ventana):
        Aplicacion(ventana)


if __name__ == "__main__":
    root = Tk()
    miapp = AppPrincipal(root)
    root.mainloop()
