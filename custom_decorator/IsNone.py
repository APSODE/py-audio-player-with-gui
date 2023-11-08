from typing import Callable


class IsNone:
    def __init__(self, field_name: str):
        self._field_name = field_name

    def __call__(self, method: Callable):
        def wrapper(instance, **kwargs):
            field_value = getattr(instance, self._field_name)
            if field_value is None:
                return method(instance, **kwargs)

            else:
                error_msg = ""

                if self._field_name == "_audio_thread":
                    error_msg = error_msg.join("오디오 파일을 재생하는 도중에 다시 오디오 파일을 재생할 수 없습니다.")

                else:
                    error_msg = error_msg.join(f"{self._field_name}이 None이 아닌 상태에서 사용할 수 없습니다.")

                raise ValueError(error_msg)

        return wrapper
