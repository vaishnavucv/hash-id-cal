import hashlib

def calculate_file_hash(file_path):
    # Create a hash object
    hash_object = hashlib.sha256()

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Read the file in chunks to avoid loading the entire file into memory
        for chunk in iter(lambda: file.read(4096), b''):
            # Update the hash object with the current chunk
            hash_object.update(chunk)

    # Get the hexadecimal representation of the hash
    file_hash = hash_object.hexdigest()

    return file_hash

# Ask user for file path
file_path = input("Enter the file path: ")

# Calculate the hash value
hash_value = calculate_file_hash(file_path)
print(f'The hash value of {file_path} is: {hash_value}')
