from vacations_calendar import calendar


def check(date_str):
    D = date_str
    C = calendar

    for k, v in C.items():
        if C[D] == D:
            print("hoora")



check('01/01/22')
