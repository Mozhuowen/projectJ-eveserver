#!coding=utf-8

import random


def get_random_string(len):
    a = '0720-test'
    return ''.join(random.sample('0123456789zyxwvutsrqponmlkjihgfedcbaQWERTYUIOPASDFGHJKLZXCVBNM', len))
