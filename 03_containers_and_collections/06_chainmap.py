import builtins


def get_basic(key):
    builtin_vars = vars(builtins)
    if key in locals():
        value = locals()[key]
    elif key in globals():
        value = globals()[key]
    elif key in builtin_vars:
        value = builtin_vars[key]
    else:
        raise NameError('name %r is not defined' % key)

##############################################################################


def get_improved(key):
    mappings = globals(), locals(), vars(builtins)
    for mapping in mappings:
        if key in mapping:
            value = mapping[key]
            break
    else:
        raise NameError('name %r is not defined' % key)

##############################################################################

import builtins
import collections


def get_chainmap(key):
    mappings = collections.ChainMap(globals(), locals(), vars(builtins))
    value = mappings[key]

##############################################################################

import argparse
import collections

defaults = {
    'spam': 'default spam value',
    'eggs': 'default eggs value',
}

parser = argparse.ArgumentParser()
parser.add_argument('--spam')
parser.add_argument('--eggs')

args = vars(parser.parse_args())
# We need to check fo empty/default values so we can't simply use vars(args)
filtered_args = {k: v for k, v in args.items() if v}

combined = collections.ChainMap(filtered_args, defaults)

print(combined['spam'])

##############################################################################

print(combined.maps[1]['spam'])

for map_ in combined.maps:
    print(map_.get('spam'))

