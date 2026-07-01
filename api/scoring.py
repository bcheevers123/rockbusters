"""Rockbusters scoring — answer normalisation and matching."""

from api.content_bank import normalize, Clue


def check_answer(clue: Clue, user_input: str) -> bool:
    """Return True if user_input matches any normalized alias for the clue.

    Returns False for empty or whitespace-only input without raising.
    """
    if not user_input or not user_input.strip():
        return False
    normalized_input = normalize(user_input)
    return normalized_input in [normalize(alias) for alias in clue.aliases]


__all__ = ["check_answer", "normalize"]
