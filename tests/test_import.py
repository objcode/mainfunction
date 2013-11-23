#!/usr/bin/env python

from mainfunction import mainfunction

assert __name__ != '__main__'

results=[]

@mainfunction
def foo():
    results.append('foo')

def bar():
    results.append('bar')

@mainfunction
def baz():
    results.append('baz')

assert results == []

foo()
bar()
baz()

assert results == ['foo', 'bar', 'baz']

