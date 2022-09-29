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
        utils_pathname = self_pathname.parent
        resources_pathname = utils_pathname.parent
        r_pathname = resources_pathname / "resources"
        return r_pathname.resolve()
        