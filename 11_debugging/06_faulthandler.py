import ctypes

# Get memory address 0, your kernel shouldn't allow this:
ctypes.string_at(0)

##############################################################################

import ctypes

try:
    # Get memory address 0, your kernel shouldn't allow this:
    ctypes.string_at(0)
except Exception as e:
    print('Got exception:', e)

##############################################################################

import ctypes
import faulthandler

faulthandler.enable()

# Get memory address 0, your kernel shouldn't allow this:
ctypes.string_at(0)
