import tkinter as tk
from tkinter import filedialog
import time
from enum import Enum

# --- Создание главного окна ---
root = tk.Tk()
root.title("Приложение с элементами управления")
root.geometry("400x300")

# --- Радиокнопки ---
radio_var = tk.StringVar(value="Option1")

radio1 = tk.Radiobutton(root, text="Опция 1", variable=radio_var, value="Option1")
radio2 = tk.Radiobutton(root, text="Опция 2", variable=radio_var, value="Option2")

radio1.grid(row=0, column=0, padx=10, pady=5)
radio2.grid(row=0, column=1, padx=10, pady=5)

# --- Кнопка открытия файла ---
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Выбранный файл: {file_path}")

open_button = tk.Button(root, text="Открыть файл", command=open_file)
open_button.grid(row=1, column=0, columnspan=2, pady=10)

# --- Контейнер (аналог TableLayoutPanel) ---
frame = tk.Frame(root, borderwidth=2, relief="solid")
frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

label1 = tk.Label(frame, text="Ячейка 1", width=15, height=2)
label2 = tk.Label(frame, text="Ячейка 2", width=15, height=2)
label3 = tk.Label(frame, text="Ячейка 3", width=15, height=2)
label4 = tk.Label(frame, text="Ячейка 4", width=15, height=2)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

class MyClass:
    # Константа
    PI = 3.14159  # float

    # Enum
    class Status(Enum):
        ACTIVE = 1
        INACTIVE = 2
        PENDING = 3

    def __init__(self, uint_var: int, bool_array: list[bool]):
        # Переменная типа uint (замена на int >= 0)
        if uint_var < 0:
            raise ValueError("uint_var должен быть >= 0")
        self.uint_var = uint_var

        # Массив bool
        self.bool_array = bool_array

        # Enum-переменная
        self.status = MyClass.Status.ACTIVE

    # Метод для выполнения операций
    def perform_operations(self):
        print(f"Переменная uint: {self.uint_var}")
        print(f"Константа PI: {self.PI}")

        # Операция uint * float
        result = self.uint_var * self.PI
        print(f"Результат умножения uint * float: {result}")

        # Изменение статуса через Enum
        self.status = MyClass.Status.INACTIVE
        print(f"Новый статус: {self.status.name}")


# --- Тестируем класс ---
if __name__ == "__main__":
    # Создаем объект класса
    obj = MyClass(10, [True, False, True])

    # Выполняем операции
    obj.perform_operations()

# --- Таймер ---
def update_time():
    print("Таймер сработал в:", time.strftime("%H:%M:%S"))
    root.after(5000, update_time)  # Повторяет каждые 5 секунд

update_time()

# --- Запуск основного цикла ---
root.mainloop()