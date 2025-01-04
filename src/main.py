import os
from pathlib import Path

from srt_parser import parse_srt_file
from audio_generator_openai import Generator
from joiner import merge_audios
from pause_cutter import detect_pauses_and_cut

# TODO: process each srt file in dir ./data/inputs
directory = Path('./data/inputs/')
extension = '.srt'  # Change to your desired file extension


def process_file(srt_file_path):
    base_name = Path(file_path).stem

    phrases_list = parse_srt_file(srt_file_path)
    gen = Generator(voice='onyx', model='tts-1-hd')
    audio_files = []

    temp_directory = Path(f"./data/temp_audio/{base_name}/")
    temp_directory.mkdir(parents=True, exist_ok=True)
    
    idx = 1
    # Print the results
    prefix = os.environ.get('AI_AUDIO_GEN_PREFIX_TEXT') # or 'Далее идет текст на русском, диктор говорит очень спокойно и размеренно, текст о теле: [pause 2s] />... - - - '
    # gen.generate_audio(prefix, str(idx))

    for phrase in phrases_list:
        print(phrase)
        gen.generate_audio(prefix+phrase['text'], base_name, str(idx))
        audio_path = f"./data/temp_audio/{base_name}/{gen.generation_id}_{idx}.mp3"
        segment, longest_pause = detect_pauses_and_cut(audio_path)

        # Output longest pause details
        start_longest_pause, end_longest_pause = longest_pause
        print(f"Longest pause starts at {start_longest_pause:.2f}s and ends at {end_longest_pause:.2f}s, duration: {end_longest_pause - start_longest_pause:.2f}s")

        audio_path_out = f"./data/temp_audio/{base_name}/{gen.generation_id}_{idx}_last_segment.mp3"
        # Save each segment to a new file
        segment.export(audio_path_out, format="mp3")
        audio_files.append((audio_path_out, phrase['time_to_start_seconds']))
        idx += 1

    output_file = f"./data/{base_name}_{gen.generation_id}_merged_output.mp3"
    merge_audios(audio_files, output_file)
    print(f"Merged audio saved to {output_file}")


for file_path in directory.glob(f'*{extension}'):
    if file_path.is_file():
        process_file(file_path)
