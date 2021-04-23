""" Tile Cost Calculator"""

def main():
    height = int(input("Height of room in ft: "))
    width = int(input("Width of room in ft: "))
    cost = int(float(input("Cost of til per sq. foot: ")))

    print ("Total cost is " + " $" + str(width * height * cost) + "")

if __name__ == '__main__':
    main()