'''
Module with little tools and settings
'''
import argparse


def parse_args()->argparse.Namespace:
    '''
    First step. Parsing arguments of commandline
    :return:
    '''
    args = argparse.ArgumentParser()
    args.add_argument('-m', '--mode', help="Working mode type. Can be \"DEBUG\" or \"RELEASE\"")

    return args.parse_args()
