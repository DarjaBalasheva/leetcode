import tkinter as tk


def create_label_use_pack(parent: tk.Frame, text: str, param: dict) -> tk.Label:
    """
    Создаём лэйбл и задаём ему расположение с помощью метода pack

    :param parent: компонент, в котором располагаем лэйбл
    :param text: текст, который выводим на экран
    :param param: стилистические компоненты лэйбла
    :return: tk.Label
    """

    label = tk.Label(parent, text=text, **param)
    label.pack(expand=True, fill='both')
    return label
