"""
Created 06-26-18 by Matt C. McCallum
"""


# Local imports 
from . import config

# Third party imports
import numpy as np

# Python standard library imports
import os
import csv


class Annotation(object):
    """
    An interface to a single track and all its annotations.
    This class allows you to extract the data from the annotation file,
    and some simple preprocessing or selection of that data.

    Note that the Salami dataset has a notion of uppercase and lowercase annotations
    that each have different meanings. In short the uppercase annotations are much broader
    and only have one class per label. The lowercase annotations are more detailed and each
    label has a set of subclasses each with different meanings.
    """

    def __init__(self, salami_id):
        """
        Constructor.

        Args:
            salami_id - int - A number representing the SALAMI dataset signed ID for an individual track.
        """
        self._path = os.path.join(config.ANNOTATION_DIR, str(salami_id), 'parsed')

    def GetUppercase(self, annotator):
        """
        Get uppercase annotations from a specific annotator.

        Args: 
            annotator -> int - An index to the annotator. Currently in Salami there are up to two
            annotators per file, whose annotations are indexed 1 or 2.

        Return:
            list(tuple(float, str)) - A list of annotation points. Each element is a tuple who's first
            element is the time point at which the annotation starts, and the second element is the label
            for the segment that follows that timepoint. The end of each segment is found via the timepoint
            of the next annotation that follows in the list.
        """
        # If annotator is none, I return just the common boundaries
        if annotator not in [1, 2]:
            raise KeyError('Unknown annotator number selected for SALAMI dataset.')
        return self._ReadTSV(os.path.join(self._path, 'textfile' + str(annotator) + '_uppercase.txt'))

    def GetMostSegUppercase(self):
        """
        Gets the most segmented uppercase annotation for the track referenced by this object of those annotations
        that are available.

        Return:
            list(tuple(float, str)) - A list of annotation points. Each element is a tuple who's first
            element is the time point at which the annotation starts, and the second element is the label
            for the segment that follows that timepoint. The end of each segment is found via the timepoint
            of the next annotation that follows in the list.
        """
        annotators = [1, 2]
        segs = []
        for annotator in annotators:
            segs += [self.GetUppercase(annotator)]
        num_segs = [len(seg) for seg in segs]
        return segs[num_segs.index(max(num_segs))]

    def GetLeastSegUppercase(self):
        """
        Gets the least segmented uppercase annotation for the track referenced by this object of those annotations
        that are available.

        Return:
            list(tuple(float, str)) - A list of annotation points. Each element is a tuple who's first
            element is the time point at which the annotation starts, and the second element is the label
            for the segment that follows that timepoint. The end of each segment is found via the timepoint
            of the next annotation that follows in the list.
        """
        annotators = [1, 2]
        segs = []
        for annotator in annotators:
            segs += [self.GetUppercase(annotator)]
        num_segs = [len(seg) for seg in segs]
        return segs[num_segs.index(min(num_segs))]
            
    def GetLowercase(self, annotator):
        """
        Get lowercase annotations from a specific annotator.

        Args: 
            annotator -> int - An index to the annotator. Currently in Salami there are up to two
            annotators per file, whose annotations are indexed 1 or 2.

        Return:
            list(tuple(float, str)) - A list of annotation points. Each element is a tuple who's first
            element is the time point at which the annotation starts, and the second element is the label
            for the segment that follows that timepoint. The end of each segment is found via the timepoint
            of the next annotation that follows in the list.
        """
        if annotator not in [1, 2]:
            raise KeyError('Unknown annotator number selected for SALAMI dataset.')
        return self._ReadTSV(os.path.join(self._path, 'textfile' + str(annotator) + '_lowercase.txt'))

    def _ReadTSV(self, path):
        """
        Helper function for reading in a tsv file - which is the format the SALAMI dataset annotations
        are provided in.
        It expects a two column tsv format with annotations labels first and times in the second column.

        Args:
            path -> str - The path to the annotations file to be read in and returned.

        Return:
            list(tuple(float, str)) - A list of annotation points. Each element is a tuple who's first
            element is the time point at which the annotation starts, and the second element is the label
            for the segment that follows that timepoint. The end of each segment is found via the timepoint
            of the next annotation that follows in the list.
        """
        segments = []
        with open(path, 'r') as f:
            f_reader = csv.reader(f, delimiter='\t')
            for line in f_reader:
                segments += [(line[0], line[1])]
        return segments
