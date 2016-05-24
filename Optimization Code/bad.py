# Purposefully bad!!! Fix me!!!
fi = open('artistdata.csv')
txt = fi.read()
lines = txt.split('\n')
lines = lines[1:] # ignore the header

artists = {}

for line in lines:
    if not line: continue
    sp = line.split(',')
    artist = sp[0]
    rest = sp[1:]
    vector = []
    for i in rest:
        vector.append(float(i))
    artists[artist] = vector

reference = 'Pink Floyd' # compare artists to pink floyd
refvector = artists[reference]

similarities = []

for artist in artists:
    vector = artists[artist]
    if artist != reference:
        # Let's calculate the similarity
        numerator = 0
        for i in range(len(vector)):
            numerator = numerator + vector[i]*refvector[i]
        # Find the norms
        norm1 = 0
        for v in vector:
            norm1 = norm1 + v*v
        import math
        norm1 = math.sqrt(norm1)
        norm2 = 0
        for v in refvector:
            norm2 = norm2 + v*v
        norm2 = math.sqrt(norm2)
        sim = numerator/(norm1*norm2)
        #print artist, sim
        similarities.append((artist,sim))

# Don't worry about this, it just sorts the list and prints the first 10
print '\n'.join('%d%% - %s'%(a*100, b) for (b,a) in sorted(similarities,key=lambda x:x[1],reverse=True)[:10])

