import re

def delete_comment_lines(input_file, output_file):
    # Open the input file and read all lines
    with open(input_file, 'r') as file:
        lines = file.readlines()

        # Regular expressions to match the patterns
        remove_pattern = re.compile(r'^// ')
        modify_pattern = re.compile(r'^////')

        # List to hold the processed lines
        processed_lines = []

        for line in lines:
            if remove_pattern.match(line):
                continue  # Skip lines that start with "//"
            elif modify_pattern.match(line):
                # Remove "////" from the start of the line
                line = line[4:]
                processed_lines.append(line)
            else:
                processed_lines.append(line)

        # Write the processed lines to the output file
        with open(output_file, 'w') as file:
            file.writelines(processed_lines)

# Example Usage
input_file = '4ff6f.js'  # Replace with your input file name
output_file = 'stage2.js'  # Replace with your output file name

delete_comment_lines(input_file, output_file)

