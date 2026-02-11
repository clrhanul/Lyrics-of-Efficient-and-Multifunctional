with open('./test.txt', 'rb') as f:
    data = f.read()

result = []
buf = 0
for b in data:
    
    print(b)
