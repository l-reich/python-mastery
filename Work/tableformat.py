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


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def create_formatter(
    format: str, column_formats: list = None, upper_headers=False
) -> TableFormatter:
    match format:
        case "text":
            format_class = TextTableFormatter
        case "csv":
            format_class = CSVTableFormatter
        case "html":
            format_class = HTMLTableFormatter

    if column_formats:
        if upper_headers:

            class ReturnClass(UpperHeadersMixin, ColumnFormatMixin, format_class):
                formats = column_formats
        else:

            class ReturnClass(ColumnFormatMixin, format_class):
                formats = column_formats
    else:
        if upper_headers:

            class ReturnClass(UpperHeadersMixin, format_class):
                pass
        else:

            class ReturnClass(format_class):
                pass

    return ReturnClass()


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
