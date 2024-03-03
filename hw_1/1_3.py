import sys
def count_stats(filename=None):
    lines, words, bytes = 0, 0, 0
    if filename:
        with open(filename, 'r') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                bytes += len(line.encode('utf-8'))
    else:
        for line in sys.stdin:
            lines += 1
            words += len(line.split())
            bytes += len(line.encode('utf-8'))
    return lines, words, bytes


if __name__ == "__main__":
    total_lines, total_words, total_bytes = 0, 0, 0
    filenames = sys.argv[1:]

    if filenames:
        for filename in filenames:
            lines, words, bytes = count_stats(filename)
            print(f"{lines} {words} {bytes} {filename}")
            total_lines += lines
            total_words += words
            total_bytes += bytes
        if len(filenames) > 1:
            print(f"{total_lines} {total_words} {total_bytes} total")
    else:
        lines, words, bytes = count_stats()
        print(f"{lines} {words} {bytes}")
