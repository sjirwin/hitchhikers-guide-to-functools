import sys
from functools import partial
print_stderr = partial(print, file=sys.stderr)
print_stderr('This output goes to stderr')