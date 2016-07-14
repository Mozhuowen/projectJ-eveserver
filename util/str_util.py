#!coding=utf-8

import random


def get_random_string(len):
    return ''.join(random.sample('0123456789zyxwvutsrqponmlkjihgfedcbaQWERTYUIOPASDFGHJKLZXCVBNM', len))
