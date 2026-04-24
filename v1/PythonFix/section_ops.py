from inp_parser import keyword_of_block

def block_contains(block, text):
    text = text.upper()
    return any(text in line.upper() for line in block)

def remove_blocks_by_keyword(blocks, keyword_names):
    kept = []
    removed = []

    keyword_names = {k.upper() for k in keyword_names}

    for block in blocks:
        key = keyword_of_block(block)
        if key in keyword_names:
            removed.append(f"Removed block with keyword {key}")
        else:
            kept.append(block)

    return kept, removed

def remove_blocks_containing(blocks, patterns):
    kept = []
    removed = []

    patterns = [p.upper() for p in patterns]

    for block in blocks:
        hit = False
        for p in patterns:
            if block_contains(block, p):
                removed.append(f"Removed block containing {p}: {block[0].strip()}")
                hit = True
                break
        if not hit:
            kept.append(block)

    return kept, removed
