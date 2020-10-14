"""
Consolidated Stock Universe Membership
"""
from datetime import date

# End of time
EOT = date(9999, 12, 31)

# Example:

snapshots = [
    {"date": date(2020, 6, 1), "tickers": ["AAPL", "BRK.B", "CSCO"]},
    {"date": date(2020, 7, 1), "tickers": ["AAPL", "CSCO", "DISH"]},
    {"date": date(2020, 8, 1), "tickers": ["AAPL", "CSCO", "DISH"]},
    {"date": date(2020, 9, 1), "tickers": ["AAPL", "BRK.B", "DISH"]},
]

expected_universe = [
    {"ticker": "AAPL", "start": date(2020, 6, 1), "end": EOT},
    {"ticker": "BRK.B", "start": date(2020, 6, 1), "end": date(2020, 7, 1)},
    {"ticker": "BRK.B", "start": date(2020, 9, 1), "end": EOT},
    {"ticker": "CSCO", "start": date(2020, 6, 1), "end": date(2020, 9, 1)},
    {"ticker": "DISH", "start": date(2020, 7, 1), "end": EOT},
]


def consolidate(snapshots):
    """
    Consolidates the snapshots into a tuple of membership changes.

    :param snapshots: a list of snapshots dicts in increasing order of `date`

    :return: a list of `Member` dicts.
        * one record per `id` for date range that it belonged to the universe
        * records for the same `id` must not overlap
        * records for the same `id` must have a gap of at least one date
    """
    return []


actual_universe = consolidate(snapshots)
print(actual_universe)
assert actual_universe == expected_universe
