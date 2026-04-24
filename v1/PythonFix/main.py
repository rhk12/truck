from io_utils import read_inp, write_inp
from inp_parser import split_into_blocks
from rewrite_rules import clean_model
from model_checks import summarize_blocks

def main():
    input_file = "../Job-1.inp"
    output_file = "../Job-1_cleaned.inp"
    log_file = "cleanup_log.txt"

    lines = read_inp(input_file)
    blocks = split_into_blocks(lines)

    print("Original model summary:")
    summarize_blocks(blocks)

    cleaned_blocks, removed = clean_model(blocks)

    print("\nCleaned model summary:")
    summarize_blocks(cleaned_blocks)

    write_inp(output_file, cleaned_blocks)

    with open(log_file, "w") as f:
        for item in removed:
            f.write(item + "\n")

    print(f"\nWrote {output_file}")
    print(f"Wrote {log_file}")

if __name__ == "__main__":
    main()
