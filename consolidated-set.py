"""
Consolidated Stock Universe Membership

Problem:

    We would like to record changes to a universe of stocks over time in a space-efficient way so that we easily
    cache and query the universe in memory.

Constraints:

    Stock universes can have as many as 5000 assets and can change daily.

    To record the complete membership for each day for 20 years would require 5000 * 252 * 20 = 25 million records.

    Rather than store the full membership on each day, we can store only the changes.

Example:

    # Input
    snapshots = (
        Snapshot(dt=date(2020, 6, 1), members_ids=["AAPL", "BRK.B", "CSCO" ]),
        Snapshot(dt=date(2020, 7, 1), members_ids=["AAPL", "CSCO", "DISH ]),
        Snapshot(dt=date(2020, 8, 1), members_ids=["AAPL", "BRK.B", "DISH ]),
    )

    # Output
    universe = (
        Member(id="AAPL", start=date(2020, 6, 1)),
        Member(id="BRK.B", start=date(2020, 6, 1), end=date(2020, 7, 1)),
        Member(id="BRK.B", start=date(2020, 8, 1)),
        Member(id="CSCO", start=date(2020, 6, 1), end=date(2020, 8, 1)),
        Member(id="DISH", start=date(2020, 7, 1)),
    )
"""
from dataclasses import dataclass
from datetime import date
from typing import List, Tuple

eot = date(9999, 12, 31)


@dataclass(frozen=True)
class Snapshot(object):
    """
    Complete list of universe members IDs as of a particular date.

    * `dt` is the snapshot date
    * `member_ids` contains the unique IDs of all set members on the date
    * member IDs are in alphabetical order
    * snapshots are ordered by increasing time
    """

    dt: date
    members_ids: List[str]


@dataclass(frozen=True)
class Member(object):
    """
    Records when a stock entered and left the universe.

    * `start` is the date on which the ID entered the universe
    * `end` is the date on which the ID left the set
    * `end == eot`  means the ID is still in the set
    * records for the same ID in the universe may not have overlapping date ranges.
    """

    id: str
    start: date
    end: date = eot


def consolidate(snapshots: Tuple[Snapshot, ...]) -> Tuple[Member, ...]:
    pass

