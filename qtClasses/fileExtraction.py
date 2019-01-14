import zipfile
with zipfile.ZipFile("/home/roshan/Downloads/abc.zip", 'r') as zip_ref:
    zip_ref.extractall("/home/roshan/Downloads/try")