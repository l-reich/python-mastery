def parse_file(filename: str):
    portfolio_dict = {}
    with open(filename, "r") as f:
        for line in f:
            row = line.strip().split()
            portfolio_dict[row[0]] = int(row[1]), float(row[2])

    return portfolio_dict

if __name__ == "__main__":
    d = parse_file("../Data/portfolio.dat")
    print(sum([count * price for count, price in d.values()]))


