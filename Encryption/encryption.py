import base64

coded_string = '''DUYBHA0NBBoBUUFISUkJEwwTAkZeSUkNDgUeEwAVHAtJQVNSUQQBHQsLDAwWUU1STgsIBwYAAhJV
SVRORgAcFRMXDQcMDQxVWkFVCA0GCAwEEwwXBxpJQVNSURQcBQENCgwWUU1SThwPAwsbAhJVSVRO
RhoTEARVRU5JBwYdUUFISUkZCAdTURw='''

KEY = 'varinnair'
decoded = base64.b64decode(coded_string)

result = []
i = 0
for c in decoded:
    result.append(chr(ord(chr(c)) ^ ord(KEY[i % len(KEY)])))
    i += 1

print(''.join(result))

# output
# {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}