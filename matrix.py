#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''On include this module switches stdout to 'The Matrix'-style.
   printed text is split by lines, and put in random columns,
   witch move down at random speed with a random delay.
   After print 'red pill' is executed, the animation stops
   and sys.stdout is restored.
   '''

import sys

from threading import Thread

from time import sleep

from terminalsize import get_terminal_size

from random import randint

EXIT_TEXT = 'red pill'
SPEED_RANGE = 5
SPEED_SELECTOR = 120 # = SPEED_RANGE!
MAX_SPEED = 2

class MatrixOutput(object):
    """docstring for MatrixOutput"""
    def __init__(self):
        self.stdout = sys.stdout
        self.width, self.height = get_terminal_size()
        self.buffers = ['' for i in xrange(self.width)]
        self.speed = [randint(-SPEED_RANGE, MAX_SPEED) 
                      for i in xrange(self.width)]
        self.in_matrix = True
        self.counter = 0
        self.animation_thread = Thread(target=self.animation)
        self.clrscr()

        self.animation_thread.start()

    def clrscr(self):
        self.screen = [[' ' for i in xrange(self.width)]
                       for j in xrange(self.height)]

    def print_screen(self):
        text = ''.join([''.join(line) for line in self.screen])      
        self.stdout.write(text)
        self.stdout.flush()

    def animation(self):
        while self.in_matrix:
            self.animation_step()
            sleep(0.1)
        sys.stdout = self.stdout

    def animation_step(self):
        for column in xrange(self.width):
            step = self.speed[column]
            if step <= 0:
                step = -step + 1
                if self.counter % step == 0:
                    step = 1
                else:
                    step = 0
            self.counter = (self.counter + 1) % SPEED_SELECTOR
            column_string = ''.join([self.screen[row][column] 
                                     for row in xrange(self.height)])
            column_string = ' '*step + self.buffers[column] + column_string
            column_string = column_string[:-step]
            (self.buffers[column], 
             column_string) = (column_string[:-self.height], 
                               column_string[-self.height:])
            for row, letter in enumerate(column_string):
                self.screen[row][column] = letter

        self.print_screen()

    def add_line(self, line):
        column = randint(0, self.width - 1)
        self.buffers[column] = line + self.buffers[column]

    def write(self, text):
        text = text.rstrip()
        if len(text) == 0: return

        if text == EXIT_TEXT:
            self.in_matrix = False

        for line in text.split('\n'):
            self.add_line(line + ' ' * randint(0, self.height))       

# this line is here not by mistake, but for autoexecution in case of include
sys.stdout = MatrixOutput()

if __name__ == '__main__':
    print '''Wake up, Neo.
             The Matrix has you...
             Follow the white rabbit'''
    print '\n'.join([''.join([str(randint(0, 1)) 
                              for j in xrange(randint(0,5))]) 
                     for i in xrange(100)])


    sleep(10)
    print 'red pill'
    sleep(0.5)
    print 'welcome to real world'
