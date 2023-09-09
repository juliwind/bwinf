def main():
    upper = []
    with open("zauberschule0.txt") as f: 
        dim = [int(s) for s in f.readline().split() if s.isdigit()]
        lower = upper = [[[] for _ in range(dim[1])] for _ in range(dim[0])]
        for i in range(dim[0]):
            l = f.readline()
            for j in range(dim[1]):
                c = l[j]
                lower[i][j] = (c)
        f.readline()
        for i in range(dim[0]):
            l = f.readline()
            for j in range(dim[1]):
                c = l[j]
                upper[i][j] = (c)
        print(upper, "              sdijfisjdnfisdujnf              ", lower)
                





if __name__ == "__main__":
    main()