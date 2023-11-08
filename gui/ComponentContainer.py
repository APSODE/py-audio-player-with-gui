from tkinter import *
from tkinter.ttk import *
from typing import Dict


class ComponentContainer:
    def __init__(self):
        self._frame: Dict[str, Frame] = {}
        self._label_frame: Dict[str, LabelFrame] = {}
        self._button: Dict[str, Button] = {}
        self._combobox: Dict[str, Combobox] = {}
        self._option_menu: Dict[str, OptionMenu] = {}
        self._string_var: Dict[str, StringVar] = {}
        self._label: Dict[str, Label] = {}
        self._entry: Dict[str, Entry] = {}
        self._radiobutton: Dict[str, Radiobutton] = {}
        self._int_var: Dict[str, IntVar] = {}

    @property
    def frame(self) -> Dict[str, Frame]:
        return self._frame

    @frame.setter
    def frame(self, value: Dict[str, Frame]):
        self._frame = value

    @property
    def label_frame(self) -> Dict[str, LabelFrame]:
        return self._label_frame

    @label_frame.setter
    def label_frame(self, value: Dict[str, LabelFrame]):
        self._label_frame = value

    @property
    def button(self) -> Dict[str, Button]:
        return self._button

    @button.setter
    def button(self, value: Dict[str, Button]):
        self._button = value

    @property
    def combobox(self) -> Dict[str, Combobox]:
        return self._combobox

    @combobox.setter
    def combobox(self, value: Dict[str, Combobox]):
        self._combobox = value

    @property
    def option_menu(self) -> Dict[str, OptionMenu]:
        return self._option_menu

    @option_menu.setter
    def option_menu(self, value: Dict[str, OptionMenu]):
        self._option_menu = value

    @property
    def string_var(self) -> Dict[str, StringVar]:
        return self._string_var

    @string_var.setter
    def string_var(self, value: Dict[str, StringVar]):
        self._string_var = value

    @property
    def int_var(self) -> Dict[str, IntVar]:
        return self._int_var

    @int_var.setter
    def int_var(self, value: Dict[str, IntVar]):
        self._int_var = value

    @property
    def label(self) -> Dict[str, Label]:
        return self._label

    @label.setter
    def label(self, value: Dict[str, Label]):
        self._label = value

    @property
    def entry(self) -> Dict[str, Entry]:
        return self._entry

    @entry.setter
    def entry(self, value: Dict[str, Entry]):
        self._entry = value

    @property
    def radiobutton(self) -> Dict[str, Radiobutton]:
        return self._radiobutton

    @radiobutton.setter
    def radiobutton(self, value: Dict[str, Radiobutton]):
        self._radiobutton = value

    def get_frame(self, name: str) -> Frame:
        return self._frame.get(name)

    def get_label_frame(self, name: str) -> LabelFrame:
        return self._label_frame.get(name)

    def get_string_var(self, name: str) -> StringVar:
        return self._string_var.get(name)

    def get_int_var(self, name: str) -> IntVar:
        return self._int_var.get(name)

    def get_option_menu(self, name: str) -> OptionMenu:
        return self._option_menu.get(name)

    def get_button(self, name: str) -> Button:
        return self._button.get(name)

    def get_entry(self, name: str) -> Entry:
        return self._entry.get(name)

    def get_label(self, name: str) -> Label:
        return self._label.get(name)

    def get_radiobutton(self, name: str) -> Radiobutton:
        return self._radiobutton.get(name)

    def get_combobox(self, name: str) -> Combobox:
        return self._combobox.get(name)

    def set_string_var_value(self, name: str, value: str):
        self._string_var.get(name).set(value)

    def set_int_var_value(self, name: str, value: int):
        self._int_var.get(name).set(value)

    def add_label_frame(self, name: str, widget: LabelFrame):
        self._label_frame.update({name: widget})

    def add_frame(self, name: str, widget: Frame):
        self._frame.update({name: widget})

    def add_button(self, name: str, widget: Button):
        self._button.update({name: widget})

    def add_combobox(self, name: str, widget: Combobox):
        self._combobox.update({name: widget})

    def add_option_menu(self, name: str, widget: OptionMenu):
        self._option_menu.update({name: widget})

    def add_string_var(self, name: str):
        self._string_var.update({name: StringVar()})

    def add_int_var(self, name: str):
        self._int_var.update({name: IntVar()})

    def add_label(self, name: str, widget: Label):
        self._label.update({name: widget})

    def add_entry(self, name: str, widget: Entry):
        self._entry.update({name: widget})

    def add_radiobutton(self, name: str, widget: Radiobutton):
        self._radiobutton.update({name: widget})
