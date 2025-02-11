import tkinter as tk
from PIL import Image, ImageTk  # Для работы с изображениями

root = tk.Tk()
root.title("Приложение с ресурсами")

img = Image.open("resources/photo_for_lab1.jpg")
img = ImageTk.PhotoImage(img)

label = tk.Label(root, image=img)
label.pack()

root.mainloop()