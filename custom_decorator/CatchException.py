from typing import Callable
from tkinter import messagebox


class CatchException:
    def __init__(self):
        pass

    def __call__(self, method: Callable):
        def wrapper(instance, **kwargs):
            try:
                return method(instance, **kwargs)

            except Exception as E:
                messagebox.showinfo("에러 발생", E.__str__())

        return wrapper
