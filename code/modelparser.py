#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libsbml import *

class ModelParser:
    def __init__(self,model=None):
        self.model = readSBML(model).getModel()
        self.reactions = self.model.getListOfReactions()
        self.species = self.model.getListOfSpecies()


if __name__ == '__main__':
    import sys
    m = ModelParser(sys.argv[1])
