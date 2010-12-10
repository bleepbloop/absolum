import _mysql
import sys

def main():
    db = _mysql.connect(sys.argv[0])



# start the ball rolling.
if __name__ == "__main__":
    main()
