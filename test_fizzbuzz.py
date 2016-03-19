#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fizzbuzz import fizzbuzz

class TestFizzBuzz():

  def test_fizzbuzz_returns_string_of_integers(self):
    string_of_integers = fizzbuzz()
    assert isinstance(string_of_integers, str)

    array_of_integers = string_of_integers.split(',')
    assert isinstance(array_of_integers, list)

  def assert_index_contains_value(self, index, value):
    fizzbuzz_array = fizzbuzz().split(',')
    assert value in fizzbuzz_array[index-1]

  def assert_index_multiples_contain_value(self, multiple, value):
    for i in range(1, 100):
      if i % multiple == 0:
        self.assert_index_contains_value(i, value)

  def test_value_at_first_index_is_one(self):
    self.assert_index_contains_value(1, '1')

  def test_value_at_second_index_is_two(self):
    self.assert_index_contains_value(2, '2')

  def test_value_at_fourth_index_is_four(self):
    self.assert_index_contains_value(4, '4')

  def test_value_at_third_index_is_Fizz(self):
    self.assert_index_multiples_contain_value(3, 'Fizz')

  def test_value_at_fifth_index_is_Buzz(self):
    self.assert_index_multiples_contain_value(5, 'Buzz')

  def test_value_at_fifthteen_index_is_FizzBuzz(self):
    self.assert_index_multiples_contain_value(15, 'FizzBuzz')


