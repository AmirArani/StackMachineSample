# A STACK MACHINE TO ACCEPT L1={0^N 1^M | N>=1, M>=1, M>N+2}

print ("Enter your string. (Example: 01111)")
input_str = input("ENTER: ")
input = list(input_str)		#convert input string to list

stack = []
index = 0

# There is TWO main if condition. If input can pass one of them then it's OK
# FIRST	 if check input if first input is 1. Then it's NOT ACCEPTED.
# SECOND one is for when first input is 0. Then we count 0's and save the number with stack. Then append 3 more 1 to stack and...
#	...then check number of 1's.


#FIRST
if input[index] == '1':
	print ("NOT ACCEPTED!")
	exit()

#SECOND
elif input[index] == '0':
	while input[index] == '0':	# count 0's in this loop.
		index = index+1
		stack.append(0)		# if there is 0 in input line push 0 to stack
		if len(input) == index: # but if there is not any 1 its NOT ACCEPTED
			print ("NOT ACCEPTED")
			exit()

	#___END OF WHILE___

	stack.append(0)			# add three more 0's to stack
	stack.append(0)			# we do this for condition of this machine
	stack.append(0)


	while len(stack) != 0:		# now check is there enough 1 in input or not
		if input[index] == '1':
			index = index+1
		else:
			print ("NOT ACCEPTED!")
			exit()

		stack.pop()

		if index==len(input) and len(stack)!=0:		# this if is true when there is'nt left any 1 but we have 0's in stack.
			print ("NOT ACCEPTED!")			# this actually is true when (M!>N+2)
			exit()

	#___END OF WHILE___

	# now we empty stack. but now we can have 1's as much as we want. But just 1 not any 0.
	if len(input) > index:
		while index != len(input):
			if input[index] == '1':
				index = index+1
			else:
				print ("NOT ACCEPTED!")
				exit()

		#__END OF WHILE___

#___END OF ELIF___

# now if your input reachs here then it deserves to be ACCEPTED :)
print ("ACCEPTED!")
