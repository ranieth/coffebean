import os, sys

absolute = os.path.abspath(os.path.join(sys.path[0], os.pardir))

cache = absolute + os.sep + "cache"

log = absolute + os.sep + "log"