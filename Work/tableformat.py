from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join("%10s" % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(h for h in headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr> " + (" ".join("<th>" + h + "<\\th>" for h in headers)) + " <\\tr>")

    def row(self, rowdata):
        print(
            "<tr> "
            + (" ".join("<th>" + str(d) + "<\\td>" for d in rowdata))
            + " <\\tr>"
        )


def create_formatter(format: str) -> TableFormatter:
    match format:
        case "text":
            return TextTableFormatter()
        case "csv":
            return CSVTableFormatter()
        case "html":
            return HTMLTableFormatter()


def print_table(
    obj_list: list[object], attr_names: list[str], formatter: TableFormatter
) -> None:
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(attr_names)
    for record in obj_list:
        rowdata = [getattr(record, fieldname) for fieldname in attr_names]
        formatter.row(rowdata)


if __name__ == "__main__":
    import stock

    portfolio = stock.read_portfolio("../Data/portfolio.csv")
    print_table(portfolio, ["name", "shares", "price"])
    print_table(portfolio, ["name", "shares"])
