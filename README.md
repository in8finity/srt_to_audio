# SRT to MP3 AI based converter

## How it works

1. Parse SRT: extracting texts to be said at specified moment of time
2. Make audio from texts (using specific intro/prefix text to make speech clear and with good pace)
3. Split the intro and main speech by long pause between them
4. Join extracted main speech parts according the time from srt files

## How to use

### Using docker and make

Check if make is installed 

```bash
➜  ~ make -v
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
```

You will need the docker and docker-compose installed to run converter.
Make sure if they are installed. 
You must set some constants in env.dev:
```
ELEVENLABS_API_KEY='...'
OPENAI_API_KEY='...'
AI_AUDIO_GEN_PREFIX_TEXT='Далее идет текст на русском, диктор говорит очень спокойно и размеренно, текст о теле: [pause 2s] />... - - - '
```
Then just use
```bash
make run
```

to convert all `./data/inputs/*.srt` files into audio


### Just in console

instal required dependencies: 
1. python3
2. pip
2. ffmpeg
3. libs from requirements.txt (with `pip install -r requirements.txt`)


### For development

TODO:

## Key modules

- srt_parser - responsble for converting .srt file into list of dictionaries like this: "{'text': 'Таз, тазобедренные суставы, левый и правый.', 'time_to_start_seconds': 65.07, 'length_seconds': 4.200000000000003}"
- audio_generator_* - responsible for converting texts into audio using specific AI enginge, for now OpenAI and ElevenLabs are supported
- pause_cutter - detects the pause between intro and main part, then it extracts the main part in separate file
- joiner - assembles the final audio by time_to_start_seconds marks
