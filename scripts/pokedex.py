import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("600x500")
window.title("Pokedex")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Master Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack()

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_height = tk.Label(window)
pokemon_height.config(font=("Arial", 20))
pokemon_height.pack(padx=10, pady=10)

pokemon_weight = tk.Label(window)
pokemon_weight.config(font=("Arial", 20))
pokemon_weight.pack(padx=10, pady=10)

pokemon_abilities = tk.Label(window)
pokemon_abilities.config(font=("Arial", 20))
pokemon_abilities.pack(padx=10, pady=10)

pokemon_base_stats = tk.Label(window)
pokemon_base_stats.config(font=("Arial", 20))
pokemon_base_stats.pack(padx=10, pady=10)

pokemon_moves = tk.Label(window)
pokemon_moves.config(font=("Arial", 20))
pokemon_moves.pack(padx=10, pady=10)


# function

window.mainloop()



