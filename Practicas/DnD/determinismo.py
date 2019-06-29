import random 

def main():
    base = []
    x = 0
    y = 0
    bajo = 0
    bajo_count = 0
    alto  = 0
    alto_count = 0
    while x < 1000000:
        base.append(random.randint(1, 100))
        x = x + 1
        

    x = 1
    while x < 101:
        y = base.count(x)
        #print(f"\nnum '{x}': {y} veces")
        if x == 1:
            bajo = x
            bajo_count = y
            alto = x
            alto_count = y

        if y < bajo_count:
            bajo_count = y
            bajo = x

        if y > alto_count:
            alto_count = y
            alto = x
        x = x + 1
        
    print(f"El mas alto fue: {alto} con {alto_count}")
    print(f"El mas bajo fue: {bajo} con {bajo_count}")

for i in range(20):
    main()
