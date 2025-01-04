import os
import time
from openai import OpenAI

class Generator:
    def __init__(self, voice="alloy", model="tts-1"):
        self.client = OpenAI()
        
        unix_timestamp_int = int(time.time())
        timestamp_str = str(unix_timestamp_int)
        self.generation_id = timestamp_str
        
        self.model = model
        self.voice = voice
    
    def output_file_name(self, dir_name, file_suffix):
        return f"./data/temp_audio/{dir_name}/{self.generation_id}_{file_suffix}.mp3"

    def generate_audio(self, text, dir_name, file_suffix):
        response = self.client.audio.speech.create(
            model=self.model,
            voice=self.voice,
            input=text
        )
        
        response.stream_to_file(self.output_file_name(dir_name, file_suffix))

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
    gen.generate_audio('И постарайтесь «прочесать» все тело. То есть, сознавайте, как отдельные части тела соприкасаются с полом.', "1")
    # gen.generate_audio('<duration=5>Goodbye, Alex</duration>', "2")
    
    # # Example usage:
    # input_path = "data/temp_audio/1728738759_1.mp3"  # Replace with your input file
    # output_path = "data/temp_audio/1728738759_1_slow.mp3"  # Replace with desired output file
    # desired_duration = 1.25  # Desired duration in seconds

    # change_audio_duration_with_pitch_correction(input_path, output_path, desired_duration)

        