# Import the parser module from the Tika library
from tika import parser
# Import the os module
import os

# Define a function for converting PDF files to text
def convert_pdf_to_text(dir):
    # Initialize an empty list to store the extracted text contents
    output=[]
    # Perform a walk through the directory and its subdirectories
    for root, dirs, files in os.walk(dir):
        # Print the names of all the files in the current directory
        print(files)
        # Iterate through all the files in the current directory
        for file in files:
            # Create the full path to the current file
            path_to_pdf = os.path.join(root, file)
            # Uncomment the following line to print the path to each file
            #print(path_to_pdf)
            # Split the file name and extension
            [stem, ext] = os.path.splitext(path_to_pdf)
            # Check if the extension is '.pdf'
            if ext == '.pdf':
                # Print a message indicating that the file is being processed
                print("Processing " + path_to_pdf)
                # Use the parser module to extract the text contents of the file
                pdf_contents = parser.from_file(path_to_pdf, service='text')
                # Create the path to the text file
                path_to_txt = stem + '.txt'
                # Uncomment the following block of code to write the extracted text contents to a text file
                # with open(path_to_txt, 'w', encoding='utf-8') as txt_file:
                #     print("Writing contents to " + path_to_txt)
                #     txt_file.write(pdf_contents['content'])
                # Append the extracted text contents to the `output` list
                output.append(pdf_contents['content'])
    # Return the `output` list
    return output

