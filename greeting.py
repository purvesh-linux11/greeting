#!/usr/bin/env python3

import sys
def main():
	#print("snapcraft is working. . . . . . . . . . . . .let's start the FUNNNN..!!!",'\n')
	try:
		args = sys.argv[1]
		print("greeting my friend, ",args)
	except:
		print("atleast one argument is needed here.")

if __name__ == '__main__':
    main()
