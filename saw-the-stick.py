__author__ = 'Steve'
The robots want to saw the stick in several pieces. The length of the stick is N inches. We should help our robots saw the stick. All of the parts should have integer lengths (1, 2, 3 .. inches, but not 1.2). As we love the numerical series and especially the Triangular numbers (read more about Triangular numbers on Wikipedia), you should saw the stick so that the lengths form the consecutive fragment of the Triangular numbers series with the maximum quantity (fragment's length). The parts should have different lengths (no repeating). For example: 64 should divided at 15, 21, 28, because 28, 36 is shorter and 1, 3, 15, 45 is not a consecutive fragment.
You are given a length of the stick (N). You should return the list of lengths (integers) for the parts in ascending order. If it's not possible and the problem does not have a solution, then you should return an empty list.
sawing
Input: A length of the stick, an integer.
Output: A fragment of the Triangular numbers, a list of integers (sorted in ascending order) or an empty list.
def checkio(number):
    return [number // 2, number - number // 2]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"