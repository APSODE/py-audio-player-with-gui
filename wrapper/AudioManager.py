from pyaudio import PyAudio, Stream
from wrapper.LoadedAudioFile import LoadedAudioFile


class AudioManager(PyAudio):
    def __init__(self, loaded_audio_file: LoadedAudioFile):
        super().__init__()
        self._loaded_audio_file: LoadedAudioFile = loaded_audio_file
        self._audio_stream: Stream = self._create_audio_stream()
        self._is_playing: bool = False

    @staticmethod
    def create_manager(loaded_audio_file: LoadedAudioFile) -> "AudioManager":
        return AudioManager(loaded_audio_file = loaded_audio_file)

    def _field_initialization(self):
        self._loaded_audio_file.file.setpos(0)
        self._audio_stream = self._create_audio_stream()
        self._is_playing = False

    def _create_audio_stream(self) -> Stream:
        return self.open(
            format = self.get_format_from_width(self._loaded_audio_file.file.getsampwidth()),
            channels = self._loaded_audio_file.file.getnchannels(),
            rate = self._loaded_audio_file.file.getframerate(),
            output = True
        )

    def play(self, reverse: bool = False):
        self._is_playing = True

        r_count = 1
        nframe = 1024

        if reverse:
            self._loaded_audio_file.file.setpos(self._loaded_audio_file.file.getnframes() - (r_count * nframe))

        while len(audio_data := self._loaded_audio_file.file.readframes(nframe)):
            if self._is_playing:
                self._audio_stream.write(audio_data)

                if reverse:
                    r_count += 1

                    if self._loaded_audio_file.file.getnframes() - (r_count * nframe) < 0:
                        break

                    else:
                        self._loaded_audio_file.file.setpos(
                            self._loaded_audio_file.file.getnframes() - (r_count * nframe)
                        )

        self._stop()
        self.terminate()

    def _stop(self):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self._field_initialization()

    def stop(self):
        self._is_playing = False
