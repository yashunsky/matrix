#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

class MatrixOutput(object):
    """docstring for MatrixOutput"""
    def __init__(self):
        self.stdout = sys.stdout
    def write(self, text):
        self.stdout.write(text)

if __name__ == '__main__':
    sys.stdout = MatrixOutput()
    print 'Wake up, Neo. The matrix has you'