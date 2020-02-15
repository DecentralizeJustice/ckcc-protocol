from ckcc.cli import get_block_chain, get_version, _list
import sys
arguments = sys.argv[1:]
print(arguments)
if (arguments[0] == 'list'):
    _list()
