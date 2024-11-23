class Planet:
    def __init__(self, nombre, radio, masa, imagen):
        self.nombre = nombre
        self.radio = radio
        self.masa = masa
        self.imagen = imagen


PLANETS_DATA = [
    Planet("Mercurio", "2,439.7 km", "3.30E+23 kg", "./img/mercurio.png"),
    Planet("Venus", "6,051.8 km", "4.87E+24 kg", "./img/venus.png"),
    Planet("Tierra", "6,371.0 km", "5.98E+24 kg", "./img/tierra.png"),
    Planet("Marte", "3,389.5 km", "6.42E+23 kg", "./img/marte.png"),
    Planet("Júpiter", "69,911.0 km", "1.90E+27 kg", "./img/jupiter.png"),
    Planet("Saturno", "58,232.0 km", "5.68E+26 kg", "./img/saturno.png"),
    Planet("Urano", "25,362.0 km", "8.68E+25 kg", "./img/urano.png"),
    Planet("Neptuno", "24,622.0 km", "1.02E+26 kg", "./img/neptuno.png"),
]
