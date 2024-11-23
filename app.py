import tkinter as tk
from PIL import Image, ImageTk


class App:
    def __init__(self, root, planets):
        self.root = root
        self.root.title("Selección de Planetas")
        self.root.geometry("800x400")
        self.root.configure(bg="#A9CCE3")
        self.planets = planets
        self.selected_planet = tk.StringVar(value="")
        self.create_widgets()

    def create_widgets(self):
        # Marco principal
        main_frame = tk.Frame(self.root, bg="#A9CCE3")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Marco izquierdo para los planetas
        planets_frame = tk.Frame(main_frame, bg="#A9CCE3", width=700)
        planets_frame.pack(side="left", fill="y", padx=10)

        # Etiqueta de título
        title_label = tk.Label(
            planets_frame,
            text="Selecciona un planeta",
            bg="#A9CCE3",
            font=("system-ui", 20, "bold"),
        )
        title_label.pack(pady=10)

        # Marco para los botones con imágenes
        grid_frame = tk.Frame(planets_frame, bg="#A9CCE3")
        grid_frame.pack()

        # Crear botones e imágenes en una cuadrícula de 4 columnas y 2 filas
        for i, planet in enumerate(self.planets):
            img = Image.open(planet.imagen)
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            planet_image = ImageTk.PhotoImage(img)

            # Crear un marco para cada planeta que contendrá la imagen y el nombre
            planet_frame = tk.Frame(grid_frame, bg="#A9CCE3")
            planet_frame.grid(row=i // 4, column=i % 4, padx=10, pady=10)

            # Crear el botón de radiobutton
            button = tk.Radiobutton(
                planet_frame,
                variable=self.selected_planet,  # Variable vinculada
                value=planet.nombre,  # Valor es el nombre del planeta
                command=self.update_info,  # Actualizar información al cambiar selección
                image=planet_image,
                bg="#A9CCE3",
                indicatoron=False,
            )
            button.image = planet_image  # Guardar referencia
            button.pack()

            # Crear el label con el nombre del planeta debajo de la imagen
            name_label = tk.Label(
                planet_frame, text=planet.nombre, bg="#A9CCE3", font=("system-ui", 10)
            )
            name_label.pack(pady=5)

        # Marco derecho para la información
        info_frame = tk.Frame(main_frame, bg="#D4E6F1", relief="groove")
        info_frame.pack(side="left", fill="both", expand=True, padx=20, pady=80)

        # Etiqueta para mostrar el planeta seleccionado
        self.planet_label = tk.Label(
            info_frame, text="Planeta", bg="#D4E6F1", font=("system-ui", 14, "bold")
        )
        self.planet_label.pack(pady=10)

        # Etiqueta y campo para el radio
        tk.Label(info_frame, text="Radio:", bg="#D4E6F1", font=("system-ui", 12)).pack(
            anchor="w", padx=30, pady=4
        )
        self.radio_label = tk.Label(info_frame, font=("system-ui", 12))
        self.radio_label.pack(fill="x", padx=30, pady=5)

        # Etiqueta y campo para la masa
        tk.Label(info_frame, text="Masa:", bg="#D4E6F1", font=("system-ui", 12)).pack(
            anchor="w", padx=30, pady=4
        )
        self.masa_label = tk.Label(info_frame, font=("system-ui", 12))
        self.masa_label.pack(fill="x", padx=30, pady=5)

        # Mostrar información inicial
        self.update_info()

    def update_info(self):
        planet_name = self.selected_planet.get()
        selected_planet = next(
            (p for p in self.planets if p.nombre == planet_name), None
        )

        # Si el planeta existe, actualizamos la información
        if selected_planet:
            self.planet_label.config(text=f"Planeta: {selected_planet.nombre}")
            self.radio_label.config(text=f"{selected_planet.radio}")
            self.masa_label.config(text=f"{selected_planet.masa}")
