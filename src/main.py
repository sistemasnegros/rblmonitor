"""
Autor: Kevin Franco
email: sistemasnegros@gmail.com

this scritp allow monit ip server if are listed in blacklist.
"""

import time
import argparse

from rblwatch import RBLSearch

# ======================================
# args
# ======================================
parser = argparse.ArgumentParser(
    description='Monit ip server if are listed in blacklist. Author Kevin Franco - sistemasnegros@gmail'
)

parser.add_argument("-i", '--ip', nargs="+", help='ip servers separated space 8.8.8.8 1.1.1.1', required=True)
parser.add_argument("-d", '--delay', help='delay default 60', default=60, type=int)
args = parser.parse_args()

list_servers = args.ip
delay = args.delay


while True:
    print "=================================================="
    print "Cancel process Control+C"
    for server in list_servers:
        searcher = RBLSearch(server)
        searcher.print_results()
        print "TIME: ", time.strftime('%d %b %y - %H:%M:%S')
    print "=================================================="

    try:
        time.sleep(delay)
    except KeyboardInterrupt:
        print "Process Cancelated."
        break
