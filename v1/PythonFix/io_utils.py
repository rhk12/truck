def read_inp(filename):
    with open(filename, "r") as f:
        return f.readlines()

def write_inp(filename, blocks):
    with open(filename, "w") as f:
        for block in blocks:
            for line in block:
                f.write(line)
