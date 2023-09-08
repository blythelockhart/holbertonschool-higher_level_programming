#!/usr/bin/python3

import sys
argv = sys.argv[1:]
num_args = len(argv)
if num_args == 0:
    print('0 arguments.')
elif num_args == 1:
    print('1 argument:')
    print('1: {}'.format(argv[1])) 
else:
    print('{} arguments:'.format(num_args))
    for i in range(num_args):
        print('{}: {}'.format(i, argv[i]))
