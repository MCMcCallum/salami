"""
Created 06-27-18 by Matt C. McCallum
"""


# Local imports 
# None.

# Third party imports
# None.

# Python standard library imports
import os


ANNOTATION_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'salami-data-public', 'annotations')
AUDIO_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mp3s/')


def configure_annotation_path(path):
    """
    Configure the path containing all annotations files. This path should contain a number
    of folders each named after an annotation ID, containing the raw annotation data and a
    subdirectory labelled 'parsed' containing parsed annotations.

    Args:
        path -> str - A complete path to the directory that contains the annotation directory
        structure.
    """
    global ANNOTATION_DIR
    ANNOTATION_DIR = path


def configure_audio_path(path):
    """
    Configure the path containing all audio files. Audio files should be in this path as mp3s or
    wavs. There should be no subdirectory structure, with all files simply in this root directory.
    Each file should be labelled with the correct extension and the filename consisting solely of
    the SALAMI ID.

    Args:
        path -> str - A complete path to the folder containing the set of audio files.
    """
    global AUDIO_DIR
    AUDIO_DIR = path