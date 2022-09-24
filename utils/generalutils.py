'''
Created on 24-Sep-2022

@author: dheer
'''

from pathlib import Path


class GeneralUtils:
    
    
    def __init__(self):
        pass
    
    
    def get_resource_path(self):
        self_pathname = Path(__file__)
        print("self pathname is : {}".format(self_pathname))
        utils_pathname = self_pathname.parent
        resources_pathname = utils_pathname.parent
        r_pathname = resources_pathname / "resources"
        print("R pathname has : {}".format(r_pathname))
        return r_pathname.resolve()
        