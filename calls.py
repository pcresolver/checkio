__author__ = 'Steve'
def total_cost(calls):
    print(calls)
    cost = 0
    for day in range(len(calls)):
        first_colon = calls[day].find(":")
        duration_seconds = int(calls[day][first_colon+6:])
        duration_minutes = round((duration_seconds/60)+0.5, 0) # add 0.5 to ensure we round up
        print("duration for day ", day + 1, "is ", duration_minutes)
        cost += daily_cost(duration_minutes)
        print("Cost after day ", day + 1, " is ", cost)
    return cost

def daily_cost(duration):
    if duration <= 100:
        return duration
    else:
        return 100 + ((duration - 100) * 2)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"