"""
Einfaches Beispiel: Animierte Partikelsimulation
------------------------------------------------
Demonstriert:
- Klassen in Python
- einfache Physik (Position + Geschwindigkeit)
- Animation mit matplotlib

Mehrere Partikel bewegen sich in einer Box und
prallen an den Wänden elastisch ab.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# -------------------------------------------------
# Parameter der Simulation
# -------------------------------------------------

WIDTH = 10
HEIGHT = 10
NUM_PARTICLES = 100
DT = 0.05


# -------------------------------------------------
# Partikelklasse
# -------------------------------------------------

class Particle:

    def __init__(self):
        # zufällige Startposition
        self.pos = np.array([
            np.random.uniform(0, WIDTH),
            np.random.uniform(0, HEIGHT)
        ])

        # zufällige Geschwindigkeit
        self.vel = np.random.uniform(-2, 2, size=2)

    def update(self):
        # Position aktualisieren
        self.pos += self.vel * DT

        # Kollision mit vertikalen Wänden
        if self.pos[0] <= 0 or self.pos[0] >= WIDTH:
            self.vel[0] *= -1

        # Kollision mit horizontalen Wänden
        if self.pos[1] <= 0 or self.pos[1] >= HEIGHT:
            self.vel[1] *= -1


# -------------------------------------------------
# Partikel erzeugen
# -------------------------------------------------

particles = [Particle() for _ in range(NUM_PARTICLES)]


# -------------------------------------------------
# Matplotlib Setup
# -------------------------------------------------

fig, ax = plt.subplots()
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_title("Partikelsimulation")

scatter = ax.scatter([], [], s=80)


# -------------------------------------------------
# Animationsfunktion
# -------------------------------------------------

def animate(frame):
    # Partikel updaten
    for p in particles:
        p.update()

    # Positionen sammeln
    positions = np.array([p.pos for p in particles])

    scatter.set_offsets(positions)

    return scatter,


# -------------------------------------------------
# Animation starten
# -------------------------------------------------

animation = FuncAnimation(
    fig,
    animate,
    frames=300,
    interval=30
)

plt.show()