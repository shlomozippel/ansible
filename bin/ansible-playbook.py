import imp
from os import path
_ansibleplayook = imp.load_source('_ansibleplaybook',path.join(path.dirname(path.realpath(__file__)),'ansible-playbook'))
from _ansibleplaybook import *
if __name__ == "__main__":
    outer_main()