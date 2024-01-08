import os
import weaviate

# Weaviate instance details
weaviate_url = "http://localhost:8080"
weaviate_client = weaviate.Client(url=weaviate_url)

# Ensure your Weaviate library version is up-to-date
# Run: pip install --upgrade weaviate-client

# Function to embed files into Weaviate
def embed_files_in_weaviate(file_paths):
    for file_path in file_paths:
        try:
            # Get file extension
            file_extension = os.path.splitext(file_path)[1].lower()

            # Read file content based on the file extension
            if file_extension == ".txt":
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
            elif file_extension == ".docx":
                # Add code to extract text from docx files
                file_content = "Content from docx file"
            elif file_extension == ".pdf":
                # Add code to extract text from pdf files
                file_content = "Content from pdf file"
            else:
                print(f"Unsupported file type: {file_extension}")
                continue

            # Create a data object
            data_object = {
                "text": file_content,
                "filename": os.path.basename(file_path)
            }

            # Define the class name (update as per your schema in Weaviate)
            class_name = "Document"

            # Add the data object to Weaviate
            weaviate_client.data_object.create(data_object, class_name=class_name)

            print(f"File {file_path} embedded successfully.")

        except Exception as e:
            print(f"Error embedding file {file_path}: {e}")

# Specify the data folder path
data_folder_path = "data"  # Update with your data folder path

# Get a list of all files in the data folder
file_paths_to_embed = [os.path.join(data_folder_path, file) for file in os.listdir(data_folder_path) if os.path.isfile(os.path.join(data_folder_path, file))]

# Example usage
embed_files_in_weaviate(file_paths_to_embed)
