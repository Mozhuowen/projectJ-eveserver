#!coding=utf-8

import random


def get_random_string(len):
    a = 'webhook-test-test-awen'
    return ''.join(random.sample('0123456789zyxwvutsrqponmlkjihgfedcbaQWERTYUIOPASDFGHJKLZXCVBNM', len))
