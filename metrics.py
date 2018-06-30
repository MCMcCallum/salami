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
        truth -> list(float) - The set of ground truth time points that are to be estimated.
        This can be provided in any order.
        
        estimate -> list(float) - The set of estimated time points that are intended to be estimates
        of the values in "truth". This can be provided in any order.

        tolerance -> float - A positive value providing the accepted absolute distance between a
        value in truth and estimate, for the value in estimate to be considered correct.

    Return:
        precision -> float - The precision of the provided estimates.

        recall -> float - The recall of the provided estimates.

        f_measure -> float - The F-measure of the provided estimates.
    """
    num_ests = len(estimate)
    num_boundaries = len(truth)
    correct_ests = 0
    for est_boundary in estimate:
        if any([abs(est_boundary-true_boundary)<=tolerance for true_boundary in truth]):
            correct_ests += 1
    precision = correct_ests/num_ests
    recall = correct_ests/num_boundaries
    f_measure = precision*recall/(precision+recall)
    return precision, recall, f_measure
