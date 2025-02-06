# hkwc

A Python-based implementation of the Unix `wc` command that provides file analysis capabilities including byte count, line count, word count, and character count.

## Features

- Count bytes in a file (`-c`)
- Count lines in a file (`-l`)
- Count words in a file (`-w`)
- Count characters in a file (`-m`)
- Display all counts together (default behavior)
- Support for both file input and piped input

## Installation

```bash
git clone https://github.com/hard02/hkwc
cd hkwc
```

## Usage

```bash
python hkwc_build/main.py [operation] [file]
```

### Operations

- `c` - Count bytes
- `l` - Count lines
- `w` - Count words
- `m` - Count characters
- `all` - Show lines, words, and bytes (default)

### Examples

Count all metrics in a file:
```bash
python hkwc_build/main.py test.txt
```

Count only lines:
```bash
python hkwc_build/main.py l test.txt
```

Use with piped input:
```bash
cat test.txt | python hkwc_build/main.py w
```

## Output Format

The output format varies based on the operation:

- Single operation: `[count] [filename]`
- All operations: `[lines] [words] [bytes] [filename]`

## Performance

The script includes execution time measurement, displayed after each operation.

## Requirements

- Python 3.6 or higher
- No additional dependencies required

## Error Handling

The script includes robust error handling for:
- File not found
- Permission issues
- Invalid file formats
- Invalid inputs

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues and enhancement requests!
