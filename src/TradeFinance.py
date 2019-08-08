'''
Created on Aug 6, 2019

@author: Brian
'''
from initialize import initialize
from cleanup import cleanup
from enigma_data import read_bill_of_lading_summary

if __name__ == '__main__':
    print('Hello World')
    f_out, tf_data_dir = initialize()

    df_bills_of_lading = read_bill_of_lading_summary(tf_data_dir)

    cleanup(f_out)
    print('Goodbye cruel world')
    pass