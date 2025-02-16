from os import path, walk
from post_data import PostData

class BuildJson:
    def __init__(self, file) -> None:
        self._file = file

    def json(self):
        # Collect all the files in the "static" directory
        files = [path.join(dirpath, f) for (dirpath, dirnames, filenames) in walk(self._file) for f in filenames]

        # Return all collected dictionaries.
        return [PostData(f).get_post_data() for f in files]
