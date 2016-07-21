#!/usr/bin/python -tt

__author__ = "DC"


# is        Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.     x is y
# is not    Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.     x is not y

a = 20
b = 20

if ( a is b ):
   print ("Line 1 - a and b have same identity")
else:
   print ("Line 1 - a and b do not have same identity")

if ( id(a) == id(b) ):
   print ("Line 2 - a and b have same identity")
else:
   print ("Line 2 - a and b do not have same identity")

b = 30
if ( a is b ):
   print ("Line 3 - a and b have same identity")
else:
   print ("Line 3 - a and b do not have same identity")

if ( a is not b ):
   print ("Line 4 - a and b do not have same identity")
else:
   print ("Line 4 - a and b have same identity")
