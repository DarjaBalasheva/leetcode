import tkinter as tk

from back.service.frame import create_frame_use_pack
from back.service.label import create_label_use_pack
from style.base_style import geometry, colors, font
from style.frame_style import display_frame, button_frame
from style.label_style import total_label, current_label
from back.data.data import digits


class Calculator:
    """
    Модель классического калькулятора
     для математических вычислений
    """

    def __init__(self):
        # Создаём главное окно
        self.window = tk.Tk()
        self.window.geometry(geometry.get("main_window"))
        self.window.title('Calculator')
        self.window['bg'] = colors.get('main_bg')

        # Значения, отображающиеся на экране
        self.total_expression = "0"
        self.current_expression = "0"

        # Создаём дислпей для кнопок и результата
        self.display_frame, self.button_frame = self.create_display()

        # Создаём лэйблы для отображения результатов
        self.total_label, self.current_label = self.create_display_labels()

        # Создание кнопок
        self.create_digit_buttons()

    def create_display(self) -> tuple:
        """
        Создаём фрэйм для результатов
        :return: tk.Frame, tk.Frame
        """
        disp_frame = create_frame_use_pack(parent=self.window,
                                           param=display_frame)

        butt_frame = create_frame_use_pack(parent=self.window,
                                           param=button_frame)
        return disp_frame, butt_frame

    def create_display_labels(self) -> tuple:
        """
        Создаём лэйблы для отображения значений
        :return: tk.Label, tk.Label
        """
        tot_label = create_label_use_pack(parent=self.display_frame,
                                          text=self.total_expression,
                                          param=total_label)

        label = create_label_use_pack(parent=self.display_frame,
                                      text=self.current_expression,
                                      param=current_label)
        return tot_label, label

    def create_digit_buttons(self) -> None:
        """
        Создаём кнопки
        :return:
        """
        for digit, grid_values in digits.items():
            print(digit, grid_values)
            button = tk.Button(self.button_frame, text=str(digit), bg="#A3E4D7",  # Цвет кнопок
                               # command=lambda d=digit: self.update_expression(d))
                               )
            button.grid(row=grid_values[0], column=grid_values[1], sticky="nsew")

        # По высоте
        for i in range(4):
            self.button_frame.grid_rowconfigure(i, weight=1)
        # По ширине
        for i in range(3):
            self.button_frame.grid_columnconfigure(i, weight=1)

    def update_expression(self, value):
        print(value)
        # Обрабатываем 0
        if self.current_expression == "0" and value != "C":
            self.current_expression = str(value)
        # Обрабатываем Clear
        elif value == "C":
            self.current_expression = "0"
        else:
            # Добавляем значение
            self.current_expression += str(value)
        # Обновляем значение
        self.current_label.config(text=self.current_expression)

    def clear_expression(self):
        self.current_expression = "0"
        self.current_label.config(text=self.current_expression)


# Запуск
if __name__ == "__main__":
    calculator = Calculator()
    calculator.window.mainloop()
