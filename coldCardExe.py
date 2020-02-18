from ckcc.cli import get_block_chain, get_version, _list, get_xpub, get_fingerprint
import sys
import hidapi
arguments = sys.argv[1:]
print(arguments)
if (arguments[0] == 'list'):
    _list()
if (arguments[0] == 'xpub'):
    get_xpub(arguments[1])
if (arguments[0] == 'xfp'):
    get_fingerprint(False)
