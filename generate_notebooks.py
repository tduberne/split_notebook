#!/bin/env python3
from optparse import OptionParser
import jupytext
import copy

parser = OptionParser()
parser.add_option('-s', '--solution', dest='solution_file',
                help='solution output file name')

parser.add_option('--solution-name', dest='solution_name',
                default='solution',
                help='value of the metadata for solution cells')

parser.add_option('-e', '--exercise', dest='exercise_file',
                help='exercise output file name')

parser.add_option('--exercise-name', dest='exercise_name',
                default='exercise',
                help='value of the metadata for exercise cells')

parser.add_option('-m', '--metadata', default='exercise_type',
                help='name of metadata field')

options, args = parser.parse_args()

original_notebook = jupytext.read(args[0])

def _filter(nb, t):
    if t is None:
        raise ValueError('type was None')

    filtered = copy.deepcopy(nb)
    filtered['cells'] = [
        cell
        for cell in filtered['cells']
        if cell['metadata'].get(options.metadata, t) == t
    ]

    return filtered

def _filter_and_write(nb, t, out):
    if out:
        jupytext.write(_filter(nb, t), out)

_filter_and_write(original_notebook, options.solution_name, options.solution_file)
_filter_and_write(original_notebook, options.exercise_name, options.exercise_file)

