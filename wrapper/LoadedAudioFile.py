from wave import Wave_read
from wave import open as wv_open
from wrapper.LibrosaWrapper import LibrosaWrapper


class LoadedAudioFile:
    def __init__(self, wav_file_dir: str):
        self._wav_file = wv_open(wav_file_dir, "rb")
        self._librosa_wrapper = LibrosaWrapper.create_object(wav_file_dir = wav_file_dir)
        self._length = self._get_length()
        self._sampling_rate = self._get_sampling_rate()

    @staticmethod
    def create_object(wav_file_dir: str) -> "LoadedAudioFile":
        return LoadedAudioFile(wav_file_dir = wav_file_dir)

    def _get_length(self) -> float:
        return round(self._wav_file.getnframes() / self._wav_file.getframerate(), 2)

    def _get_sampling_rate(self) -> float:
        return self._wav_file.getframerate() / 1000

    @property
    def file(self) -> Wave_read:
        return self._wav_file

    @property
    def length(self):
        return self._length

    @property
    def sampling_rate(self) -> float:
        return self._sampling_rate

    @property
    def librosa(self) -> LibrosaWrapper:
        return self._librosa_wrapper

    def sampling_with_format(self) -> str:
        return f"{self._sampling_rate}KHz"

    def length_with_format(self) -> str:
        minute = int(self._length // 60)
        second = int(self._length - (60 * minute))

        return f"{minute}분 {second}초"
