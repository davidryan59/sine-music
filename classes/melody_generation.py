from copy import copy
from dataclasses import dataclass
from fractions import Fraction
from typing import Union, List


# Classes to iteratively build up melodies as graphs of freq vs time


@dataclass
class NoteBase:
    # Abstract base class
    t: Union[Fraction, int]  # Duration, unit could be seconds, or beats


@dataclass
class Note(NoteBase):
    # Represents a frequency (f), at a volume (db)
    f: Union[Fraction, int]  # Frequency, unit could be Hz, or relative
    db: Union[Fraction, int] = 100  # Decibels, where 100 dB = amplitude 1

    # Reduce volume of note by specified number of decibels
    def sub_db(self, db):
        note: NoteBase = copy(self)
        note.db -= db
        return note


@dataclass
class Rest(NoteBase):
    # Represents a rest, which has a duration, nothing else
    pass


@dataclass
class Melody:
    # Represents a list of notes (or rests) to be played sequentially
    notes: List[NoteBase]

    def duration(self):
        return sum([n.t for n in self.notes])
