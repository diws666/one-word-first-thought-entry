# This file IS the entry. WORD below is the complete entry and is written
# byte-for-byte to /output/entry.txt — it must stay byte-identical:
# exactly "kaleidoscope", no trailing newline, no extra whitespace.
WORD = "kaleidoscope"

with open("/output/entry.txt", "w") as f:
    f.write(WORD)
