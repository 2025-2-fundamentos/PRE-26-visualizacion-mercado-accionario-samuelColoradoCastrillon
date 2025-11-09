import os

def generate_file_for_test():
    output_dir = "files/output"

    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"Ensured directory exists: {output_dir}")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    filepath = os.path.join(output_dir, "stocks.png")

    try:
        with open(filepath, 'w') as f:
            pass
        print(f"Created file: {filepath}")
    except IOError as e:
        print(f"Error creating file {filepath}: {e}")

generate_file_for_test()