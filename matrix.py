#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

from threading import Thread

from time import sleep

from terminalsize import get_terminal_size

from random import randint

EXIT_TEXT = 'red pill'

class MatrixOutput(object):
    """docstring for MatrixOutput"""
    def __init__(self):
        self.stdout = sys.stdout
        self.width, self.height = get_terminal_size()
        self.buffers = ['' for i in xrange(self.width)]
        self.in_matrix = True
        self.animation_thread = Thread(target=self.animation)
        self.clrscr()

        self.animation_thread.start()

    def clrscr(self):
        self.screen = [[' ' for i in xrange(self.width)] for j in xrange(self.height)]

    def print_screen(self):
        text = ''.join([''.join(line) for line in self.screen])      
        self.stdout.write(text)
        self.stdout.flush()

    def animation(self):
        while self.in_matrix:
            self.animation_step()
            sleep(0.2)
        sys.stdout = self.stdout

    def animation_step(self, step=1):
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

        if text == EXIT_TEXT:
            self.in_matrix = False

        column = randint(0, self.width)
        self.buffers[column] = text
        
        self.print_screen()

if __name__ == '__main__':
    sys.stdout = MatrixOutput()
    print 'Wake up, Neo.'
    sleep(2)
    print 'The Matrix has you...'
    sleep(2)
    print 'Follow the white rabbit'
    sleep(5)
    print 'red pill'
