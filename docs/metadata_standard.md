🗂 Metadata Standard — Zaan Koshur

This document defines the official metadata structure for the Zaan Koshur dataset, including speaker IDs, file naming conventions, CSV formats, and ethical requirements. These standards ensure that all recordings remain consistent, anonymous, and usable for ASR, TTS, and other NLP tasks.

⭐ 1. Speaker ID Format (Professional Region-Based System)

Zaan Koshur uses a region-coded anonymized speaker ID, following this pattern:

KS-XXX-NNN


Where:

KS → Kashmiri (language code)

XXX → District code

SGR = Srinagar

BAR = Baramulla

ANG = Anantnag

PUL = Pulwama

GAW = Ganderbal

BUD = Budgam

KUP = Kupwara

SHP = Shopian

BAN = Bandipora

KUL = Kulgam

KTR - Kishtwar (optional regions)

DPL = Doda 

NNN → Speaker number (001, 002, 003 …)

✔ Examples:
KS-SGR-001
KS-ANG-005
KS-BAR-014
KS-KUP-022
KS-BUD-009

✔ Advantages:

Highly professional

Represents dialect diversity

Scales to >10,000 speakers

Still 100% anonymous

Research-friendly

⭐ 2. Audio File Naming Format

Each speaker has multiple clips. Use:

KS-XXX-NNN_YYY.wav


Where:

KS-XXX-NNN → speaker ID

YYY → clip number (001, 002, 003 …)

✔ Example:
KS-SGR-001_001.wav
KS-SGR-001_002.wav
KS-ANG-005_017.wav

Audio Requirements:

WAV

PCM 16-bit

Mono

16 kHz sample rate

⭐ 3. Metadata Folder Structure
metadata/
   speakers.csv      → speaker-level metadata
   clips.csv         → clip-level metadata


Optional:

metadata/
   dataset_readme.md

⭐ 4. Speaker Metadata Format (speakers.csv)

Each row describes one speaker.

Field                              	Description                    	           Example
speaker_id                        	region-based ID                         	KS-SGR-001
gender	                          male / female / other	                        female
age_group                      	7–12, 13–17, 18–25, 26–40, 40+	                18–25
district	                          home district	                             Srinagar
accent_type                    	specific locality/dialect	                     Downtown
environment                   	quiet / indoor / mild-noise / outdoor          	quiet
device	                         microphone/phone used                         Motorola
notes	                              optional comments                        	slight echo   

✔ Example Entry:
speaker_id,gender,age_group,district,accent_type,environment,device,notes
KS-SGR-001,female,18-25,Srinagar,Downtown,quiet,iPhone 12,None

⭐ 5. Clip Metadata Format (clips.csv)

Each row describes one audio clip.

Field                            	Description	                               Example
file_name	                        audio file	                          KS-SGR-001_003.wav
speaker_id                      	who recorded it                         	KS-SGR-001
text                              transcription                             	مۍ چُھ آوان
duration_seconds	                clip length	                                2.14
environment	                      recording conditions	                      quiet
quality_rating                     	1–5 (human review)                        	4


✔ Example Entry:
file_name,speaker_id,text,duration_seconds,environment,quality_rating
KS-SGR-001_003.wav,KS-SGR-001,مۍ چُھ آوان,1.84,quiet,5

⭐ 6. CSV Formatting Rules

To ensure compatibility with AI tooling:

UTF-8 encoding

Comma-separated values

No trailing commas

First row = header

No extra spaces

Transcriptions must follow transcription_rules.md

⭐ 7. Ethical Metadata Requirements

To protect all contributors:

No personal names

No phone numbers or addresses

No village ID if too specific

No sensitive demographic data

Region codes are safe and common in linguistic research

All audio stored in private HuggingFace Gated Dataset

Access granted only by project owner

Linked documents:

LICENSE

CONSENT.txt

⭐ 8. Versioning Standard

Each dataset release follows semantic versioning:

v0.1  → internal testing dataset  

v0.2  → expanded speaker count 

v0.9  → pre-release  

v1.0  → public dataset (if approved)


Each version must include:

speakers.csv

clips.csv

transcription rules version

license

changelog

integrity checks

📘 End of Metadata Standard (Zaan Koshur)

Updates and improvements will be documented in this file.
