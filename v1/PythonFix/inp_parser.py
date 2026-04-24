def split_into_blocks(lines):
    blocks = []
    current = []

    for line in lines:
        if line.lstrip().startswith("*") and current:
            blocks.append(current)
            current = [line]
        else:
            current.append(line)

    if current:
        blocks.append(current)

    return blocks

def keyword_of_block(block):
    first = block[0].strip().upper()
    if not first.startswith("*"):
        return "TEXT"
    return first.split(",")[0]
