def process_files(file_names, processors):
    for filename, processor in zip(file_names, processors):
        print(f"Processing {filename} with {processor.__name__}")
        # Would actually process the file here

def uppercase_processor(content):
    return content.upper()

def lowercase_processor(content):
    return content.lower()

files = ['file1.txt', 'file2.txt']
processors = [uppercase_processor, lowercase_processor]

process_files(files, processors)
