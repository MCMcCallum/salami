"""
Created 06-29-18 by Matt C. McCallum
"""


# Local imports
# None.

# Third party imports
# None.

# Python standard library imports
# None.


def hit_rate(truth, estimate, tolerance):
    """
    Provides the precision recall and f measure for estimates of continuous 1D values.
    For example, for time boundaries in the SALAMI dataset.

    Args:
        truth -> list(list(float)) - The set of ground truth time points that are to be estimated for
        a range of tracks. Each track is a top level element, and the boundaries are the lists within
        the list. The track order must match the "estimate" arg. But the boundaries can be provided in 
        any order.
        
        estimate -> list(float) - The set of estimated time points that are intended to be estimates
        of the values in "truth". Each track is a top level element, and the boundaries are the lists within
        the list. The track order must match the "truth" arg. But the boundaries can be provided in 
        any order.

        tolerance -> float - A positive value providing the accepted absolute distance between a
        boundary value for a given track in truth and estimate, for the value in estimate to be considered 
        correct.

    Return:
        precision -> float - The precision of the provided estimates.

        recall -> float - The recall of the provided estimates.

        f_measure -> float - The F-measure of the provided estimates.
    """
    est_hits = 0
    boundary_hits = 0
    tot_num_ests = 0
    tot_num_boundaries = 0
    for track_boundaries, est_boundaries in zip(truth, estimate):
        num_ests = len(est_boundaries)
        num_boundaries = len(track_boundaries)
        est_hits = [False]*num_ests
        truth_hits = [False]*num_boundaries
        correct_ests = 0
        for est_idx, est_boundary in enumerate(est_boundaries):
            for truth_idx, boundary in enumerate(track_boundaries):
                if abs(est_boundary-boundary) <= tolerance:
                    est_hits[est_idx] = True
                    truth_hits[truth_idx] = True
        est_hits = sum(est_hits)
        boundary_hits = sum(truth_hits)
        tot_num_ests += num_ests
        tot_num_boundaries += num_boundaries
    precision = est_hits/tot_num_ests
    recall = boundary_hits/tot_num_boundaries
    f_measure = precision*recall/(precision + recall)
    return precision, recall, f_measure
