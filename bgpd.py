import salt
import re

RE_NEIGHBORS = 'BGP neighbor is (.+), remote AS (\d+)\n Description: (.+)\n.+ router-id (.+)\n  BGP state = (\w+), (\w+) for (.+)\n.+\n.*\n.*\n.*\n.*\n\n.*Message statistics:\n.*\n  (\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\w+)\s+(\w+)\n\s+(\w+\s\w+)\s+(\w+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\n.*\n.*\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+)\s+(\d+)\s+(\d+)\n\s+(\w+-\w+-\w+)\s+(\d+)\s+(\d+)\n\n\s+(\w+ \w+):\s+(.+), (\w+ \w+):\s+(\d+)\n\s+(\w+ \w+):\s+(.+), (\w+ \w+):\s+(\d+)\n'
