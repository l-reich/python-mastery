import sys


def parse_file(filename: str):
    portfolio_dict = {}
    with open(filename, "r") as f:
        for line in f:
            row = line.strip().split()
            try:
                portfolio_dict[row[0]] = int(row[1]), float(row[2])
            except ValueError as e:
                print("Cound't parse", row, e)

    return portfolio_dict


def portfolio_cost(filename: str) -> float:
    portfolio_dict = parse_file(filename)
    return sum([count * price for count, price in portfolio_dict.values()])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        portfolio_path = sys.argv[1]
    else:
        portfolio_path = "../Data/portfolio.dat"

    print(portfolio_cost(portfolio_path))
