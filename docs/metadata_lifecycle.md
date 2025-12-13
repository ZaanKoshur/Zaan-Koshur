# Metadata Lifecycle — Zaan Koshur

This document defines how metadata entries are created, validated,
and maintained for the Zaan Koshur dataset.

The goal is to ensure consistency, privacy, and scalability as the
dataset grows.

---

## 1. Speaker Metadata Lifecycle (speakers.csv)

- One speaker corresponds to exactly one `speaker_id`.
- A speaker entry is created only once.
- Speaker metadata is added when:
  - valid consent is obtained
  - at least one audio clip is approved

### Rules
- Speaker IDs must be unique.
- Duplicate speaker entries are not allowed.
- Speaker entries are never created for rejected submissions.

---

## 2. Clip Metadata Lifecycle (clips.csv)

- One row represents one accepted audio clip.
- Clip metadata is added only after:
  - audio format standardization
  - transcription verification
  - quality evaluation

### Rules
- Each clip must reference a valid `speaker_id`.
- Clips without transcriptions are not added.
- Rejected clips are never written to metadata.

---

## 3. Quality Control Rules

Each audio clip is assigned a `quality_rating` from 1 to 5:

- 1 — unusable
- 2 — poor quality
- 3 — acceptable
- 4 — good
- 5 — excellent

### Inclusion Rule
- Only clips with `quality_rating >= 3` are eligible for dataset use.

---

## 4. Rejection Conditions

A clip is rejected if:
- audio is silent or unintelligible
- duration is extremely short or excessively long
- transcription does not match the spoken content
- background noise overwhelms speech
- consent is missing or withdrawn

Rejected clips are discarded and not recorded in metadata.

---

## 5. Certificate Eligibility (Future Use)

Certificates are generated based on accepted clip counts.

Example logic:
- Count accepted clips per speaker
- Issue certificates after defined thresholds (e.g., 10, 50, 100 clips)

Certificate generation relies exclusively on metadata, not raw audio.

---

## 6. Privacy and Ethics

- Metadata must not contain personally identifiable information.
- Speaker identities remain anonymous.
- Metadata must never enable re-identification of contributors.

All metadata practices must comply with CONSENT.txt and LICENSE terms.

---

## 7. Withdrawal Handling

If a contributor requests removal:
- Associated audio files are deleted
- Corresponding metadata entries are removed where feasible
- No further processing is performed for that speaker
