'''
Created on Aug 6, 2019

@author: Brian
'''
from initialize import initialize
from cleanup import cleanup

if __name__ == '__main__':
    print('Hello World')
    f_out = initialize()

    cleanup(f_out)
    print('Goodbye cruel world')
    pass