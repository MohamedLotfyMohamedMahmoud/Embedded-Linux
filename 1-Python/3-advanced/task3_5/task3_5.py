import re
import openpyxl

def extract_function_prototypes(header_file_content):
    # Regular expression to match function prototypes
    prototype_pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\s+\**\s*\b[A-Za-z_][A-Za-z0-9_]*\s*\([^;]*\)\s*;')
    return prototype_pattern.findall(header_file_content)

def write_to_excel(function_prototypes, output_file):
    # Create a new Excel workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Function Prototypes"

    # Write the header
    sheet.append(["ID", "Function Prototype"])

    # Write the function prototypes with unique IDs
    for idx, prototype in enumerate(function_prototypes):
        sheet.append([f"IDX{idx}", prototype])

    # Save the workbook to a file
    workbook.save(output_file)

def main():
    header_file_path = input("Enter the path to the C header file: ")
    output_file_path = input("Enter the path to the output Excel file: ")

    # Read the content of the header file
    with open(header_file_path, 'r') as file:
        header_file_content = file.read()

    # Extract function prototypes
    function_prototypes = extract_function_prototypes(header_file_content)

    # Write function prototypes to Excel
    write_to_excel(function_prototypes, output_file_path)

    print(f"Function prototypes have been written to {output_file_path}")

if __name__ == "__main__":
    main()
