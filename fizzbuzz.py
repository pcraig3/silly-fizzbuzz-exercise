#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fizzbuzz():
  sequence = []
  for i in range(1, 101):
    value = ''

    if i % 3 == 0:
      value = '{}{}'.format(value, 'Fizz')

    if i % 5 == 0:
      value = '{}{}'.format(value, 'Buzz')

    if not value:
      value = '{}'.format(i)

    sequence.append(value)

  return ','.join(sequence)
