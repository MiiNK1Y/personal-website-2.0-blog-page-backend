from bs4 import BeautifulSoup


class PostJson:
    def __init__(self, file: str) -> None:

        # File contents, not actual file.
        self._file = file

        # Create an instance of BeautifulSoup with the given file and the parser type.
        self._soup = BeautifulSoup(self._file, "html.parser")

        # The tags (properties) BeautifulSoup will be looking for.
        self._post_info = {
            "title": None,
            "post-url": None,
            "tags": None,
            "date-of-posting": None,
            "date-of-last-edit": None,
            "description": None,

            # Need modification by client for functionality:
            "preview-img-url": None,
        }

        # Fill the dict when creating the instance.
        self._fill_post_info()

    def _fill_post_info(self) -> None:
        for key in self._post_info.keys():

            if (key == "post-url"):

                # Make the title url-friendly
                self._post_infe["post-url"] = self._post_info["title"].lower().replace(" ", "-")

            # Get the first occurrence of the class (key) in the given file.
            elif (k := self._soup.select_one(f".{key}")):

                # If the tag is an image (to get the 'preview-img-url') -
                # get the content of the 'src' attr instead of the tags content.
                if (k.name == "img"):
                    self._post_info[key] = k["src"]

                else:

                    # Remove newline characters.
                    s = str(k.text).replace("\n", "")

                    # Remove excess and trailing whitespaces.
                    n = " ".join(s.split())

                    self._post_info[key] = n


    def get_json_data(self) -> dict:
        return self._post_info
