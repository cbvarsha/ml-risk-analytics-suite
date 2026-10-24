import pytest
from src.app import confusion, population_stability


def test_confusion_rejects_mismatched_lengths():
    with pytest.raises(ValueError, match="equal length"):
        confusion([0, 1], [0.2])


def test_confusion_rejects_invalid_probabilities():
    with pytest.raises(ValueError, match="Probabilities"):
        confusion([1], [1.2])


def test_psi_rejects_invalid_distributions():
    with pytest.raises(ValueError, match="sum to one"):
        population_stability([0.2, 0.2], [0.5, 0.5])
