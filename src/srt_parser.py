import re
from datetime import timedelta

def parse_srt_time(time_str):
    """Convert SRT time format (HH:MM:SS,ms) to seconds."""
    time_parts = re.split(r'[:,]', time_str)
    hours, minutes, seconds, milliseconds = map(int, time_parts)
    total_seconds = timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds).total_seconds()
    return total_seconds

def parse_srt_file(file_path):
    """Parse the SRT file and split it into a list of dictionaries."""
    subtitles = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split based on empty lines which separate each subtitle block
    blocks = re.split(r'\n\n+', content.strip())
    
    for block in blocks:
        lines = block.split('\n')
        
        if len(lines) >= 3:
            # The second line should contain the time info in SRT format
            time_info = lines[1]
            start_time_str, end_time_str = time_info.split(' --> ')
            start_time_sec = parse_srt_time(start_time_str)
            end_time_sec = parse_srt_time(end_time_str)
            length_in_seconds = end_time_sec - start_time_sec
            
            # Join the rest of the lines for the subtitle text
            text = ' '.join(lines[2:])
            
            subtitle = {
                'text': text,
                'time_to_start_seconds': start_time_sec,
                'length_seconds': length_in_seconds
            }
            subtitles.append(subtitle)
    
    return subtitles


if __name__ == "__main__":
    # Example usage
    srt_file_path = './data/inputs/lesson1.srt'  # Replace with the path to your SRT file
    subtitles_list = parse_srt_file(srt_file_path)

    # Print the results
    for subtitle in subtitles_list:
        print(subtitle)
