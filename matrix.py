#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

from threading import Thread

from terminalsize import get_terminal_size

class MatrixOutput(object):
    """docstring for MatrixOutput"""
    def __init__(self):
        self.stdout = sys.stdout
        self.width, self.height = get_terminal_size()
        
        self.clrscr()

    def clrscr(self):
        self.screen = [[' ' for i in xrange(self.width)] for j in xrange(self.height)]

    def print_screen(self):      
        self.stdout.write(''.join([''.join(line) for line in self.screen]))

    def write(self, text):
        text = text.rstrip()
        if len(text) == 0: return

        for i in xrange(self.height):
            self.screen[i][i] = '*'
        self.print_screen()
        #self.stdout.write(text)

if __name__ == '__main__':
    sys.stdout = MatrixOutput()
    print 'Wake up, Neo. The matrix has you'