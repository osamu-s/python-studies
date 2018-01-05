#!/usr/bin/env python3

import yaml

i_str = """
| hoge | 192.168.0.1:22 |
| hage | 192.168.0.2:8080 |"""

map_port_hd = 6400

# srv = [dict(zip(['addr', 'port', 'r_port'],
#                 ln[1:-1].split('|')[1].strip().split(':') + [i + map_port_hd]))
#        for i, ln in enumerate(i_str.splitlines())
#        if ln.startswith('|') and ln.endswith('|')]

def get_token(lines):
    return  [ [cell.strip() for cell in ln[1:-1].split('|')]
              for ln in lines.splitlines()
              if ln.startswith('|') and ln.endswith('|') ]

def projection(nested_list, idx):
    return [ ln[idx] for ln in nested_list]

srv = [ ln[1:-1].split('|')[1].strip().split(':') 
        for ln in i_str.splitlines()
        if ln.startswith('|') and ln.endswith('|') ]

fwd = [ dict(zip(['addr', 'port', 'r_port'], s+[i + map_port_hd]))
        for i, s in enumerate(srv) ]

for s in fwd:
    s['port'] = int(s['port'])
print(yaml.dump(fwd))
