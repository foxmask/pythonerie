#optparse doc : http://docs.python.org/library/optparse.html
from optparse import OptionParser
import os

def main():
    usage = "%prog -e environment name -r release name. \nfor example : \npython make_delivery -e envname -r 20130101"
    parser = OptionParser(usage)
    parser.add_option("-e", "--env", dest="environment",
                      help="the environment name to use to build the delivery", metavar="ENV")
    parser.add_option("-r", "--rel", dest="release",
                      help="the profinance release name of this delivery (used to name the final package like release-RELEASE-yyyymmdd)", metavar="RELEASE")
    parser.add_option("-c", "--conf", dest="configfile",
                    help="the path where the config file is located. This file should contain the name of the environment from which to download the archives. By Default the script will search in ./env_dirs.conf", default="./env_dirs.conf", metavar="CONFIG")
    parser.add_option("-l", "--log", dest="configlogfile",
help="the path where the config file for the loggging is located. By Default the script will search in ~/MakeDelivery/logging.conf", default=os.path.expanduser('~/MakeDelivery/logging.conf'), metavar="LOGGING_CONFIG")
    (options, args) = parser.parse_args()
    if options.environment == None or options.release == None:
        parser.error("options -e and -r are mandatory")
    else:
        print "environment {0} release {1}".format(options.environment,options.release)

if __name__ == '__main__':
    main()