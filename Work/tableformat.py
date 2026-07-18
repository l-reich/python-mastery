def print_table(obj_list: list[object], attr_names: list[str]) -> None:
    longest_name_len = max(len(a_name) for a_name in attr_names) + 4
    dashes = ["-" * longest_name_len for i in range(len(attr_names))]
    long_in_str = str(longest_name_len)
    formatting_str = (("%" + long_in_str + "s ") * len(attr_names))[:-1]

    print(formatting_str % tuple(attr_names))
    print(*dashes)

    for o in obj_list:
        values = tuple(getattr(o, attr) for attr in attr_names)
        print(formatting_str % values)


if __name__ == "__main__":
    import stock

    portfolio = stock.read_portfolio("../Data/portfolio.csv")
    print_table(portfolio, ["name", "shares", "price"])
    print_table(portfolio, ["name", "shares"])
