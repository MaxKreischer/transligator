fileName = '.\example_terminology.txt'
lines = open(fileName, 'r').readlines()

if fileName.endswith('.txt'):
    print("Is text file")
print(lines[0])

idx = lines[0].find("\t")
nativeString = lines[0][0:idx]
targetString = lines[0][idx:].lstrip()
print(idx)
print(nativeString)
print(targetString)