import os


def clean_up_fixtures(elements_to_remove: list):
    for element in elements_to_remove:
        os.remove(element)