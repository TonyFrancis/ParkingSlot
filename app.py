import sys

if __name__ == '__main__':
    bInteractive = bool(len(sys.argv) > 1)
    if bInteractive:
        input_file = open(sys.argv[1],'r')
        getCommand = input_file.readline
    else:
        getCommand = raw_input
    sCommand = getCommand()
    while sCommand:
        print sCommand
        sCommand = getCommand()
