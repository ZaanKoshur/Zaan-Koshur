# Quality and Validation Rules — Zaan Koshur

This document defines the validation and quality control process
for audio clips contributed to the Zaan Koshur dataset.

The goal is to ensure high-quality, ethical, and reliable data
before any clip is included in the dataset.

---

## 1. Validation Stages

Each audio clip passes through the following stages:

1. Format validation
2. Duration validation
3. Transcription validation
4. Audio quality review
5. Ethical and privacy review

Only clips that pass all stages are accepted.

---

## 2. Format Validation (Automatic)

An audio clip must meet the following technical requirements:

- File format: WAV (PCM)
- Sample rate: 16 kHz
- Channels: Mono (1)

Clips failing format validation are rejected.

---

## 3. Duration Validation (Automatic)

Recommended duration range:
- Minimum: 1 second
- Maximum: 12 seconds

Clips outside this range may be rejected unless explicitly approved.

---

## 4. Transcription Validation (Manual or Semi-Manual)

A clip is rejected if:
- Transcription is missing
- Transcription does not match spoken content
- Words are clearly misheard or incorrect

Minor pronunciation variations are acceptable if meaning is preserved.

---

## 5. Audio Quality Review (Human)

Each clip is reviewed for:

- Speech clarity
- Background noise level
- Distortion or clipping
- Overall intelligibility

---

## 6. Quality Rating Scale

Each accepted clip is assigned a `quality_rating` from 1 to 5:

- 1 — Unusable
- 2 — Poor quality
- 3 — Acceptable
- 4 — Good
- 5 — Excellent

Only clips with a rating of **3 or higher** are eligible for dataset use.

---

## 7. Ethical and Privacy Review

A clip is rejected if it contains:

- Personally identifiable information
- Attempts at self-identification
- Sensitive personal details
- Disrespectful or harmful language
- Content violating CONSENT.txt

---

## 8. Rejection Policy

Rejected clips:

- Are not stored in the dataset
- Are not written to metadata
- Do not count toward certificates
- May be permanently deleted

---

## 9. Acceptance Policy

Accepted clips:

- Are stored in private datasets
- Are recorded in `clips.csv`
- Count toward contributor certificates
- May be used for model training and research

---

## 10. Final Authority

The project maintainer retains final authority
over acceptance or rejection decisions.

All validation decisions must align with
CONSENT.txt and LICENSE terms.
