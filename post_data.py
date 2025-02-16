import re

class PostData:
    def __init__(self, file: str) -> None:
        self._file = open(file, "r").readlines()
        self._html_tag_classes = {
            "title": None,
            "tags": None,
            "date-of-posting": None,
            "date-of-last-edit": None,
            "description": None,
            "post-url": None,
            "prev-img-url": None
        }

    def _key_in_line_is_valid(self, key, line) -> bool:
        """
        Check that the found key is actully wrapped inside the class attribute.
        """

        # RegEx with the following rules:
        # - The line HAVE to contain: " class=" # with "" or '' after the "=".
        # - The line HAVE to contain the given key between the class-quotes,
        # BUT is flexible enough to have other classes before or after the given key.
        re_l = r"(\s\bclass=(\"|'))((.*?)\b"
        re_r = r"(.*?))?(\"|')"
        re_w_key = re_l + key + re_r

        return bool(re.search(re_w_key, line))

    def _html_tag_content(self, line) -> str:
        """
        Remove the HTML from a string, returning only the conent between the tags.
        """

        cont_r = line[line.find(">")+1:]
        cont_l = cont_r[:cont_r.find("<")]

        return cont_l

    def get_post_data(self) -> dict:
        """
        Fill the dictionary with the information found inside the HTML file.
        """

        for line in self._file:
            for key in self._html_tag_classes.keys():
                if (key in line) and (self._key_in_line_is_valid(key, line)):
                    self._html_tag_classes[key] = self._html_tag_content(line)

        return self._html_tag_classes
