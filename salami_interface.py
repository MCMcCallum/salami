"""
Created 06-27-18 by Matt C. McCallum
"""


# Local imports 
from data_access import dir_funcs
from .annotation import Annotation
from . import config

# Third party imports
# None.

# Python standard library imports
import os


class SalamiInterface(object):
    """
    Provides an interface to the overall SALAMI dataset. Any reading of audio or annotations
    in the dataset should be interfaced through this class.
    """

    def __init__(self):
        """
        Constructor.
        """
        # Get all mp3, wav and pkl files.
        self._audio_files = dir_funcs.get_filenames(config.AUDIO_DIR, ['.mp3', '.wav', '.pkl']) # <= Note that if there are pickled object files in this directory
                                                                                                #    they are assumed to be pickled features of the desired audio files
        # Select only the files that have a numeric SALAMI ID as the filename
        self._audio_files = [fname for fname in self._audio_files if os.path.splitext(os.path.basename(fname))[0].isdigit()]

    def GetIDsWithAudio(self):
        """
        Gets a list of all SALAMI ID numbers that have audio on disk.
        Audio is expected to be in the module configured "AUDIO_DIR" as a wav or mp3 file with
        the filename consisting of the SALAMI ID number.

        Return:
            list(int) - Returns a list of integers containing all IDs that audio was found for.
        """
        return [int(os.path.splitext(os.path.basename(fname))[0]) for fname in self._audio_files]

    def GetAnnotationsForIDs(self, ids=[]):
        """
        Returns a list of annotation objects for each of the requested IDs.

        Args:
            ids -> list(int) - A list of SALAMI IDs as integers to return the annotations for.

        Return:
            list(Annotation) - A list of annotation objects interfacing the SALAMI annotation data
            for the requested IDs.
        """
        return [Annotation(id_number) for id_number in ids]

    def AudioURLForID(self, id_number):
        """
        Returns a URL for an audio file of a given ID.

        Args:
            id_number -> int - An integer providing a SALAMI ID for a SALAMI annotation, to retrieve the
            URL for the corresponding audio file.

        Return:
            str - A string containing the path and filename for the requested audio file.
        """
        audio_ids = self.GetIDsWithAudio()
        if id_number not in audio_ids:
            raise KeyError('No audio for requested SALAMI ID')
        return self._audio_files[next(idx for idx, x in enumerate(audio_ids) if x==id_number)]
