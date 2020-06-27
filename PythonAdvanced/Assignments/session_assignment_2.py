"""
2. Let's imagine a scenario where we have a Server instance running different services such as http and ssh on different ports. Some of these services have an active state while others are inactive.

class Server:

    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]

- Create an iterator for the Server class which would loop over only the active ports
- Create a generator class that does the same thing

"""

from itertools import compress

print("----Iterator------ ")

def server_selection(services):
    server_selectors = []
    for each in services:
        server_selectors.append(each['active'])
    return server_selectors

services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
        {'active': False, 'protocol': 'https', 'port': 443},
    ]

active_servers = compress(services,server_selection(services))
print("Printing All Active Servers")

for server in active_servers:
    print (server)

print("----Generator------ ")

def get_active_server_generator(services):
    active_servers = compress(services, server_selection(services))
    for server in active_servers:
        yield server

active_server_generator = get_active_server_generator(services)
print(active_server_generator.__next__())
#print(active_server_generator.__next__())
