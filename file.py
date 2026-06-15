def find_and_replace(filename, old_word, new_word):
    try:
        # Read file content
        with open(filename, "r") as file:
            content = file.read()

        # Check if word exists
        if old_word not in content:
            print(f"'{old_word}' not found in the file.")
            return

        # Replace word
        updated_content = content.replace(old_word, new_word)

        # Write updated content back to file
        with open(filename, "w") as file:
            file.write(updated_content)

        print("Word replaced successfully!")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main Program
print("=== Find and Replace in Text File ===")

file_name = input("Enter file name (e.g., sample.txt): ")
find_word = input("Enter word to find: ")
replace_word = input("Enter replacement word: ")

find_and_replace(file_name, find_word, replace_word)