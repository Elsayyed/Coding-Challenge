# wc_tool.py - Word Count Tool

This Python script is a simple word count tool (`wc` command) that provides various statistics about text files. It can count the number of lines, words, characters, and bytes in a file.

## Usage

### Running the Script

You can run the script from the command line with Python. Here's the basic usage:

```bash
python wc_tool.py [OPTIONS] [FILE]
```

- `[OPTIONS]`: Optional command-line options to specify the type of statistic to calculate. Options include:
  - `-c`: Count the number of bytes in the file.
  - `-l`: Count the number of lines in the file.
  - `-w`: Count the number of words in the file.
  - `-m`: Count the number of characters in the file.

- `[FILE]`: Optional path to the text file to analyze. If not provided, the script will read from standard input (`stdin`).

### Examples

1. Count the number of lines in a file:
```bash
python wc_tool.py -l example.txt
```

2. Count the number of words in a file:
```bash
python wc_tool.py -w example.txt
```

3. Count the number of bytes in a file:
```bash
python wc_tool.py -c example.txt
```

4. Count the number of characters in a file (including multi-line characters):
```bash
python wc_tool.py -m example.txt
```

5. Piping input from `cat`:
```bash
cat example.txt | python wc_tool.py -l
```

## Implementation Details

- The script utilizes Python's standard `sys` and `io` modules to handle command-line arguments and file input.
- It defines a `wc_tool` class that encapsulates the functionality of the word count tool.
- The class has methods to handle both piped input and file input, as well as methods to calculate various statistics.
- Statistics are calculated based on the provided command-line options.
- Edge cases, such as empty input or missing file names, are handled gracefully.