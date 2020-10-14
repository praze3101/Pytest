def rev_string_function(string: str, filter_list: list = None):
    if filter_list == None:
        return "".join([letter for letter in list(string)])[::-1].capitalize()
    else:
        return "".join([letter for letter in list(string) if letter not in filter_list])[::-1].capitalize()


if __name__ == "__main__":
    print(rev_string_function(string="Abra cadabra"))
