import os
import sys

def main():
    print sys.version
    dirtest()
    
    fib(100000)


def dirtest():
    """ Do some Directory Testing """

    # test system directory calls
    print "Current Directory:"
    print os.listdir(os.getcwd())

    print "Parent Directory:"
    print "Is '.ssh' in home?", '.ssh' in os.listdir(os.pardir)

    # print current directory
    print os.getcwd()

    print os.path.ismount('/home')

def usage():
    # test print 
    print """
    Usage: thingy [options]
	    -h
	    -H hostname
    """

def fib(n):
    a, b = 0,1
    while a < n:
        print a,
        a, b = b, a+b


# start the ball rolling.
if __name__ == "__main__":
    main()
