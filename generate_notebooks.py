#!/bin/env python3
from optparse import OptionParser
import jupytext
import copy

parser = OptionParser()
parser.add_option('-s', '--solution', dest='solution_file',
                help='solution output file name')

parser.add_option('-e', '--exercise', dest='exercise_file',
                help='exercise output file name')

parser.add_option('-m', '--metadata', default='exercise_type',
                help='name of metadata field')

options, args = parser.parse_args()

original_notebook = jupytext.read(args[0])

def _filter(nb, t):
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

_filter_and_write(original_notebook, 'solution', options.solution_file)
_filter_and_write(original_notebook, 'exercise', options.exercise_file)

