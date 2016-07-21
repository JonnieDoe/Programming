#!/usr/bin/python -tt

__author__ = "DC"


# & Binary AND                  Operator copies a bit to the result if it exists in both operands                               (a & b) (means 0000 1100)
# | Binary OR                   It copies a bit if it exists in either operand.                                                 (a | b) = 61 (means 0011 1101)
# ^ Binary XOR                  It copies the bit if it is set in one operand but not both.                                     (a ^ b) = 49 (means 0011 0001)
# ~ Binary Ones Complement      It is unary and has the effect of 'flipping' bits.                                              (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
# << Binary Left Shift          The left operands value is moved left by the number of bits specified by the right operand.     a << = 240 (means 1111 0000)
# >> Binary Right Shift         The left operands value is moved right by the number of bits specified by the right operand.    a >> = 15 (means 0000 1111)


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)