#!./.env/bin/python3.12

import marko


with open("./posts/post-1.md", "r") as f:
    test_text = f.read()

print(test_text)

print(marko.convert(test_text))
