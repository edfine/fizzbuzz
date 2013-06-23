#!/usr/bin/env python
# encoding: utf-8
"""
fizzbuzz.py

Created by Ed Fine on 2013-06-22.
Copyright (c) 2013 __AFineFellow__. CC Attribution Some rights reserved.
"""

import sys
import os
import unittest


def main():
  for i in range(100):
		if ((i+1) % 3)==0 and ((i+1) % 5)==0:
			print "fizzbuzz"
		elif  ((i+1) % 3)!=0 and ((i+1) % 5)==0:
			print "buzz"
		elif  ((i+1) % 3)==0 and ((i+1) % 5)!=0:
			print "fizz"
		else:
			print str(i+1)



if __name__ == '__main__':
	main()
