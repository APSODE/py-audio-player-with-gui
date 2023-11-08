from tkinter import Tk, Frame, Button, LabelFrame, Label, messagebox, Toplevel, StringVar, Entry
from tkinter.ttk import Combobox

from PyAudioPlayer import PyAudioPlayer
from custom_decorator.CatchException import CatchException
from gui.ComponentManager import ComponentManager
from gui.RenderParamWrapper import RenderParamWrapper

from asyncio import run


_MENU_BTN_FRAME_NAMES = ["play_btn_frame", "stop_btn_frame", "rplay_btn_frame", "plot_btn_frame"]
_MEDIA_CONTROL_SYMBOLS = ["▶", "■", "◀", "파형분석"]
_BTN_RELATED_COMMAND = ["_audio_file_play", "_audio_file_stop", "_audio_file_rplay", "_show_audio_file_plot"]


class PopUpGUI(Toplevel):
    def __init__(self, master: Tk, player_instance: PyAudioPlayer):
        super().__init__(master = master)
        self._component_manager = ComponentManager.create_manager()
        self._py_audio_player = player_instance
        self._set_initial_window()
        self._render_component()

    def _set_initial_window(self):
        width = 500
        height = 150
        center_x = (self.winfo_screenwidth() // 2) - (width // 2)
        center_y = (self.winfo_screenheight() // 2) - (height // 2)
        self.title("PyAudioPlayer v1.0 - Plot Data Inputter")
        self.geometry(f"{width}x{height}+{center_x}+{center_y}")
        self.resizable(False, False)

    def _render_component(self):
        self._set_frame()
        self._set_label_frame()
        self._set_entry()
        self._set_button()

    def _set_frame(self):
        self._component_manager.add_component(
            name = "base_frame",
            component = Frame(self),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(side = "top", anchor = "center", ipadx = 10, ipady = 5)
        )

        base_frame = self._component_manager.get_component("base_frame", Frame)

        self._component_manager.add_component(
            name = "start_end_time_frame",
            component = Frame(base_frame),
            with_render = True,
            render_type = "grid",
            render_param = RenderParamWrapper(row = 0, column = 0, padx = 10, pady = 10)
        )

        self._component_manager.add_component(
            name = "button_frame",
            component = Frame(base_frame),
            with_render = True,
            render_type = "grid",
            render_param = RenderParamWrapper(row = 1, column = 0, padx = 10, pady = 10)
        )

        start_end_time_frame = self._component_manager.get_component("start_end_time_frame", Frame)

        self._component_manager.add_component(
            name = "start_time_frame",
            component = Frame(start_end_time_frame),
            with_render = True,
            render_type = "grid",
            render_param = RenderParamWrapper(row = 0, column = 0, padx = 10)
        )
        self._component_manager.add_component(
            name = "end_time_frame",
            component = Frame(start_end_time_frame),
            with_render = True,
            render_type = "grid",
            render_param = RenderParamWrapper(row = 0, column = 1, padx = 10)
        )

    def _set_label_frame(self):
        self._component_manager.add_component(
            name = "start_time_label_frame",
            component = LabelFrame(
                self._component_manager.get_component("start_time_frame", Frame),
                text = "시작시간"
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", ipadx = 10, ipady = 4)
        )

        self._component_manager.add_component(
            name = "end_time_label_frame",
            component = LabelFrame(
                self._component_manager.get_component("end_time_frame", Frame),
                text = "종료시간"
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", ipadx = 10, ipady = 4)
        )

    def _set_entry(self):
        start_time_default_string = StringVar()
        start_time_default_string.set("0")

        end_time_default_string = StringVar()
        end_time_default_string.set("0")

        self._component_manager.add_component(
            name = "start_time_entry",
            component = Entry(
                self._component_manager.get_component("start_time_label_frame", LabelFrame),
                textvariable = start_time_default_string
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", pady = 10)
        )

        self._component_manager.add_component(
            name = "end_time_entry",
            component = Entry(
                self._component_manager.get_component("end_time_label_frame", LabelFrame),
                textvariable = end_time_default_string
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", pady = 10)
        )

    def _set_button(self):
        self._component_manager.add_component(
            name = "accept_btn",
            component = Button(
                self._component_manager.get_component("button_frame", Frame),
                text = "확인",
                width = 6,
                height = 2,
                command = self._on_click_button
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", padx = 10)
        )

    def _on_click_button(self):
        start_time_component = self._component_manager.get_component("start_time_entry", Entry)
        end_time_component = self._component_manager.get_component("end_time_entry", Entry)

        try:
            start_time_value = int(start_time_component.get())
            end_time_value = int(end_time_component.get())

            start_time_not_negative_check = start_time_value >= 0
            end_time_not_negative_check = end_time_value >= 0
            duration_positive_check = end_time_value - start_time_value > 0
            end_time_not_over_check = self._py_audio_player.loaded_file.length - end_time_value >= 0

            if (start_time_not_negative_check and end_time_not_negative_check
                    and duration_positive_check and end_time_not_over_check):

                run(self._py_audio_player.show_plot(*(start_time_value, end_time_value)))
                self.destroy()
            else:
                raise ValueError()

        except ValueError as E:
            messagebox.showinfo("에러 발생!", "수치를 다시 입력하십시오.")


class PyAuidoPlayerGUI(Tk):
    def __init__(self):
        super().__init__()
        self._component_manager = ComponentManager.create_manager()
        self._py_audio_player = PyAudioPlayer(with_gui = True)
        self._set_initial_window()
        self._render_component()
        self.mainloop()

    def _set_initial_window(self):
        width = 500
        height = 300
        center_x = (self.winfo_screenwidth() // 2) - (width // 2)
        center_y = (self.winfo_screenheight() // 2) - (height // 2)
        self.title("PyAudioPlayer v1.0")
        self.geometry(f"{width}x{height}+{center_x}+{center_y}")
        self.resizable(False, False)

    def _render_component(self):
        self._set_base_frame()
        self._set_label_frame()
        self._set_player_menu_frame()
        self._set_label()
        self._set_button()
        self._set_combobox()
        self._set_event_binder()

    def _set_base_frame(self):
        self._component_manager.add_component(
            name = "base_frame",
            component = Frame(self),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(side = "top", anchor = "center")
        )

        base_frame = self._component_manager.get_component("base_frame", Frame)
        self._component_manager.add_component(
            name = "top_base_frame",
            component = Frame(base_frame),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(side = "top", anchor = "center")
        )
        self._component_manager.add_component(
            name = "bottom_base_frame",
            component = Frame(base_frame),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(side = "top", anchor = "center")
        )

        top_base_frame = self._component_manager.get_component("top_base_frame", Frame)
        self._component_manager.add_component(
            name = "audio_data_frame",
            component = Frame(top_base_frame),
            with_render = True,
            render_type = "grid",
            render_param = RenderParamWrapper(row = 0, column = 0, padx = 20, pady = 20)
        )

        self._component_manager.add_component(
            name = "player_menu_frame",
            component = Frame(top_base_frame),
            with_render = True,
            render_type = "grid",
            render_param = RenderParamWrapper(row = 0, column = 1, padx = 20, pady = 20)
        )

        bottom_base_frame = self._component_manager.get_component("bottom_base_frame", Frame)
        self._component_manager.add_component(
            name = "file_select_frame",
            component = Frame(bottom_base_frame),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(side = "top", anchor = "center")
        )

    def _set_player_menu_frame(self):
        for idx, name in enumerate(_MENU_BTN_FRAME_NAMES):
            self._component_manager.add_component(
                name = name,
                component = Frame(self._component_manager.get_component("player_menu_label_frame", LabelFrame)),
                with_render = True,
                render_type = "grid",
                render_param = RenderParamWrapper(row = 0, column = idx, padx = 10, pady = 10)
            )

    def _set_label_frame(self):
        self._component_manager.add_component(
            name = "audio_data_label_frame",
            component = LabelFrame(
                self._component_manager.get_component("audio_data_frame", Frame),
                text = "오디오 파일 정보"
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", ipadx = 10, ipady = 10)
        )
        self._component_manager.add_component(
            name = "player_menu_label_frame",
            component = LabelFrame(
                self._component_manager.get_component("player_menu_frame", Frame),
                text = "플레이어 메뉴"
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center")
        )
        self._component_manager.add_component(
            name = "file_select_label_frame",
            component = LabelFrame(
                self._component_manager.get_component("file_select_frame", Frame),
                text = "오디오 파일 선택"
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", ipadx = 10, ipady = 4)
        )

    def _set_label(self):
        self._component_manager.add_component(
            name = "audio_data_label",
            component = Label(
                self._component_manager.get_component("audio_data_label_frame", LabelFrame),
                text = "파일 이름 : 몰?루\n파일 형식 : 몰?루\n샘플링 : 몰?루\n길이 : 몰?루"
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", expand = True)
        )

    def _set_button(self):
        for idx, name in enumerate(_MENU_BTN_FRAME_NAMES):
            self._component_manager.add_component(
                name = f"test_button_{idx}",
                component = Button(
                    self._component_manager.get_component(name, Frame),
                    text = _MEDIA_CONTROL_SYMBOLS[idx],
                    command = getattr(self, _BTN_RELATED_COMMAND[idx])
                ),
                with_render = True,
                render_type = "pack",
                render_param = RenderParamWrapper(anchor = "center")
            )

    def _set_combobox(self):
        self._component_manager.add_component(
            name = "audio_file_select_combobox",
            component = Combobox(
                self._component_manager.get_component("file_select_label_frame", LabelFrame),
                values = self._py_audio_player.get_audio_file_dirs(),
                width = 48
            ),
            with_render = True,
            render_type = "pack",
            render_param = RenderParamWrapper(anchor = "center", pady = 10)
        )

    def _set_event_binder(self):
        component = self._component_manager.get_component("audio_file_select_combobox", Combobox)
        component.bind("<<ComboboxSelected>>", self._on_audio_file_select)

    def _on_audio_file_select(self, *args):
        self._py_audio_player.load_audio_file(self._get_current_selected_audio_file_name())

        update_result = self._component_manager.update_component(
            "audio_data_label",
            Label,
            **{"text": self._create_audio_file_data_string()}
        )

        if update_result is not None:
            messagebox.showinfo("에러 발생!", update_result.__str__())

    def _create_audio_file_data_string(self) -> str:
        data_string = (f"파일 이름 : {self._get_current_selected_audio_file_name()}\n"
                       f"파일 형식 : wav\n"
                       f"샘플링 : {self._py_audio_player.get_audio_file_sampling()}\n"
                       f"길이 : {self._py_audio_player.get_audio_file_length()}")

        return data_string

    def _get_current_selected_audio_file_name(self):
        return self._component_manager.get_component("audio_file_select_combobox", Combobox).get()

    @CatchException()
    def _audio_file_play(self):
        run(self._py_audio_player.play())

    @CatchException()
    def _audio_file_rplay(self):
        run(self._py_audio_player.play(reverse = True))

    @CatchException()
    def _audio_file_stop(self):
        run(self._py_audio_player.stop())

    @CatchException()
    def _show_audio_file_plot(self):
        PopUpGUI(self, player_instance = self._py_audio_player)


if __name__ == '__main__':
    PAP_GUI = PyAuidoPlayerGUI()
