from classes.melody_generation import Note, Rest, Melody
from fractions import Fraction


def script_generate_melody():
    fname = script_generate_melody.__name__

    # Setup fractions
    fr_1_3 = Fraction(1, 3)
    fr_2_5 = Fraction(2, 5)
    fr_10_9 = Fraction(10, 9)

    # Setup rests
    r1 = Rest(t=1)
    r2 = Rest(t=fr_1_3)

    # Setup notes
    n1 = Note(t=3, f=240)
    n2 = Note(t=1, f=270, db=95)
    n3 = Note(t=4, f=300).sub_db(3)
    n4 = Note(t=fr_2_5, f=fr_10_9 * 240).sub_db(6)
    n5 = Note(t=2, f=360 / fr_10_9).sub_db(7)

    # Setup melody
    m = Melody(notes=[n1, r1, n2, r2, n3, n4, n5])
    print(f"{fname}: melody duration {m.duration()}, notes {m}")
