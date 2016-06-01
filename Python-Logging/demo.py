import argparse
parser = argparse.ArgumentParser(description = "Fibonacci Sequence.")
parser.add_argument('-s', action='store_const', const=sum, default=max, help = 'this is a test help')

def main():
    args = parser.parse_args()
    print "test"
if __name__ == '__main__':
    main()