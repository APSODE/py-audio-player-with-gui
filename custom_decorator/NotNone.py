from typing import Callable


class NotNone:
    def __init__(self, field_name: str):
        self._field_name = field_name

    def __call__(self, method: Callable):
        def wrapper(instance, *args, **kwargs):
            field_value = getattr(instance, self._field_name)
            if field_value is not None:
                return method(instance, *args, **kwargs)
            else:
                error_msg = ""

                if self._field_name == "_loaded_file":
                    error_msg = error_msg.join("오디오 파일을 load하지 않고 해당 기능은 실행 할 수 없습니다.")

                elif self._field_name in ["_audio_manager", "_audio_thread"]:
                    error_msg = error_msg.join("오디오 파일을 play하지 않고 해당 기능은 실행 할 수 없습니다.")

                else:
                    error_msg = error_msg.join(f"{self._field_name}이 None인 상태에서 사용할 수 없습니다.")

                raise ValueError(error_msg)

        return wrapper
