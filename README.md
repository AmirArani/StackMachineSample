# Stack Machine

**A stack Machine Example. Implemented by Python**

to accept    L1={0^n 1^m | n>=1, m>=1, m>n+2}
_________________________________________    

There is TWO main if condition. If input can pass one of them then it's OK

FIRST: if check input if first input is 1. Then it's NOT ACCEPTED.

SECOND: one is for when first input is 0. Then we count 0's and save the number with stack. Then append 3 more 1 to stack and then check number of 1's.
    There is 3 possiblity: ONE: 1's are less than stack length which is NOT ACCEPTED. TWO: 1's are same as stack length. THREE: 1's are more than stack length.


_________________________________________    
NOTE: Enter your string like 0011111.

