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

    def animate(self, step=1):
        for column in xrange(self.width):
            column_string = ''.join([self.screen[row][column] for row in xrange(self.height)])
            column_string = ' '*step + self.buffers[column] + column_string
            column_string = column_string[:-step]
            self.buffers[column], column_string = column_string[:-self.height], column_string[-self.height:]
            for row, letter in enumerate(column_string):
                self.screen[row][column] = letter

        self.print_screen()

    def write(self, text):
        text = text.rstrip()
        if len(text) == 0: return

        column = randint(0, self.width)
        self.buffers[column] = text
        
        self.print_screen()

if __name__ == '__main__':
    sys.stdout = MatrixOutput()
    print 'Wake up, Neo.'
    print 'The Matrix has you...'
    print 'Follow the white rabbit'
    for i in xrange(50):
        sys.stdout.animate()
        sleep(0.1)
