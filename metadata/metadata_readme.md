# Metadata Documentation — Zaan Koshur

This folder contains all metadata related to the Zaan Koshur speech
dataset, including speaker information, clip-level details, and internal
dataset organization files.

## Files in this directory

### 1. speakers.csv
Information about each speaker:
- speaker_id (KS-XXX-NNN format)
- gender
- age_group
- district
- accent_type
- environment
- device
- notes

### 2. clips.csv
Information about each audio clip:
- file_name (KS-XXX-NNN_YYY.wav)
- speaker_id
- text
- duration_seconds
- environment
- quality_rating

## Purpose of Metadata
Metadata ensures:
- anonymity of speakers  
- accurate pairing of audio and transcriptions  
- balanced regional and demographic coverage  
- reproducibility for research  
- support for training ASR, TTS, and NLP models  

## How Metadata Is Used
Training pipelines use metadata to:
- load correct audio files  
- associate each clip with its transcription  
- split dataset by speaker, region, gender  
- evaluate performance on diverse subsets  

## Extending Metadata
If new metadata fields are needed:
- update this document  
- update metadata_standard.md  
- reflect changes in speakers.csv and clips.csv  

All contributions must follow privacy and ethical guidelines in CONSENT.txt.
