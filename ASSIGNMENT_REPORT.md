# ASSIGNMENT 3
## TEXT ENCODING AND DECODING PROGRAM USING THE CAESAR CIPHER

**Student Name:** GODFRED TOKU ASSIAMAH 
**Index Number:** 10353222 
**Programme/Class:** EVENING 2  


---

## 1. Introduction

Encoding and decoding are important concepts in computer science and information security. Encoding transforms information into another form, while decoding converts the transformed information back into a readable form. This assignment presents a Python program that performs text encoding and decoding using the Caesar Cipher algorithm.

## 2. Aim and Objectives

The aim is to develop a working text encoder and decoder.

The objectives are to:
1. Understand the basic concept of text encryption and decryption.
2. Implement the Caesar Cipher algorithm using Python.
3. Allow users to encode and decode messages with a numerical shift key.
4. test the program with different messages and shift values.
5. demonstrate how an algorithm can be translated into a working computer program.

## 3. Algorithm Selected: Caesar Cipher

The Caesar Cipher is a classical substitution cipher. It replaces each alphabetic character with another character a fixed number of positions away in the alphabet.

For example, with a shift key of 3:
- A becomes D
- B becomes E
- C becomes F
- X becomes A
- Y becomes B
- Z becomes C

The same key is used for encoding and decoding. Encoding shifts letters forward; decoding shifts them backward.

**Encoding formula:**

`C = (P + K) mod 26`

**Decoding formula:**

`P = (C - K) mod 26`

Where:
- `P` represents the original letter position.
- `C` represents the encoded letter position.
- `K` represents the shift key.
- `mod 26` keeps the result within the 26-letter English alphabet.

## 4. Program Design / Pseudocode

```text
START
    Display program title
    REPEAT
        Display menu:
            1. Encode
            2. Decode
            3. Exit
        Read user's choice

        IF choice is 1
            Read message
            Read shift key
            Shift each letter forward by the key
            Display encoded message
        ELSE IF choice is 2
            Read encoded message
            Read shift key
            Shift each letter backward by the key
            Display decoded message
        ELSE IF choice is 3
            Display exit message
        ELSE
            Display invalid choice message
        END IF
    UNTIL choice is 3
STOP
```

## 5. Implementation

The program is implemented in Python 3. It uses:
- `ord()` to obtain the numerical position of a character.
- `chr()` to convert a numerical position back to a character.
- The modulo operator (`%`) to wrap shifts around the alphabet.
- A function named `caesar_cipher()` to perform the transformation.
- A menu to let the user choose encoding, decoding or exiting.

The complete source code is in `text_encoder_decoder.py`.

## 6. Sample Execution

**Encoding**

```text
Enter the text to encode: HELLO WORLD
Enter the shift key (whole number): 3

ENCODED MESSAGE: KHOOR ZRUOG
```

**Decoding**

```text
Enter the text to decode: KHOOR ZRUOG
Enter the shift key (whole number): 3

DECODED MESSAGE: HELLO WORLD
```

## 7. Testing and Results

| Test | Input | Key | Expected result |
|---|---|---:|---|
| Encode uppercase | HELLO | 3 | KHOOR |
| Decode uppercase | KHOOR | 3 | HELLO |
| Encode lowercase | hello | 3 | khoor |
| Preserve spaces | HELLO WORLD | 3 | KHOOR ZRUOG |
| Preserve punctuation | Hello! | 3 | Khoor! |
| Wrap around alphabet | XYZ | 3 | ABC |
| Zero shift | ABC | 0 | ABC |
| Large shift | ABC | 29 | DEF |

The program is designed to preserve the case of letters and leave spaces, numbers and punctuation unchanged. It also accepts negative and large integer keys because shifts are normalized using modulo 26.

## 8. Advantages and Limitations

### Advantages
- Simple to understand and implement.
- Demonstrates functions, loops, conditions and string processing.
- Supports uppercase and lowercase text.
- Preserves spaces, numbers and punctuation.
- Allows different integer shift keys.

### Limitations
- It is not secure for modern communication.
- It has only 26 effective shift possibilities.
- A person can easily try every possible key to recover the message.
- It is intended for learning algorithm implementation, not protecting sensitive data.

## 9. Conclusion

The assignment successfully demonstrates the development of a text encoding and decoding program using Python. The Caesar Cipher algorithm was implemented to shift alphabetic characters forward during encoding and backward during decoding. Testing examples demonstrate that an encoded message can be restored to its original form when the correct key is used.

This project improved understanding of algorithms, Python functions, loops, conditional statements, character conversion and basic cryptography.

## 10. References

1. Python Software Foundation. *Python 3 Documentation*. https://docs.python.org/3/
2. Encyclopaedia Britannica. *Cryptology: Caesar cipher and substitution ciphers*. https://www.britannica.com/topic/cryptology
