import logging
import os
import sys

from main import load_source_to_ast


def test_all():
    directory = "../heroc-examples/"
    for filename in os.listdir(directory):
        if filename.endswith(".heroc"):
            try:
                load_source_to_ast(directory+filename)
                print("{} OK!".format(filename))
            except Exception as e:
                print("{} FAILED!".format(filename))
        else:
            continue

if __name__ == '__main__':
    test_all()
