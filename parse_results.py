from counter import Counter

tally = Counter()
with open('differences') as f:
    for line in f.readlines():
        if 'hash' in line and 'iptcdata' not in line:
            lib, _, _hash = line.split()
            tally[_hash] += 1
            tally[lib] += 1
        
print tally['pyexiv2'] 
pyexiv_and_pil_diffs = [x for x in tally if tally[x] == 1]
print len(pyexiv_and_pil_diffs)
print len(pyexiv_and_pil_diffs) / float(tally['pyexiv2'])
#print pyexiv_and_pil_diffs
