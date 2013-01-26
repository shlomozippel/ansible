import imp
from os import path
imp.load_source('_ansible',path.join(path.dirname(path.realpath(__file__)),'ansible'))
from _ansible import *
if __name__ == "__main__":
    main()