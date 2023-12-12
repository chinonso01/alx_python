from sys import argv

def print_argument(argv):
    num_args = len(argv)
    if  num_args == 0:
        print("{} arguments".format(num_args))
    elif num_args == 1:
        print("{} argument:\n".format(num_args))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:\n".format(num_args))
        i = 1
        while i < num_args:
            print("{}: {}".format(i, argv[i]))
            i = i + 1

if __name__ == "__main__":
    argument = argv[0:]
    print_argument(argument)