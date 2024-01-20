#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hidden = dir(hidden_4)
    fine = [name for name in hidden if not name.startswith('__')]

    sort_name = sorted(fine)

    for name in sort_name:
        print(name)
