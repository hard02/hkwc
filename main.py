import argparse
import time
import sys
import tempfile

def byte_count(fname):
    """
    Counts the number of bytes in a given file.

    Args:
    fname (str): The path to the file whose byte count is to be calculated.

    Returns:
    int: The number of bytes in the file.
    """
    with open(fname, 'rb') as file:
        content = file.read()
        return len(content)


def line_count(fname):
    """
    Counts the number of lines in a given file.

    Args:
    fname (str): The path to the file whose line count is to be calculated.

    Returns:
    int: The number of lines in the file.
    """
    with open(fname, 'r') as file:
        return len(file.readlines())


def word_count(fname):
    """
    Counts the number of words in a given file.

    Args:
    fname (str): The path to the file whose word count is to be calculated.

    Returns:
    int: The number of words in the file.
    """
    with open(fname, 'r') as file:
        word_count = 0
        for words in file:
            word_count += len(words.split())
    return word_count


def char_count(fname):
    """
    Counts the number of characters in a given file.

    Args:
    fname (str): The path to the file whose character count is to be calculated.

    Returns:
    int: The number of characters in the file.
    """
    with open(fname, 'rb') as file:
        content = file.read()
        decoded_content = content.decode('utf-8')
        return len(decoded_content)


def main():
    """
    Main function that parses command-line arguments and performs various file analysis operations.

    The operations available are:
    - 'c': Count the number of bytes in the file.
    - 'l': Count the number of lines in the file.
    - 'w': Count the number of words in the file.
    - 'm': Count the number of characters in the file.
    - 'all': Perform all the above operations and display the results.

    The script also handles piped input if no file is provided, and processes the content as if it were read from a file.

    Arguments:
    operation (str): The operation to perform on the file ('c', 'l', 'w', 'm', or 'all'). Defaults to 'all'.
    add_file (str): The path to the file to process. If not provided, the script reads from stdin.
    """
    start = time.time()
    parser = argparse.ArgumentParser(description='A personalised code implementation of word count command in Unix based systems')
    parser.add_argument("operation",
                        choices=['c', 'l', 'w', 'm', 'all'],
                        type=str,
                        default='all',
                        nargs="?")
    parser.add_argument("add_file",
                        type=str,
                        help="The file to process",
                        nargs="?")

    args = parser.parse_args()

    try:
        # Handle piped input if no file is provided
        if not args.add_file:
            # Read piped input from stdin
            piped_content = sys.stdin.buffer.read()
            # Create a temporary file to store the piped content
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(piped_content)
                file_name = temp_file.name
        else:
            file_name = args.add_file

        # Perform the operation
        result = None
        if args.operation == 'c':
            result = byte_count(file_name)
        elif args.operation == 'l':
            result = line_count(file_name)
        elif args.operation == 'w':
            result = word_count(file_name)
        elif args.operation == 'm':
            result = char_count(file_name)
        elif args.operation == 'all':
            result = f"{line_count(file_name)} {word_count(file_name)} {byte_count(file_name)}"

        # Print the result
        print(f"{result} {file_name if args.add_file else ''}")

    except Exception as err:
        print(f"Error: {err}")

    finally:
        end = time.time()
        print(f"{(end - start):.3f} secs to execute")


if __name__ == '__main__':
    main()
