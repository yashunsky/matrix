#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

from threading import Thread

from time import sleep

from terminalsize import get_terminal_size

from random import randint

class MatrixOutput(object):
    """docstring for MatrixOutput"""
    def __init__(self):
        self.stdout = sys.stdout
        self.width, self.height = get_terminal_size()
        self.buffers = ['' for i in xrange(self.width)]

        self.clrscr()

    def clrscr(self):
        self.screen = [[' ' for i in xrange(self.width)] for j in xrange(self.height)]

    def print_screen(self):
        text = ''.join([''.join(line) for line in self.screen])      
        self.stdout.write(text)
        self.stdout.flush()

    def write(self, text):
        text = text.rstrip()
        if len(text) == 0: return

        column = randint(0, self.width)
        for row, letter in enumerate(text):
            self.screen[row + 1][column] = letter
        
        self.print_screen()

if __name__ == '__main__':
    sys.stdout = MatrixOutput()
    print 'Wake up, Neo.'
    sleep(2)
    print 'The Matrix has you...'
    sleep(2)
    print 'Follow the white rabbit'
