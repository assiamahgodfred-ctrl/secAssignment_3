# Assignment 3 — Text Encoder and Decoder

**Language:** Python 3  
**Algorithm:** Caesar Cipher

## Project description
This program encodes and decodes text using the Caesar Cipher. The user chooses an operation and enters a numerical shift key. Encoding shifts letters forward through the alphabet; decoding shifts them backward.

## Requirements
- Python 3.8 or later
- No third-party packages are required

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python text_encoder_decoder.py
```

On some Windows installations, use:

```bash
py text_encoder_decoder.py
```

## How it works
For encoding, each letter is shifted forward by the key. For decoding, the same operation is performed with the negative key. The modulo operation (`% 26`) ensures that the shift wraps around the alphabet.

For a letter represented by a position from 0 to 25:

`Encoded position = (Original position + Shift) % 26`

Decoding uses:

`Decoded position = (Encoded position - Shift) % 26`

The program preserves uppercase and lowercase letters. Spaces, punctuation, numbers and other non-letter characters remain unchanged.

## Example
- Original text: `HELLO WORLD`
- Shift key: `3`
- Encoded text: `KHOOR ZRUOG`
- Decoded text with key `3`: `HELLO WORLD`

## Important security note
The Caesar Cipher is a classical educational cipher. It is not suitable for protecting confidential information because there are only 26 possible letter shifts and it can be broken easily.

## Files
- `text_encoder_decoder.py` — complete Python source code
- `ASSIGNMENT_REPORT.md` — assignment write-up, algorithm, tests and conclusion
