# Case insensitive text matching

import re

heroRegex = re.compile(r'batman|superman|spiderman|iron man', re.I)

heroes = heroRegex.findall('Batman, two identical Supermans, George and Iron Man were sitting in a pub.')

print(heroes)
