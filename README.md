🌿 Zaan Koshur

Know Kashmiri. Preserve Kashmiri.

An open-source initiative to document, protect, and revive the Kashmiri language through community voices, linguistic research, and modern AI technologies.

🧭 About the Project

Zaan Koshur is a community-driven Kashmiri language preservation effort aimed at creating the first large-scale, openly available Kashmiri speech dataset, text corpus, and AI-ready linguistic resources.

Kashmiri is one of the oldest languages of the region, rich in poetry, culture, and oral heritage. Yet today, it is spoken less, documented rarely, and underrepresented in digital and research spaces.
Zaan Koshur exists to change that.

This repository provides the foundational structure for building datasets, defining linguistic rules, ensuring ethical data collection, and supporting research for:

Speech Recognition (ASR)

Text-to-Speech (TTS)

Natural Language Processing (NLP)

Transliteration tools

Language learning applications

Digital archives & cultural preservation

Our goal is simple but powerful:

To ensure Kashmiri survives, grows, and thrives in the digital age.


📂 Repository Structure

This repository follows a clean, scalable structure used in professional dataset projects:

ZaanKoshur/
 ├── audio_raw/           # Unprocessed recordings (private or internal only)
 
 ├── audio_clean/         # Cleaned, trimmed, 16 kHz mono WAV files
 
 ├── transcriptions/      # Text transcripts for each audio file
 
 ├── metadata/            # Speaker metadata, dataset splits, CSVs
 
 ├── docs/                # Documentation, rules, contribution guides
 
 ├── scripts/             # Processing and utility scripts
 
 ├── README.md
 
 ├── LICENSE
 
 ├── CONSENT.txt
 
 └── .gitignore
 
This structure ensures easy scaling for thousands of files and compatibility with research tools.

🗣️ Dataset Components

Zaan Koshur datasets will eventually include:

1. Speech Data

Smooth, clean voice recordings

Multiple speakers (gender, age, district diversity)

Short sentences, phrases, words, and natural speech

Clean 16 kHz mono WAV format

Fully anonymized

2. Text Corpus

Traditional and modern Kashmiri vocabulary

Phrases, idioms, proverbs

Sample dialogues

Story fragments

High-quality spelling rules

3. Annotations & Metadata

Each audio file will include metadata such as:

Speaker ID (anonymous)

District / region

Age group

Gender

Recording environment

Transcript text

File duration

✍️ Transcription Rules

To maintain consistency, Zaan Koshur uses standardized guidelines for writing Kashmiri.
These rules will be stored in docs/transcription_rules.md and include:

Chosen script: Perso-Arabic

Lowercase usage standard

No punctuation unless required

Representation of fillers, hesitations, background noises

Standardized spellings for common terms

Transparent rules ensure that independent contributors produce consistent data.

🔐 Ethical Data Collection & Privacy

Zaan Koshur follows strict ethical standards:

All contributions are fully anonymous.

No names, personal details, or identifying information are collected.

Voices are used only for language preservation and open research.

Consent is required for every recording.

Contributors may request removal at any time.

A detailed consent form is provided in CONSENT.txt.

🤖 Long-Term Vision

Zaan Koshur aims to enable:

✔ Kashmiri Speech-to-Text (ASR)

✔ Kashmiri Text-to-Speech (TTS) voices

✔ Translation tools

✔ Kashmiri grammar & spell-check tools

✔ Online language-learning apps

✔ A complete digital archive of Kashmiri speech & text

✔ Open-source access for researchers, students, and the community

This project is designed to grow into a full digital ecosystem for the Kashmiri language.

🤝 How to Contribute (Phase 2 Launch)

Public contributions are not yet open.
In Phase 2, we will launch:

A voice contribution portal

A public upload system

Certificates for contributors

Clear submission guidelines

Until then, you can follow updates at:
📌 Instagram: [@zaankoshur]

🛠️ Technical Standards
Audio Requirements

WAV PCM 16-bit

16 kHz mono

File naming: spk01_001.wav

Length: 1–10 seconds

File Organization

Each speaker's recordings will be grouped and labeled for compatibility with ASR training pipelines (Whisper, Wav2Vec2, MMS, etc.).

📜 License

The dataset and associated resources will be released under:

Creative Commons Attribution 4.0 (CC-BY-4.0)

with ethical use guidelines regarding privacy and cultural respect.

This supports open research while protecting contributors.

🌍 Why Zaan Koshur Matters

Kashmiri has survived centuries through oral tradition.
But without digital representation, it risks fading in a world dominated by global languages.
By building open, community-driven language data and tools, we ensure our heritage continues to live—not only in memory, but in technology, education, and future generations.

❤️ Join the Mission

If you believe Kashmiri deserves protection, revival, and global representation, this project welcomes you.

Together, we build Zaan.
Together, we save Koshur.

📬 Contact

For collaborations, questions, or suggestions:
📧 Email: zaankoshur@gmail.com
📸 Instagram: @zaankoshur

🔚 End of README

