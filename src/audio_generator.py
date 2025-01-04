import os
import time

from elevenlabs.client import ElevenLabs
from elevenlabs.core import RequestOptions
from elevenlabs import save

class Generator:
    def __init__(self, voice='Brian', model='eleven_multilingual_v2'):
        self.client = ElevenLabs(
            api_key=os.environ['ELEVENLABS_API_KEY']
        )
        unix_timestamp_int = int(time.time())
        timestamp_str = str(unix_timestamp_int)
        self.generation_id = timestamp_str
        
        self.model = model
        self.voice = voice

    def generate_audio(self, text, dir_name, file_suffix, previous_text="", next_text=""):
        opts = RequestOptions()
        opts['additional_query_parameters'] = {"next_text": "he said slowly", "previous_text": "he said slowly"}
        audio = self.client.generate(
            text=text,
            voice=self.voice,
            model=self.model,
            request_options=opts
            )
        save(audio, f"./data/temp_audio/{dir_name}/{self.generation_id}_{file_suffix}.mp3")

if __name__ == "__main__":
    # import logging
    # import contextlib
    # from http.client import HTTPConnection
    # HTTPConnection.debuglevel = 1

    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True
    
    gen = Generator()
    gen.generate_audio('Hello, Alex', "1")
    # gen.generate_audio('<duration=5>Goodbye, Alex</duration>', "2")
    
    # # Example usage:
    # input_path = "data/temp_audio/1728738759_1.mp3"  # Replace with your input file
    # output_path = "data/temp_audio/1728738759_1_slow.mp3"  # Replace with desired output file
    # desired_duration = 1.25  # Desired duration in seconds

    # change_audio_duration_with_pitch_correction(input_path, output_path, desired_duration)

        