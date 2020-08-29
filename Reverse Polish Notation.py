NY_line = []

NY_line[:0] = input()

NY_line.append("~")

NY_line.insert(0, "~")

TX_line = []

CA_line = []


def main_func(NY_line, TX_line, CA_line):
    for car in NY_line:

        if car == "~":
            if len(CA_line) > 0:
                final_round(car, TX_line, NY_line, CA_line)
                return ("".join(CA_line))

            else:
                TX_line.append(car)
                continue

        if chr(ord("A")) <= car <= chr(ord("Z")):
            CA_line.append(car)
            continue

        if car == "+" or car == "-":
            plus_and_minus(car, TX_line, NY_line, CA_line)
            continue

        if car == "*" or car == "/":
            multi_and_divide(car, TX_line, NY_line, CA_line)
            continue

        if car == ")":
            closed_parenthasis(car, TX_line, NY_line, CA_line)
            continue

        if car == "(":
            TX_line.append(car)
            continue


def plus_and_minus(car, TX_line, NY_line, CA_line):
    previous_car = TX_line[len(TX_line) - 1]

    if previous_car == "~" or previous_car == "(":
        # rule 1
        TX_line.append(car)
        return

    if previous_car == "+" or previous_car == "-" or previous_car == "*" or previous_car == "/":
        # rule 2
        CA_line.append(previous_car)
        TX_line.pop()
        plus_and_minus(car, TX_line, NY_line, CA_line)
        return


def multi_and_divide(car, TX_line, NY_line, CA_line):
    previous_car = TX_line[len(TX_line) - 1]

    if previous_car == "~" or previous_car == "+" or previous_car == "-" or previous_car == "(":
        # rule 1
        TX_line.append(car)
        return

    if previous_car == "*" or previous_car == "/":
        # rule 2
        CA_line.append(previous_car)
        TX_line.pop()
        plus_and_minus(car, TX_line, NY_line, CA_line)
        return


def closed_parenthasis(car, TX_line, NY_line, CA_line):
    previous_car = TX_line[len(TX_line) - 1]

    if previous_car == "~":
        return "There has been an error"

    if previous_car == "+" or previous_car == "-" or previous_car == "*" or previous_car == "/":
        CA_line.append(previous_car)
        TX_line.pop()
        closed_parenthasis(car, TX_line, NY_line, CA_line)
        return

    if previous_car == "(":
        TX_line.pop()
        return


def final_round(car, TX_line, NY_line, CA_line):
    previous_car = TX_line[len(TX_line) - 1]

    if previous_car == "~":
        # rule 1
        return CA_line

    if previous_car == "+" or previous_car == "-" or previous_car == "*" or previous_car == "/":
        # rule 2
        CA_line.append(previous_car)
        TX_line.pop()
        final_round(car, TX_line, NY_line, CA_line)
        return CA_line

    if previous_car == "(":
        # rule 1
        TX_line.append(car)
        return "There has been an error"


print(main_func(NY_line, TX_line, CA_line))