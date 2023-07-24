"""Grids representing brick layouts per level.  The brick layouts were designed
in Excel. The Grid lists were generated using parse_excel_levels.py utility.

    W=White
    R=Red
    B=Blue
    O=Orange
    C=Cyan
    G=Green
    Y=Yellow
    M=Magenta
    S=Silver
    A=Gold
    .=None

    0=annulus
    1=molecule
    2=morph
    3=orb
    4=tetrahedron
"""

BRICK_WIDTH = 44
BRICK_HEIGHT = 22

LEVEL001 = [
    [['W', 'W', 'W', 'W', 'W', 'W', 'W'],
     ['R', 'R', 'R', 'R', 'R', 'R', 'R'],
     ['B', 'B', 'B', 'B', 'B', 'B', 'B'],
     ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
     ['.', '.', '.', '.', '.', '.', '.'],
     ['C', 'C', 'C', 'C', 'C', 'C', 'C'],
     ['G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
     ['M', 'M', 'M', 'M', 'M', 'M', 'M']],
    [['W', 'W', 'W', 'W', 'W', 'W', 'W'],
     ['R', 'R', 'R', 'R', 'R', 'R', 'R'],
     ['B', 'B', 'B', 'B', 'B', 'B', 'B'],
     ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
     ['.', '.', '.', '.', '.', '.', '.'],
     ['C', 'C', 'C', 'C', 'C', 'C', 'C'],
     ['G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
     ['M', 'M', 'M', 'M', 'M', 'M', 'M']]]

LEVEL002 = [
    [['.', '.', 'O', '.', '.', '.', '.', '.', 'O', '.', '.'],
     ['.', '.', '.', 'O', '.', '.', '.', 'O', '.', '.', '.'],
     ['.', '.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', '.', '.'],
     ['.', 'G', 'G', 'R', 'G', 'G', 'G', 'R', 'G', 'G', '.'],
     ['.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', '.'],
     ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['G', '.', 'G', '.', '.', '.', '.', '.', 'G', '.', 'G'],
     ['G', '.', 'G', '.', '.', '.', '.', '.', 'G', '.', 'G'],
     ['.', '.', '.', 'G', 'G', '.', 'G', 'G', '.', '.', '.']]]

LEVEL003 = [
    [['M', '.', 'O', 'O', 'O', 'O', '.'],
     ['M', '.', '.', '.', '.', 'Y', '.'],
     ['M', 'M', 'M', '.', 'Y', 'Y', 'Y'],
     ['M', 'M', '4', '.', '.', 'Y', 'Y'],
     ['M', 'M', '.', '.', '4', 'Y', 'Y'],
     ['M', 'M', '.', '.', '.', 'Y', 'Y'],
     ['M', 'M', 'M', '.', 'Y', 'Y', 'Y'],
     ['.', 'M', '.', '.', '.', '.', '.'],
     ['.', 'O', 'O', 'O', 'O', '.', '.']],
    [['.', '.', 'Y', 'Y', 'Y', 'Y', '.'],
     ['.', '.', '.', '.', '.', 'R', '.'],
     ['O', 'O', 'O', '.', 'R', 'R', 'R'],
     ['O', 'O', '4', '.', '.', 'R', 'R'],
     ['O', 'O', '.', '.', '4', 'R', 'R'],
     ['O', 'O', '.', '.', '.', 'R', 'R'],
     ['O', 'O', 'O', '.', 'R', 'R', 'R'],
     ['.', 'O', '.', '.', '.', '.', 'R'],
     ['.', 'Y', 'Y', 'Y', 'Y', '.', 'R']]]

LEVEL004 = [
    [['.', '.', '.', '.', '.', 'R', 'Y', 'Y', 'Y', '.', '.', '.', '.'],
     ['.', '.', '.', '.', 'R', 'R', 'R', '.', '.', '.', '.', '.', 'Y'],
     ['.', 'G', 'G', '.', 'R', 'W', 'R', 'R', '.', 'R', 'R', 'R', 'Y'],
     ['R', 'G', 'G', 'R', 'R', 'R', 'W', 'R', 'R', 'R', 'R', 'R', 'Y'],
     ['R', 'G', 'G', 'R', 'R', 'R', 'W', 'W', 'R', '.', '.', '.', '.'],
     ['R', 'G', 'G', 'R', 'R', 'R', 'W', 'R', 'R', 'R', 'R', 'R', 'Y'],
     ['.', 'G', 'G', '.', 'R', 'W', 'R', 'R', '.', 'R', 'R', 'R', 'Y'],
     ['.', '.', '.', '.', 'R', 'R', 'R', '.', '.', '.', '.', '.', 'Y'],
     ['.', '.', '.', '.', '.', 'R', 'Y', 'Y', 'Y', '.', '.', '.', '.']]]

LEVEL005 = [
    [['S'],
     ['M'],
     ['B'],
     ['C'],
     ['G'],
     ['Y'],
     ['O'],
     ['R'],
     ['S']],
    [['S'],
     ['M'],
     ['B'],
     ['C'],
     ['G'],
     ['Y'],
     ['O'],
     ['R'],
     ['S']],
    [['S'],
     ['M'],
     ['B'],
     ['C'],
     ['G'],
     ['Y'],
     ['O'],
     ['R'],
     ['S']],
    [['S'],
     ['M'],
     ['B'],
     ['C'],
     ['G'],
     ['Y'],
     ['O'],
     ['R'],
     ['S']],
    [['S'],
     ['M'],
     ['B'],
     ['C'],
     ['G'],
     ['Y'],
     ['O'],
     ['R'],
     ['S']],
    [['S'],
     ['M'],
     ['B'],
     ['C'],
     ['G'],
     ['Y'],
     ['O'],
     ['R'],
     ['S']],
    [['S'],
     ['M'],
     ['B'],
     ['C'],
     ['G'],
     ['Y'],
     ['O'],
     ['R'],
     ['S']]]

LEVEL006 = [
    [['.', '.', '.', '.', 'M', '.', 'M', '.', '.', '.', '.'],
     ['.', '.', '.', '.', 'M', '.', 'M', '.', '.', '.', '.'],
     ['.', '.', '.', 'M', 'M', 'M', 'M', 'M', '.', '.', '.'],
     ['M', 'M', 'M', 'M', 'R', 'M', 'R', 'M', 'M', 'M', 'M'],
     ['.', '.', '.', 'M', 'M', 'M', 'M', 'M', '.', '.', '.'],
     ['.', 'B', 'B', 'B', 'M', 'M', 'M', 'B', 'B', 'B', '.'],
     ['B', 'B', 'B', '.', 'M', 'M', 'M', '.', 'B', 'B', 'B'],
     ['B', 'B', '.', '.', '.', 'M', '.', '.', '.', 'B', 'B']]]

LEVEL007 = [
    [['C', 'C', 'C', 'C', 'C', 'C', 'C'],
     ['C', '.', '4', '.', '.', '.', '.'],
     ['C', '.', '.', '.', '4', '.', '.'],
     ['C', '.', '.', '.', '.', '.', '.'],
     ['C', 'B', 'B', 'B', 'B', 'B', 'B'],
     ['C', '.', '.', '.', '4', '.', '.'],
     ['C', '.', '4', '.', '.', '.', '.'],
     ['C', '.', '.', '.', '.', '.', '.'],
     ['C', 'C', 'C', 'C', 'C', 'C', 'C']],
    [['C', 'C', 'C', 'C', 'C', 'C', 'C'],
     ['.', '.', '.', '.', '4', '.', 'C'],
     ['.', '.', '4', '.', '.', '.', 'C'],
     ['.', '.', '.', '.', '.', '.', 'C'],
     ['B', 'B', 'B', 'B', 'B', 'B', 'C'],
     ['.', '.', '4', '.', '.', '.', 'C'],
     ['.', '.', '.', '.', '4', '.', 'C'],
     ['.', '.', '.', '.', '.', '.', 'C'],
     ['C', 'C', 'C', 'C', 'C', 'C', 'C']]]

LEVEL008 = [
    [['G', 'C', 'B', '.', '.', '.', '.'],
     ['.', 'G', 'C', 'B', '.', '.', '.'],
     ['3', '.', 'G', 'C', 'B', '.', '.'],
     ['.', '.', '3', 'G', 'C', 'B', '.'],
     ['.', '.', '.', '.', 'G', 'C', 'B'],
     ['3', '.', '.', 'G', 'C', 'B', '.'],
     ['.', '.', 'G', 'C', 'B', '.', '.'],
     ['.', 'G', 'C', 'B', '.', '.', '.'],
     ['G', 'C', 'B', '.', '.', '.', '.']],
    [['.', '.', '.', '.', 'B', 'C', 'G'],
     ['.', '.', '.', 'B', 'C', 'G', '.'],
     ['.', '.', 'B', 'C', 'G', '.', '3'],
     ['.', 'B', 'C', 'G', '.', '.', '.'],
     ['B', 'C', 'G', '.', '3', '.', '.'],
     ['.', 'B', 'C', 'G', '.', '.', '3'],
     ['.', '.', 'B', 'C', 'G', '.', '.'],
     ['.', '.', '.', 'B', 'C', 'G', '.'],
     ['.', '.', '.', '.', 'B', 'C', 'G']]]

LEVEL009 = [
    [['R', 'M', 'B', 'Y', 'O', 'G', 'C', 'S', '.', '.', '4', '.', '4'],
     ['R', 'M', 'B', 'Y', 'O', 'G', 'C', 'S', '.', '.', '.', '.', '.'],
     ['R', 'M', 'B', 'Y', 'O', 'G', 'C', 'S', '.', '.', '.', '.', '.'],
     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '4', '.', '4'],
     ['4', '.', '4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
     ['.', '.', '.', '.', '.', 'S', 'R', 'M', 'B', 'Y', 'O', 'G', 'C'],
     ['4', '.', '4', '.', '.', 'S', 'R', 'M', 'B', 'Y', 'O', 'G', 'C'],
     ['.', '.', '.', '.', '.', 'S', 'R', 'M', 'B', 'Y', 'O', 'G', 'C']]]

LEVEL010 = [
    [['.', '.', 'Y', 'Y', '.'],
     ['.', 'Y', 'Y', 'Y', 'Y'],
     ['.', 'Y', 'Y', 'Y', '.'],
     ['3', 'Y', 'Y', '.', '.'],
     ['.', 'Y', '.', '.', '.'],
     ['.', 'Y', 'Y', '.', '.'],
     ['.', 'Y', 'Y', 'Y', '.'],
     ['.', 'Y', 'Y', 'Y', 'Y'],
     ['.', '.', 'Y', 'Y', '.']],
    [['.', '.', 'R', 'R', 'R', 'R', '.'],
     ['.', 'R', 'W', 'W', 'R', '.', '.'],
     ['.', 'R', 'W', 'B', 'R', 'R', '.'],
     ['3', 'R', 'R', 'R', 'R', '.', '3'],
     ['.', 'R', 'R', 'R', 'R', 'R', '.'],
     ['.', 'R', 'R', 'R', 'R', '.', '.'],
     ['.', 'R', 'W', 'B', 'R', 'R', '.'],
     ['.', 'R', 'W', 'W', 'R', '.', '.'],
     ['.', '.', 'R', 'R', 'R', 'R', '.']]]

LEVEL011 = [
    [['.', '.', '.', '.', 'B', 'B', 'B', '.', '.', '.', '.'],
     ['.', '.', '.', 'B', 'B', '.', 'B', 'B', '.', '.', '.'],
     ['.', '.', 'B', 'B', '.', '.', '.', 'B', 'B', '.', '.'],
     ['.', 'B', 'B', '.', '0', '.', '.', '.', 'B', 'B', '.'],
     ['B', 'B', '.', '.', '.', '.', '0', '.', '.', 'B', 'B'],
     ['.', 'B', 'B', '.', '.', '.', '.', '.', 'B', 'B', '.'],
     ['.', '.', 'B', 'B', '.', '.', '.', 'B', 'B', '.', '.'],
     ['.', '.', '.', 'B', 'B', '.', 'B', 'B', '.', '.', '.'],
     ['.', '.', '.', '.', 'B', 'B', 'B', '.', '.', '.', '.']]]

LEVEL012 = [
    [['O', 'O', 'O', 'G', 'G', 'R', 'B', 'M', 'M', 'M', 'B', 'B', 'B'],
     ['O', '1', 'G', 'G', 'R', 'R', 'B', '.', 'M', '.', '.', '1', 'B'],
     ['M', '.', 'B', 'B', 'R', 'B', 'B', '.', 'O', 'O', 'C', '.', 'M'],
     ['M', 'M', 'B', 'G', '.', 'C', 'C', 'C', 'C', 'O', 'C', 'M', 'M'],
     ['M', '1', 'B', 'G', 'G', 'O', 'Y', 'Y', '.', 'O', 'C', '1', 'M'],
     ['B', '.', 'R', 'R', 'G', 'O', 'Y', 'Y', 'M', '.', 'C', '.', 'O'],
     ['B', 'B', 'B', 'R', 'R', 'O', 'O', 'M', 'M', 'M', 'O', 'O', 'O']]]

LEVEL013 = [
    [['.', '.', 'C', '.', '.'],
     ['.', 'C', 'B', 'C', '.'],
     ['C', 'B', '.', 'B', 'C'],
     ['C', '4', '.', '.', 'C'],
     ['C', '.', '.', '4', 'B'],
     ['B', '.', '.', '.', 'B'],
     ['B', 'C', '.', 'C', 'B'],
     ['.', 'B', 'C', 'B', '.'],
     ['.', '.', 'B', '.', '.']],
    [['.', 'O', '.'],
     ['O', 'O', 'O'],
     ['O', 'O', 'O'],
     ['O', 'O', 'O'],
     ['.', 'O', '.']],
    [['.', '.', 'C', '.', '.'],
     ['.', 'C', 'B', 'C', '.'],
     ['C', 'B', '.', 'B', 'C'],
     ['C', '4', '.', '.', 'C'],
     ['C', '.', '.', '4', 'B'],
     ['B', '.', '.', '.', 'B'],
     ['B', 'C', '.', 'C', 'B'],
     ['.', 'B', 'C', 'B', '.'],
     ['.', '.', 'B', '.', '.']]]

LEVEL014 = [
    [['A', '.', 'S', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
     ['G', '.', 'S', '.', '.', '.', '.', '.', 'G', '.', '.', '.', 'G'],
     ['G', '.', 'G', '.', 'G', 'G', 'G', '.', 'G', '.', 'G', '.', 'G'],
     ['G', '.', 'G', '.', 'G', '.', '1', '.', 'G', '.', 'G', '.', 'G'],
     ['G', '.', 'G', '.', 'G', '1', '.', '1', 'G', '.', 'G', '.', 'G'],
     ['G', '.', 'G', '.', 'G', '.', '.', '.', 'G', '.', 'G', '.', 'G'],
     ['G', '.', 'G', '.', 'G', '.', 'G', 'G', 'G', '.', 'G', '.', 'G'],
     ['G', '.', '.', '.', 'G', '.', '.', '.', '.', '.', 'S', '.', 'G'],
     ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'S', '.', 'A']]]

LEVEL015 = [
    [['W', '.', 'W'],
     ['W', '.', 'W'],
     ['W', '.', 'W'],
     ['3', 'W', '.'],
     ['.', 'W', '3'],
     ['.', 'W', '.'],
     ['W', '.', 'W'],
     ['W', '.', 'W'],
     ['W', '.', 'W']],
    [['C', '.', 'C'],
     ['C', '.', 'C'],
     ['C', '.', 'C'],
     ['3', 'C', '.'],
     ['.', 'C', '3'],
     ['.', 'C', '.'],
     ['C', '.', 'C'],
     ['C', '.', 'C'],
     ['C', '.', 'C']],
    [['G', '.', 'G'],
     ['G', '.', 'G'],
     ['G', '.', 'G'],
     ['3', 'G', '.'],
     ['.', 'G', '3'],
     ['.', 'G', '.'],
     ['G', '.', 'G'],
     ['G', '.', 'G'],
     ['G', '.', 'G']],
    [['Y', '.', 'Y'],
     ['Y', '.', 'Y'],
     ['Y', '.', 'Y'],
     ['3', 'Y', '.'],
     ['.', 'Y', '3'],
     ['.', 'Y', '.'],
     ['Y', '.', 'Y'],
     ['Y', '.', 'Y'],
     ['Y', '.', 'Y']]]

LEVEL016 = [
    [['C', 'C', 'C'],
     ['C', '.', 'C'],
     ['C', '.', 'C'],
     ['C', '.', 'C'],
     ['C', 'C', 'C'],
     ['C', '.', '.'],
     ['C', '.', '.'],
     ['C', '.', '.'],
     ['C', '.', '.']],
    [['G', 'G', 'G'],
     ['G', '.', 'G'],
     ['G', '.', 'G'],
     ['G', '.', 'G'],
     ['G', '.', 'G'],
     ['G', '.', 'G'],
     ['G', 'G', 'G']],
    [['M', 'M', '.'],
     ['M', '.', 'M'],
     ['M', '.', 'M'],
     ['M', '.', 'M'],
     ['M', '.', 'M'],
     ['M', '.', 'M'],
     ['M', '.', 'M']],
    [['R', 'R', 'R'],
     ['R', '.', 'R'],
     ['R', '.', 'R'],
     ['R', '.', 'R'],
     ['R', 'R', 'R'],
     ['.', '.', 'R'],
     ['.', '.', 'R'],
     ['.', '.', 'R'],
     ['R', 'R', 'R']]]

LEVEL017 = [
    [['W', 'W', 'W', '.', '.', 'R', 'R', 'R', '.', '.', 'W', 'W', 'W'],
     ['W', 'W', '.', '.', 'R', 'O', 'O', 'O', 'R', '.', '.', 'W', 'W'],
     ['W', '.', '.', 'R', 'O', 'Y', 'Y', 'Y', 'O', 'R', '.', '.', 'W'],
     ['1', '.', 'R', 'O', 'Y', 'B', 'B', 'B', 'Y', 'O', 'R', '.', '.'],
     ['.', '.', 'R', 'O', 'Y', 'B', '.', 'B', 'Y', 'O', 'R', '.', '.'],
     ['.', 'R', 'O', 'Y', 'B', '.', '.', '.', 'B', 'Y', 'O', 'R', '1'],
     ['.', 'R', 'O', 'Y', 'B', '.', '.', '.', 'B', 'Y', 'O', 'R', '.'],
     ['R', 'O', 'Y', 'B', '.', '.', '.', '.', '.', 'B', 'Y', 'O', 'R'],
     ['R', 'O', 'Y', 'B', '.', '.', '.', '.', '.', 'B', 'Y', 'O', 'R']]]

LEVEL018 = [
    [['.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', '.'],
     ['G', '.', '.', '.', '.', '0', '.', '.', '.', '.', 'G'],
     ['G', '0', '.', '.', '.', '.', '.', '.', '.', '0', 'G'],
     ['G', '.', '.', 'R', 'S', 'S', 'S', 'R', '.', '.', 'G'],
     ['G', '.', '.', 'R', 'S', 'S', 'S', 'R', '.', '.', 'G'],
     ['G', '0', '.', 'R', 'S', 'S', 'S', 'R', '.', '0', 'G'],
     ['G', '.', '.', '.', '.', '0', '.', '.', '.', '.', 'G'],
     ['G', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'G'],
     ['.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', '.']]]

LEVEL019 = [
    [['B', '.', '.', '.', '.', '.', '.'],
     ['Y', 'B', '.', '.', '.', '.', '.'],
     ['B', 'Y', 'B', '.', '.', '.', '.'],
     ['.', 'B', 'Y', 'B', '.', '.', '.'],
     ['1', '.', 'B', 'Y', 'B', '.', '.'],
     ['.', '.', '.', 'B', 'Y', 'B', '.'],
     ['.', '.', '.', '.', 'B', 'Y', 'B'],
     ['1', '.', '1', '.', '1', 'B', 'Y'],
     ['.', '.', '.', '.', '.', '.', 'B']],
    [['W', '.', '1', '.', '1', '.', '1'],
     ['R', 'W', '.', '.', '.', '.', '.'],
     ['W', 'R', 'W', '.', '.', '.', '.'],
     ['.', 'W', 'R', 'W', '.', '.', '1'],
     ['.', '.', 'W', 'R', 'W', '.', '.'],
     ['.', '.', '.', 'W', 'R', 'W', '.'],
     ['.', '.', '.', '.', 'W', 'R', 'W'],
     ['.', '.', '.', '.', '.', 'W', 'R'],
     ['.', '.', '.', '.', '.', '.', 'W']]]

LEVEL020 = [
    [['M', 'M', '.', '.', '.'],
     ['2', '.', 'M', '.', '.'],
     ['.', '.', '.', 'M', '.'],
     ['.', '.', '.', '.', 'M'],
     ['A', '.', '2', '.', 'M'],
     ['.', '.', '.', '.', 'M'],
     ['2', '.', '.', 'M', '.'],
     ['.', '.', 'M', '.', '.'],
     ['M', 'M', '.', '.', '.']],
    [['R', '.', 'G'],
     ['R', '.', 'G'],
     ['.', 'A', '.'],
     ['B', '.', 'C'],
     ['B', '.', 'C']],
    [['.', '.', '.', 'M', 'M'],
     ['.', '.', 'M', '.', '2'],
     ['.', 'M', '.', '.', '.'],
     ['M', '.', '2', '.', '.'],
     ['M', '.', '.', '.', 'A'],
     ['M', '.', '.', '.', '.'],
     ['.', 'M', '.', '.', '2'],
     ['.', '.', 'M', '.', '.'],
     ['.', '.', '.', 'M', 'M']]]

LEVEL021 = [
    [['C', 'C', 'C'],
     ['C', '4', 'C'],
     ['C', '.', 'C'],
     ['C', 'C', 'C'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.']],
    [['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['R', 'R', 'R'],
     ['R', '4', 'R'],
     ['R', '.', 'R'],
     ['R', 'R', 'R']],
    [['O', 'O', 'O'],
     ['O', '4', 'O'],
     ['O', '.', 'O'],
     ['O', 'O', 'O'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.']],
    [['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['.', 'S', '.'],
     ['G', 'G', 'G'],
     ['G', '4', 'G'],
     ['G', '.', 'G'],
     ['G', 'G', 'G']]]

LEVEL022 = [
    [['.', '3', '.', '3', '.', '.', '.', '.', 'G', 'G', 'G', '.', '.'],
     ['.', '.', '.', '.', '.', '.', 'G', 'G', 'G', 'G', 'G', 'G', '.'],
     ['W', '.', '.', '.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['W', '.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['.', 'W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['.', '.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['.', '.', '.', '.', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
     ['.', '3', '.', '3', '.', '.', 'G', 'G', 'G', 'G', 'G', 'G', '.'],
     ['.', '.', '.', '.', '.', '.', '.', '.', 'G', 'G', 'G', '.', '.']]]

LEVEL023 = [
    [['.', 'G', 'G', 'G', '.'],
     ['G', 'G', 'G', 'G', 'G'],
     ['G', '0', '.', '.', 'G'],
     ['G', '.', '.', '.', 'G'],
     ['G', '.', '.', '.', 'G'],
     ['G', '.', '.', '0', 'G'],
     ['G', '.', '.', '.', 'G'],
     ['G', 'S', 'S', 'S', 'G'],
     ['.', 'G', 'G', 'G', '.']],
    [['.', 'C', 'C', 'C', '.'],
     ['C', 'S', 'S', 'S', 'C'],
     ['C', '.', '.', '0', 'C'],
     ['C', '.', '.', '.', 'C'],
     ['C', '.', '.', '.', 'C'],
     ['C', '0', '.', '.', 'C'],
     ['C', '.', '.', '.', 'C'],
     ['C', 'C', 'C', 'C', 'C'],
     ['.', 'C', 'C', 'C', '.']]]

LEVEL024 = [
    [['R', 'R', 'B', '1', 'O', 'O', 'C'],
     ['R', '.', 'B', '.', 'O', '.', 'C'],
     ['R', '.', 'B', '.', 'O', '.', 'C'],
     ['R', '.', 'B', '.', 'O', '.', 'C'],
     ['R', '.', 'B', '.', 'O', '.', 'C'],
     ['R', '.', 'B', '.', 'O', '.', 'C'],
     ['R', '.', 'B', '.', 'O', '.', 'C'],
     ['R', '1', 'B', '.', 'O', '1', 'C'],
     ['R', '.', 'B', 'B', 'O', '.', 'C']],
    [['W', '1', 'M', 'Y', 'Y', '1', 'G'],
     ['W', '.', 'M', '.', 'Y', '.', 'G'],
     ['W', '.', 'M', '.', 'Y', '.', 'G'],
     ['W', '.', 'M', '.', 'Y', '.', 'G'],
     ['W', '.', 'M', '.', 'Y', '.', 'G'],
     ['W', '.', 'M', '.', 'Y', '.', 'G'],
     ['W', '.', 'M', '.', 'Y', '.', 'G'],
     ['W', '.', 'M', '1', 'Y', '.', 'G'],
     ['W', 'M', 'M', '.', 'Y', 'G', 'G']]]

LEVEL025 = [
    [['.', 'M', '.'],
     ['.', 'M', '.'],
     ['.', 'M', '.'],
     ['M', '2', 'M'],
     ['M', '.', 'M'],
     ['M', '.', 'M'],
     ['.', 'M', '.'],
     ['.', 'M', '.'],
     ['.', 'M', '.']],
    [['.', 'O', '.'],
     ['.', 'O', '.'],
     ['.', 'O', '.'],
     ['O', '.', 'O'],
     ['O', '2', 'O'],
     ['O', '.', 'O'],
     ['.', 'O', '.'],
     ['.', 'O', '.'],
     ['.', 'O', '.']],
    [['.', 'B', '.'],
     ['.', 'B', '.'],
     ['.', 'B', '.'],
     ['B', '2', 'B'],
     ['B', '.', 'B'],
     ['B', '.', 'B'],
     ['.', 'B', '.'],
     ['.', 'B', '.'],
     ['.', 'B', '.']],
    [['.', 'R', '.'],
     ['.', 'R', '.'],
     ['.', 'R', '.'],
     ['R', '.', 'R'],
     ['R', '2', 'R'],
     ['R', '.', 'R'],
     ['.', 'R', '.'],
     ['.', 'R', '.'],
     ['.', 'R', '.']]]

LEVEL026 = [
    [['M', 'M', '.', '.', '.', '.'],
     ['M', 'M', '.', '.', '.', '.'],
     ['M', 'M', 'S', 'S', '.', '.'],
     ['M', 'M', 'G', 'G', '.', '.'],
     ['3', '.', 'G', 'G', '.', '.'],
     ['.', '.', 'G', 'G', 'C', 'C'],
     ['.', '.', 'S', 'S', 'C', 'C'],
     ['3', '.', '.', '.', 'C', 'C'],
     ['.', '.', '.', '.', 'C', 'C']],
    [['O', 'O', '.', '.', '.', '3'],
     ['O', 'O', '.', '.', '.', '.'],
     ['O', 'O', 'S', 'S', '.', '.'],
     ['O', 'O', 'B', 'B', '.', '3'],
     ['.', '.', 'B', 'B', '.', '.'],
     ['.', '.', 'B', 'B', 'R', 'R'],
     ['.', '.', 'S', 'S', 'R', 'R'],
     ['.', '.', '.', '.', 'R', 'R'],
     ['.', '.', '.', '.', 'R', 'R']]]

LEVEL027 = [
    [['C', 'C', 'C', 'C'],
     ['C', '0', '.', 'C'],
     ['C', '.', '.', 'C'],
     ['C', '.', '.', 'C'],
     ['C', '.', '.', 'C'],
     ['C', '.', '.', 'C'],
     ['C', '.', '0', 'C'],
     ['C', '.', '.', 'C'],
     ['C', 'C', 'C', 'C']],
    [['M', 'M', 'M'],
     ['M', 'M', 'M'],
     ['R', 'R', 'R'],
     ['R', 'R', 'R'],
     ['S', 'S', 'S'],
     ['O', 'O', 'O'],
     ['O', 'O', 'O'],
     ['Y', 'Y', 'Y'],
     ['Y', 'Y', 'Y']],
    [['B', 'B', 'B', 'B'],
     ['B', '.', '0', 'B'],
     ['B', '.', '.', 'B'],
     ['B', '.', '.', 'B'],
     ['B', '.', '.', 'B'],
     ['B', '.', '.', 'B'],
     ['B', '0', '.', 'B'],
     ['B', '.', '.', 'B'],
     ['B', 'B', 'B', 'B']]]

LEVEL028 = [
    [['.', '.', '.', '.', '.', 'S'],
     ['.', '.', '.', '.', 'S', 'M'],
     ['.', '.', '.', 'S', '.', 'M'],
     ['.', '.', 'S', '.', '.', 'M'],
     ['.', 'S', '.', '.', '4', 'M'],
     ['S', '.', '.', '.', '.', 'M'],
     ['M', 'M', 'M', 'M', 'M', 'M']],
    [['M', 'M', 'M', 'M', 'M', 'M'],
     ['M', '4', '.', '.', '.', 'S'],
     ['M', '.', '.', '.', 'S', '.'],
     ['M', '.', '.', 'S', '.', '.'],
     ['M', '.', 'S', '.', '.', '.'],
     ['M', 'S', '.', '.', '.', '.'],
     ['S', '.', '.', '.', '.', '.']]]

LEVEL029 = [
    [['A', 'A', 'A', 'A', 'A', '1'],
     ['W', 'W', 'W', 'W', 'W', '.'],
     ['B', 'B', 'B', 'B', 'B', '.'],
     ['M', 'M', 'M', 'M', 'M', '.'],
     ['R', 'R', 'R', 'R', 'R', '1'],
     ['S', 'S', 'S', 'S', 'S', '.']],
    [['1', 'S', 'S', 'S', 'S', 'S'],
     ['.', 'Y', 'Y', 'Y', 'Y', 'Y'],
     ['.', 'C', 'C', 'C', 'C', 'C'],
     ['.', 'O', 'O', 'O', 'O', 'O'],
     ['1', 'G', 'G', 'G', 'G', 'G'],
     ['.', 'A', 'A', 'A', 'A', 'A']]]

LEVEL030 = [
    [['.', 'R', '.', '.', '.'],
     ['R', '.', 'R', '.', 'B'],
     ['R', '.', '.', 'B', 'B'],
     ['R', '.', '3', '.', 'S'],
     ['R', '.', '.', '.', 'S'],
     ['R', '.', '.', 'B', 'B'],
     ['R', '.', 'R', '.', 'B'],
     ['.', 'R', '.', '.', '.']],
    [['.', '.', '.', 'M', '.'],
     ['C', '.', 'M', '.', 'M'],
     ['C', 'M', '.', '.', 'M'],
     ['S', '.', '3', '.', 'M'],
     ['S', '.', '.', '.', 'M'],
     ['C', 'M', '.', '.', 'M'],
     ['C', '.', 'M', '.', 'M'],
     ['.', '.', '.', 'M', '.']]]

LEVEL031 = [
    [['M'],
     ['M'],
     ['M'],
     ['M'],
     ['M'],
     ['M'],
     ['M'],
     ['M'],
     ['M']],
    [['B'],
     ['B'],
     ['B'],
     ['B'],
     ['B'],
     ['B'],
     ['B'],
     ['B'],
     ['B']],
    [['C'],
     ['C'],
     ['C'],
     ['C'],
     ['C'],
     ['C'],
     ['C'],
     ['C'],
     ['C']],
    [['G'],
     ['G'],
     ['G'],
     ['G'],
     ['G'],
     ['G'],
     ['G'],
     ['G'],
     ['G']],
    [['Y'],
     ['Y'],
     ['Y'],
     ['Y'],
     ['Y'],
     ['Y'],
     ['Y'],
     ['Y'],
     ['Y']],
    [['O'],
     ['O'],
     ['O'],
     ['O'],
     ['O'],
     ['O'],
     ['O'],
     ['O'],
     ['O']],
    [['R'],
     ['R'],
     ['R'],
     ['R'],
     ['R'],
     ['R'],
     ['R'],
     ['R'],
     ['R']]]

LEVEL032 = [
    [['.', 'W', 'W', 'W', 'W', 'W', '.', 'W', 'W', 'W', 'W', 'W', '.'],
     ['A', '.', '.', '.', '.', '2', 'W', '2', '.', '.', '.', '.', 'W'],
     ['W', '.', '.', '2', '.', '.', 'W', '.', '.', '2', '.', '.', 'W'],
     ['W', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', 'W'],
     ['W', '2', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '2', 'W'],
     ['W', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', 'A'],
     ['.', 'W', 'W', 'W', 'W', 'W', '.', 'W', 'W', 'W', 'W', 'W', '.']]]

LEVEL033 = [
    [['R', 'W', 'B'],
     ['R', 'W', 'B'],
     ['R', 'W', 'B'],
     ['R', 'W', 'B'],
     ['R', 'W', 'B']],
    [['S', 'S', 'S', 'S', 'S'],
     ['R', '3', '.', '3', 'R'],
     ['S', '.', '.', '.', 'S'],
     ['A', '.', '.', '.', 'A'],
     ['S', '3', '.', '3', 'S'],
     ['B', '.', '.', '.', 'B'],
     ['S', 'S', 'S', 'S', 'S']],
    [['B', 'W', 'R'],
     ['B', 'W', 'R'],
     ['B', 'W', 'R'],
     ['B', 'W', 'R'],
     ['B', 'W', 'R']]]

LEVEL034 = [
    [['R', 'R', 'R'],
     ['W', 'A', 'W'],
     ['B', '.', 'B'],
     ['R', '.', 'R'],
     ['W', '1', 'W'],
     ['B', '.', 'B']],
    [['R', 'R', 'R'],
     ['W', 'S', 'W'],
     ['B', '.', 'B'],
     ['R', '.', 'R'],
     ['W', '1', 'W'],
     ['B', '.', 'B']],
    [['C', '1', 'C'],
     ['Y', '.', 'Y'],
     ['M', '.', 'M'],
     ['C', '.', 'C'],
     ['Y', 'S', 'Y'],
     ['M', 'M', 'M']],
    [['C', '1', 'C'],
     ['Y', '.', 'Y'],
     ['M', '.', 'M'],
     ['C', '.', 'C'],
     ['Y', 'A', 'Y'],
     ['M', 'M', 'M']]]

LEVEL035 = [
    [['4', 'R', 'C', 'B'],
     ['.', 'S', 'S', 'S'],
     ['.', 'A', 'A', 'A'],
     ['4', 'S', 'S', 'S'],
     ['.', 'Y', 'O', 'M']],
    [['4', 'R', 'G', '4'],
     ['.', 'S', 'S', '.'],
     ['.', 'A', 'A', '.'],
     ['4', 'S', 'S', '4'],
     ['.', 'W', 'B', '.']],
    [['G', 'O', 'W', '4'],
     ['S', 'S', 'S', '.'],
     ['A', 'A', 'A', '.'],
     ['S', 'S', 'S', '4'],
     ['C', 'M', 'Y', '.']]]

LEVEL036 = [
    [['.', 'G', 'G', '.'],
     ['G', '.', '.', 'G'],
     ['G', '3', '.', 'G'],
     ['G', '.', '.', 'G'],
     ['G', '.', '.', 'G'],
     ['G', '.', '3', 'G'],
     ['G', '.', '.', 'G'],
     ['G', '.', '.', 'G'],
     ['.', 'G', 'G', '.']],
    [['.', '.', 'O', '.', '.'],
     ['.', 'O', '.', 'O', '.'],
     ['.', 'O', '.', 'O', '.'],
     ['O', '.', '.', '.', 'O'],
     ['O', '.', '3', '.', 'O'],
     ['O', '.', '.', '.', 'O'],
     ['.', 'O', '.', 'O', '.'],
     ['.', 'O', '.', 'O', '.'],
     ['.', '.', 'O', '.', '.']],
    [['.', 'B', 'B', '.'],
     ['B', '.', '.', 'B'],
     ['B', '3', '.', 'B'],
     ['B', '.', '.', 'B'],
     ['B', '.', '.', 'B'],
     ['B', '.', '3', 'B'],
     ['B', '.', '.', 'B'],
     ['B', '.', '.', 'B'],
     ['.', 'B', 'B', '.']]]

LEVEL037 = [
    [['W', 'W', 'W', 'W'],
     ['R', '2', '.', 'R'],
     ['B', '.', '.', 'B'],
     ['O', '.', '2', 'O'],
     ['C', '.', '.', 'C'],
     ['G', '2', '.', 'G'],
     ['Y', '.', '.', 'Y'],
     ['M', '.', '.', 'M']],
    [['W', 'W', 'W'],
     ['R', 'R', 'R'],
     ['B', 'B', 'B'],
     ['O', 'O', 'O'],
     ['C', 'C', 'C'],
     ['G', 'G', 'G'],
     ['Y', 'Y', 'Y'],
     ['M', 'M', 'M']],
    [['W', '.', '.', 'W'],
     ['R', '.', '2', 'R'],
     ['B', '.', '.', 'B'],
     ['O', '2', '.', 'O'],
     ['C', '.', '.', 'C'],
     ['G', '.', '2', 'G'],
     ['Y', '.', '.', 'Y'],
     ['M', 'M', 'M', 'M']]]

LEVEL038 = [
    [['.', '.', '.', '.', '0', '.', 'G'],
     ['.', '.', '.', '.', '.', 'G', 'R'],
     ['.', '.', '0', '.', 'G', 'R', '.'],
     ['.', '.', '.', 'G', 'R', '.', '.'],
     ['.', '.', 'G', 'R', '.', '.', '.'],
     ['.', 'G', 'R', '.', '.', '.', '.'],
     ['G', 'R', '.', '.', '0', '.', '0'],
     ['R', '.', '.', '.', '.', '.', '.']],
    [['B', '.', '0', '.', '.', '.', '.'],
     ['R', 'B', '.', '.', '.', '.', '.'],
     ['.', 'R', 'B', '.', '0', '.', '.'],
     ['.', '.', 'R', 'B', '.', '.', '.'],
     ['.', '.', '.', 'R', 'B', '.', '.'],
     ['.', '.', '.', '.', 'R', 'B', '.'],
     ['0', '.', '0', '.', '.', 'R', 'B'],
     ['.', '.', '.', '.', '.', '.', 'R']]]

LEVEL039 = [
    [['4', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', '4'],
     ['.', 'C', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'C', '.'],
     ['4', 'C', 'W', 'Y', 'Y', 'Y', 'Y', 'Y', 'W', 'C', '4'],
     ['.', 'C', 'W', 'Y', 'R', 'R', 'R', 'Y', 'W', 'C', '.'],
     ['.', 'C', 'W', 'Y', 'R', 'A', 'R', 'Y', 'W', 'C', '.'],
     ['4', 'C', 'W', 'Y', 'R', 'R', 'R', 'Y', 'W', 'C', '4'],
     ['.', 'C', 'W', 'Y', 'Y', 'Y', 'Y', 'Y', 'W', 'C', '.'],
     ['4', 'C', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'C', '4'],
     ['.', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', '.']]]


def get_level(level_number):
    """Get grid representing brick layout for level.

    Args:
        level_number(int): Level number.
    """
    level = globals().get(f"LEVEL{level_number:03d}")
    if level is None:
        raise ValueError("Invalid level number.")
    else:
        return level


def get_dimensions(level_number):
    """Get dimensions in pixels of all shapes in level grid.

    Args:
        level_number(int): Level number.
    """
    level = globals().get(f"LEVEL{level_number:03d}")
    if level is None:
        raise ValueError("Invalid level number.")
    else:
        dimensions = []
        for shape in level:
            dimensions.append([len(shape[0] * BRICK_WIDTH,),
                               len(shape) * BRICK_HEIGHT])
        return dimensions


def max_levels():
    """Return the maximum level number."""
    return sum(1 for const in globals() if const.startswith('LEVEL'))