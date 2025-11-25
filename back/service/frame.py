import tkinter as tk


def create_frame_use_pack(parent: tk.Tk, param) -> tk.Frame:
    """
    Создаём фрэйи и задаём ему расположение с помощью метода pack

    :param parent: где распологаем фрэйм
    :param param: стилистические параметры для фрэйма
    :return: tk.Frame
    """

    frame = tk.Frame(parent, **param)
    frame.pack(expand=True, fill="both")
    return frame
