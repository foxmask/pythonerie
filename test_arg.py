from sys import argv

def main():

    usage = "To run the script enter -e environment name -r release name. \
            \nfor example : \npython make_delivery -e foxenv -r v1.0-FINAL \
            \n\nYou can optionally use the switches : \
            \n -c /path/to/configfile to use an alternative configfile \
            \n -l /path/to/logging/config/file to use an alternative configfile\
for logging"
    env = ''
    release = ''

    if len(argv) < 2:
        print usage
        exit (0)

    
    if len(argv) < 5 and len(argv) > 2:
        print "the environment name ( specified with -e ) and release name\
( specified with -r ) are mandatory "
        exit (0)

    switch = argv[1]
    switch2 = argv[3]

    if switch == '-e' and switch2 == '-r':
        env = argv[2]
        release = argv[4]
    elif switch == '-r' and switch2 == '-e': 
        env = argv[4]
        release = argv[2]
    else:
        print "the environment name ( specified with -e ) and release name\
( specified with -r ) are mandatory "
        
    print "environment {0} release {1}".format(env,release)


if __name__ == '__main__':
    main()
