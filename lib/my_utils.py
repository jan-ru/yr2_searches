import csv


def read_citekeys(filename):
    """
    Read citation keys from a CSV file.

    This function opens a specified CSV file and reads citation keys assuming each key is on a separate line in the file.

    Parameters:
        filename (str): The path to the CSV file containing the citation keys.

    Returns:
        list: A list of citation keys.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: For other issues that may arise during file reading.
    """
    citekeys = []
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Assuming each row contains one citekey
                citekeys.append(row[0])
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return citekeys
