import tkinter as tk
import random
import string


parole = ""
result = ""
MaxNum = 8
arr = list(string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase)

Window = tk.Tk()
Window.geometry("400x100")
class RandomParole:
   def __init__(self):
      Lbl = tk.Label(Window, text="Генератор паролей")
      Lbl.pack()
      But = tk.Button(Window, text="Сгенерировать", command=self.parole)
      But.pack()
   def parole(self):
      global parole
      global result
      parole = random.choices(arr, k=8)
      result = "".join(parole)
      self.Parole = tk.Label(Window, text=f"Твой пароль: {result}")
      self.Parole.pack()

RndmParole = RandomParole()

Window.mainloop()