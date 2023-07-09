import os

class FileRenamer:
    def __init__(self):
        self.target_name = ""
        self.num_digits = 0
        self.source_extension = ""
        self.target_extension = ""
        self.name_range = None

    def set_parameters(self, target_name, num_digits, source_extension, target_extension, name_range=None):
        self.target_name = target_name
        self.num_digits = num_digits
        self.source_extension = source_extension
        self.target_extension = target_extension
        self.name_range = name_range

    def rename_files(self, directory):
        file_counter = 1

        for filename in os.listdir(directory):
            if filename.endswith(self.source_extension):
                name_part = filename[self.name_range[0]:self.name_range[1]]
                new_filename = f"{name_part}_{self.target_name}{str(file_counter).zfill(self.num_digits)}.{self.target_extension}"
                file_counter += 1

                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)


renamer = FileRenamer()
renamer.set_parameters("newname", 3, ".txt", "docx", name_range=(3, 6))
renamer.rename_files("path/to/directory")