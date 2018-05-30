#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libsbml import *

class ModelParser:
    def __init__(self,model=None):
        self.model = readSBMLFromFile(model).getModel()
        self.model_id = self.model.getId()
        self.reactions = self.model.getListOfReactions()
        self.species = self.model.getListOfSpecies()


if __name__ == '__main__':
    import sys
    m = ModelParser(sys.argv[1])
