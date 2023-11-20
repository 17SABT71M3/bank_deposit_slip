import shlex
import argparse
import PyPDF2
from PyPDF2.generic import NameObject, create_string_object

def create_field_data_dict(args_str):
    args = shlex.split(args_str)
    field_data_dict = {}
    for i in range(0, len(args), 2):
        field_name = args[i].strip('\"')
        if i + 1 < len(args):
            field_value = args[i + 1].strip('\"')
            field_data_dict[field_name] = field_value
    return field_data_dict

def fill_pdf(input_path, output_path, field_data):
    # Open the PDF file
    with open(input_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Check if the page has form fields
            if '/Annots' in page:
                # Get the annotations (form fields) on the page
                annotations = page['/Annots']

                # Loop through each annotation
                for annotation_ref in annotations:
                    annotation = annotation_ref.get_object()  # Resolve IndirectObject
                    # Check if the annotation is a form field
                    if annotation['/Subtype'] == '/Widget':
                        # Get the field name
                        current_field_name = annotation['/T']

                        # Check if the field name is in the field_data dictionary
                        if current_field_name in field_data:
                            # Set the field value
                            annotation.update({
                                NameObject("/V"): create_string_object(str(field_data[current_field_name]))
                            })

            # Add the modified page to the writer
            pdf_writer.add_page(page)

        # Write the modified PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    # Static file names
    input_pdf = 'example.pdf'
    output_pdf = 'output.pdf'

    parser = argparse.ArgumentParser(description="Fill PDF form fields.")
    parser.add_argument("--field_data", nargs='+', help="Field names and values separated by space, enclose names/values with spaces in double quotes (e.g., 'field1 value1 \"field 2\" value2')")

    args = parser.parse_args()

    # Create a dictionary from the provided field_data arguments
    field_data_dict = {}
    for i in range(0, len(args.field_data), 2):
        field_name = args.field_data[i].strip('\"')
        field_value = args.field_data[i + 1].strip('\"')
        field_data_dict[field_name] = field_value
    print(field_data_dict)

    fill_pdf(input_pdf, output_pdf, field_data_dict)





