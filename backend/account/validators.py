import os

def validate_file_extensions(name):
    is_valid = True

    ext = os.path.splitext(name)[1]
    valid_extensions = ['.pdf']

    if not ext.lower() in valid_extensions:
        is_valid = False

    return is_valid