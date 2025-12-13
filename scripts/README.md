# Scripts — Audio Processing Tools

This folder contains helper scripts used for preparing audio data
for the Zaan Koshur project.

These scripts define how raw audio recordings are converted into
standardized, AI-ready formats before being used in private datasets
or model training workflows.

## convert_to_wav.py

This script converts raw audio files into a consistent format suitable
for speech and language modeling.

Standard output format:
- WAV (PCM)
- 16 kHz sample rate
- Mono (single channel)

Supported input formats may include:
- .wav
- .mp3
- .m4a
- .flac
- .aac
- .ogg

## Privacy and Data Handling

Important notes regarding privacy:

- No audio files are stored in this repository.
- These scripts are NOT executed on GitHub.
- Raw and processed audio files are excluded via `.gitignore`.
- Audio processing is performed locally or within controlled,
  private environments (e.g., Hugging Face Spaces).
- Only approved and cleaned audio may later be uploaded to
  private datasets.

This design ensures contributor privacy, reproducibility,
and ethical data handling.
