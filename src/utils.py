#! /usr/bin/env python

import pygame, resources


def save(local, data):
    log = open(local, 'w')
    log.write(data)
    log.close()


def read(local, default=''):
    log = open(local, 'r')
    data = log.readline()
    if not len(data):
        data = default

    return data


class switch:
    def __init__(self, state=0):
        self.state = state

    def to(self, state):
        self.state = state

    def get(self):
        return self.state

    def equals(self, state):
        return (self.state == state)