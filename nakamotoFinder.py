# Finds everyone whose name is Nakamoto and prints their first and last name.
# Ignores non-name words.

import re 

nakamotoFinder = re.compile(r'[A-Z]{1}[a-z]+\sNakamoto')

print(nakamotoFinder.findall('''As it was the birthday of the Nakamoto family
patriarch, most of the party were members of the Nakamoto family,
including Alice Nakamoto, Satoshi Nakamoto, Hiro Nakamoto, and the man himself,
Batman Nakamoto.'''))

