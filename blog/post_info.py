from bs4 import BeautifulSoup

class PostJson:
    def __init__(self, file: str) -> None:
        self._file = open(file, "r").read()

        # Create an instance of BeatifulSoup with the givn file and the parser type.
        self._soup = BeautifulSoup(self._file, "html.parser")

        self._post_info = {
            "title": None,
            "tags": None,
            "date-of-posting": None,
            "date-of-last-edit": None,
            "description": None,

            # Need modifiactaion by client for functionality.
            "post-url": None,
            "preview-img-url": None
        }

        self._fill_post_info() # Fill the dict when creating the instance.

    def _fill_post_info(self) -> None:
        for key in self._post_info.keys():

            if (k := self._soup.select_one(f".{key}")):

                if k.name == "img":                     # If the tag is an image (to get the 'preview-img-url').
                    self._post_info[key] = k["src"]     # Get the content of the 'src' attr instead of the tags content.

                else:
                    s = str(k.text).replace("\n", "")   # Remove newline characters.
                    n = " ".join(s.split())             # Remove excess and trailing whitespaces.
                    self._post_info[key] = n

    def get_json_data(self) -> dict:
        return self._post_info
