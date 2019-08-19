import salt
import re

RE_NEIGHBORS = 'BGP neighbor is (.+), remote AS (\d+)\n Description: (.+)\n.+ router-id (.+)\n  BGP state = (\w+), (\w+) for (.+)\n.+\n.*\n.*\n.*\n.*\n\n.*Message statistics:\n.*\n  (\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\w+)\s+(\w+)\n\s+(\w+\s\w+)\s+(\w+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\n.*\n.*\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+-\w+-\w+)\s+(\d+)\s+(\d+)\n\n\s+(\w+ \w+):\s+(.+), (\w+ \w+):\s+(\d+)\n\s+(\w+ \w+):\s+(.+), (\w+ \w+):\s+(\d+)\n'

def show():
    return __salt__['cmd.run']('bgpctl show') 

def config_raw():
    return __salt__['cmd.run']('cat /etc/bgpd.conf')
  
def neighbors():
    raw_data = __salt__['cmd.run']('bgpctl show neighbor')
    x = re.findall(RE_NEIGHBORS, raw_data)
    neighbors_dict = {}
    for neighbor in x:
        neighbors_dict[neighbor[0]] = {
            "description": neighbor[2],
            "import_policy": "",
            "export_policy": "",
            "local_address": "",
            "local_as": 1111,
            "remote_as": neighbor[1],
            "authentication_key": "1234",
            "prefix_limit": {},
            "route_reflector_client": False,
            "nhs": False
        }
    return neighbors_dict
