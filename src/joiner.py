from pydub import AudioSegment

import os

def merge_audios(audio_info, output_path, background_color=(0, 0, 0)):
    """
    Merges multiple audio files into one, placing each at the specified start time.

    Parameters:
    - audio_info: List of tuples [(file_path, start_time_in_seconds), ...]
    - output_path: Path to save the merged audio file
    - background_color: RGB tuple for the background silence (optional)
    """
    # Load all audio files and determine their end times
    audios = []
    end_times = []
    for file_path, start_time in audio_info:
        audio = AudioSegment.from_file(file_path)
        audios.append((audio, start_time * 1000))  # pydub works in milliseconds
        end_time = (start_time * 1000) + len(audio)
        end_times.append(end_time)
    
    # Determine the total duration required for the final audio
    total_duration = max(end_times)
    
    # Create a silent audio segment with the total duration
    # pydub's silence is mono by default; adjust if needed
    # To handle stereo or other channels, you might need to set frame rate and channels
    final_audio = AudioSegment.silent(duration=total_duration, frame_rate=audios[0][0].frame_rate)
    
    # Overlay each audio at the specified start time
    for audio, start_time in audios:
        final_audio = final_audio.overlay(audio, position=start_time)
    
    # Export the final merged audio
    final_audio.export(output_path, format=os.path.splitext(output_path)[1][1:])  # Format inferred from extension

if __name__ == "__main__":
    # Example usage:
    # List of (file_path, start_time_in_seconds)
    audio_files = [
        ("./data/temp_audio/1728654162_1.mp3", 0),       # Starts at 0 seconds
        ("./data/temp_audio/1728654162_2.mp3", 5),    
        # Add more files as needed
    ]
    
    output_file = "./data/1728654162_merged_output.mp3"
    
    merge_audios(audio_files, output_file)
    print(f"Merged audio saved to {output_file}")