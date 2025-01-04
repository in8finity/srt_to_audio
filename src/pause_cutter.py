from pydub import AudioSegment
import librosa
import numpy as np

def detect_pauses_and_cut(audio_path, threshold_db=-50, min_pause_duration=0.5):
    # Load audio using librosa to work with decibel levels
    y, sr = librosa.load(audio_path, sr=None)
    audio_segment = AudioSegment.from_file(audio_path)
    frame_duration = 0.1  # Duration of each frame in seconds
    frame_length = int(frame_duration * sr)
    pauses = []
    start_pause = None
    longest_pause = (0, 0)  # Initialize start and end of longest pause

    for i in range(0, len(y), frame_length):
        frame = y[i:i+frame_length]
        rms_db = librosa.amplitude_to_db([np.sqrt(np.mean(frame**2))])
        # Check if frame is below threshold and potential pause is long enough
        if rms_db < threshold_db:
            if start_pause is None:
                start_pause = i / sr
                #print(f"below thershold - starting pause at {start_pause}")
        else:
            if start_pause is not None:
                
                end_pause = i / sr
                #print(f"abowe thershold - finishing pause at {end_pause}")
                duration_pause = end_pause - start_pause
                if duration_pause >= min_pause_duration:
                    pauses.append((start_pause, end_pause))
                    # Update longest pause if this one is longer
                    if duration_pause > (longest_pause[1] - longest_pause[0]):
                        longest_pause = (start_pause, end_pause)
                start_pause = None

    segment = audio_segment[longest_pause[1] * 1000:]
    return segment, longest_pause

if __name__ == "__main__":
    # Usage
    audio_path = "data/temp_audio/1730572233_1.mp3"
    segment, longest_pause = detect_pauses_and_cut(audio_path)

    # Output longest pause details
    start_longest_pause, end_longest_pause = longest_pause
    print(f"Longest pause starts at {start_longest_pause:.2f}s and ends at {end_longest_pause:.2f}s, duration: {end_longest_pause - start_longest_pause:.2f}s")

    # Save each segment to a new file
    segment.export(f"data/temp_audio/1730572233_1_last_segment.mp3", format="mp3")