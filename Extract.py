import zipfile
import os

zip_file_path = '/content/submissions.zip'
output_dir = '/content/unzip4'
limit = 3  # Set your desired limit here

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()[:limit]  # Get a sublist of files within the limit
        for file in file_list:
            zip_ref.extract(file, output_dir)
          
print(f"Successfully extracted {limit} files from {zip_file_path} to {output_dir}.")
