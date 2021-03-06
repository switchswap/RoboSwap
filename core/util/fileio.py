from pathlib import Path


class FileIO:
    """Class mainly acts as a wrapper for the default python fileIO"""

    def __init__(self, slice_folder, file_name):
        self.slice_folder = slice_folder
        self.file_name = file_name
        self.file_dir = f"modules/data/{self.slice_folder}"
        self.file_path = f"{self.file_dir}/{self.file_name}"
        self._init_file()

    def _init_file(self):
        # Check if file exists (file_name) and creates path it if needed
        path = Path(self.file_dir)
        path.mkdir(parents=True, exist_ok=True)
        file = Path(self.file_path)
        file.touch(exist_ok=True)

    def overwrite(self):
        return open(self.file_path, 'w')

    def append(self):
        return open(self.file_path, 'a')

    def read(self):
        return open(self.file_path, 'r')

    def open(self, mode):
        return open(self.file_path, mode)
