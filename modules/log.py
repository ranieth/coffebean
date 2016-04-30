'''
Created on Apr 30, 2016

@author: ranieth
'''

from system import path

def call_decorate(function):
    
    def inside(*args, **kwargs):
        print("Entering")
        print(args)
        function(*args, **kwargs)
        print("Exiting")
        
    return inside
        
@call_decorate
def function(first, second):
    print("Inside")
    
function("first", "second")