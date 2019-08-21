import salt
import re

RE_NEIGHBORS = 'BGP neighbor is (.+), remote AS (\d+)\n(?: Description: (.+)\n)?.+ router-id (.+)\n  BGP state = (\w+)(?:, (\w+) for (.+))?(?:\n.+\n\n|\n.+\n.+\n.+\n.+\n.+\n\n)  Message statistics:\n.+\n  (Opens)\s+(\d+)\s+(\d+)\n\s+(Notifications)\s+(\d+)\s+(\d+)\n\s+(Updates)\s+(\d+)\s+(\d+)\n\s+(Keepalives)\s+(\d+)\s+(\d+)\n\s+(Route Refresh)\s+(\d+)\s+(\d+)\n.+(Total)\s+(\d+)\s+(\d+)\n\n.+\n.+\n.*(Updates)\s+(\d+)\s+(\d+)\n\s+(Withdraws)\s+(\d+)\s+(\d+)\n\s+(End-of-Rib)\s+(\d+)\s+(\d)\n\n\s+(Local host):\s+(.*),\s(Local port):\s+(\d+)\n\s+(Remote host):\s+(.*),\s(Remote port):\s+(\d+)'

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
