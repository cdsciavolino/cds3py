"""
General framework for reading/writing data from/to files on
the local system.
"""

import json


###############################################################################
#   FILE READING              #################################################
###############################################################################

def read_file(infile, handle_file, log=False):
    if log:
        print('Opening "{}"...'.format(infile))
    data = None
    with open(infile) as f:
        data = handle_file(f)
    if log:
        print('  Done.')
    return data


def read_json(infile, log=False):
    handler = lambda f: json.load(f)
    return read_file(infile, handler, log=log)


def read_jsonl(infile, log=False):
    handler = lambda f: [json.loads(line) for line in f.readlines()]
    return read_file(infile, handler, log=log)


###############################################################################
#   FILE WRITING              #################################################
###############################################################################

def write_file(outfile, handle_file, log=False):
    if log:
        print('Writing to "{}"...'.format(outfile))
    with open(outfile, 'w+') as f:
        handle_file(f)
    if log:
        print('  Done.')


def write_json(outfile, data, log=False, pretty=False):
    handler = lambda f: f.write(json.dumps(data, indent=4 if pretty else None))
    write_file(outfile, handler, log=log)
    

"""
TODO:

read_csv
read_tsv
read_with_limit (e.g. only read 10 lines)
write_jsonl
write_csv
write_tsv
reading/writing config yamls
argparse from yaml
timing - time a function
easy logging/logger
"""

