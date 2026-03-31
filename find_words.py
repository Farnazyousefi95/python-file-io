"""Script to search a text file for words matching a regular expression pattern.

This script reads a text file line by line, finds all words matching a given
regex pattern, and writes each match to an output file along with its line
number.
"""

import re


def find_pattern_in_file(input_path, pattern):
    """Read a file and find all words matching a regex pattern.

    Parameters
    ----------
    input_path : str
        Path to the text file to search.
    pattern : str
        A regular expression pattern to match words against.

    Returns
    -------
    list of tuple
        A list of (line_number, word) tuples for every match found.
    """
    matches = []
    regex = re.compile(pattern, re.IGNORECASE)
    with open(input_path, 'r') as in_stream:
        for line_number, line in enumerate(in_stream, start=1):
            line = line.strip()
            for match in regex.finditer(line):
                matches.append((line_number, match.group()))
    return matches


def write_matches_to_file(matches, output_path):
    """Write a list of (line_number, word) tuples to a tab-delimited file.

    Parameters
    ----------
    matches : list of tuple
        Each tuple contains (line_number, word).
    output_path : str
        Path to the output file to create.
    """
    with open(output_path, 'w') as out_stream:
        for line_number, word in matches:
            out_stream.write(f'{line_number}\t{word}\n')


def main():
    """Search origin.txt for heritability-related words and write results."""
    input_path = 'origin.txt'
    output_path = 'heritability_words.txt'
    pattern = r'\b\w*herit\w*\b'

    matches = find_pattern_in_file(input_path, pattern)
    write_matches_to_file(matches, output_path)

    print(f'Done! Found {len(matches)} matches.')
    print(f'Results written to {output_path}')


if __name__ == '__main__':
    main()
