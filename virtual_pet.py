import tkinter as tk
import time
from pet import Pet


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pet = Pet(
        name="Бабр",
        fullness=100,
        health=100,
        mood=100,
        cleanness=100,
        energy=100
        )
        self.geometry("512x512")
        self.name_lbl = tk.Label(self, text=f"Имя: {self.pet.name}")
        self.fullness_lbl = tk.Label(self)
        self.health_lbl = tk.Label(self, text=f"Здоровье: {self.pet.health}")
        self.mood_lbl = tk.Label(self, text=f"Настроение: {self.pet.mood}")
        self.cleanness_lbl = tk.Label(self, text=f"Чистота: {self.pet.cleanness}")
        self.energy_lbl = tk.Label(self, text=f"Чистота: {self.pet.energy}")
        self.name_lbl.pack()
        self.fullness_lbl.pack()
        self.health_lbl.pack()
        self.mood_lbl.pack()
        self.cleanness_lbl.pack()
        self.energy_lbl.pack()
        self.canvas = tk.Canvas(self, width=256, height=256)
        self.canvas.pack()
        self.img = tk.PhotoImage(file=self.pet.portrait)
        self.img = self.img.subsample(3)
        self.canvas.create_image(128, 128, image=self.img, anchor=tk.CENTER)

        self.feed_btn = tk.Button(text="Покормить")
        self.feed_btn.pack()


    def update(self):
        self.pet.downgrade_stats()
        self.fullness_lbl.config(text=f"Сытость: {self.pet.fullness}")
        self.after(1000, self.update)


if __name__ == '__main__':
    window = App()
    window.update()
    window.mainloop()
