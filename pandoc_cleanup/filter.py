import panflute


def action(elem, doc):
    if isinstance(elem, panflute.Strong):
        return list(elem.content)


def main(doc=None):
    return panflute.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
