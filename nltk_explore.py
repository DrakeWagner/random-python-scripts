import sys
print(sys.path)
import numpy as np
import nltk
# nltk.download()
from nltk import *

raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people hot-tempered,'..."""

print(re.split(r' ',raw))
print(' ')
print(re.split(r'[ \t\n]+', raw))
print(' ')
print(re.split(r'\W+',raw))

'''
(via nltk.org)
Symbol	Function
\b	Word boundary (zero width)
\d	Any decimal digit (equivalent to [0-9])
\D	Any non-digit character (equivalent to [^0-9])
\s	Any whitespace character (equivalent to [ \t\n\r\f\v])
\S	Any non-whitespace character (equivalent to [^ \t\n\r\f\v])
\w	Any alphanumeric character (equivalent to [a-zA-Z0-9_])
\W	Any non-alphanumeric character (equivalent to [^a-zA-Z0-9_])
\t	The tab character
\n	The newline character
'''

text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)     # set flag to allow verbose regexps
  (?:[A-Z]\.)+       # abbreviations, e.g. U.S.A.
| \w+(?:-\w+)*       # words with optional internal hyphens
| \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
| \.\.\.             # ellipsis
| [][.,;"'?():-_`]   # these are separate tokens; includes ], [
    '''
print(nltk.regexp_tokenize(text, pattern))

text = word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

nltk.help.upenn_tagset()    