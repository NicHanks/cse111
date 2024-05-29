


def main():
    text_list = read_list("provinces.txt")
    print(text_list)
    count = count_alberta("provinces.txt")
    print(f"Alberta was counted", count, "times.")

def count_alberta(filename):
    with open(filename, "rt") as text_file:
        next(text_file)
        x = 0
        for line in text_file:
            clean_line = line.strip()
            if clean_line == "AB":
                clean_line = "Alberta"
            if clean_line == "Alberta":
                x += 1
        return x

def read_list(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        next(text_file)
        for line in text_file:
            clean_line = line.strip()
            if clean_line == "AB":
                clean_line = "Alberta"
            text_list.append(clean_line)
        text_list.pop()
        return text_list

if __name__ == "__main__":
    main()