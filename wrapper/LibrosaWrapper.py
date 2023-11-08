from librosa import load as rosa_load
from numpy import ndarray


class LibrosaWrapper:
    def __init__(self, wav_file_dir: str):
        self._librosa_tuple = rosa_load(wav_file_dir, mono = False)

    @staticmethod
    def create_object(wav_file_dir: str) -> "LibrosaWrapper":
        return LibrosaWrapper(wav_file_dir = wav_file_dir)

    @property
    def signal(self) -> ndarray:
        return self._librosa_tuple[0]

    @property
    def sampling_rate(self) -> float:
        return self._librosa_tuple[1]
