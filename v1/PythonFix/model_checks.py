from collections import Counter
from inp_parser import keyword_of_block

def summarize_blocks(blocks):
    counts = Counter(keyword_of_block(b) for b in blocks)
    for key, value in sorted(counts.items()):
        print(f"{key}: {value}")
