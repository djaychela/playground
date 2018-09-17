def pressureGauges(morning, evening):
    return [list(map(min, zip(morning, evening))), list(map(max, zip(morning, evening)))]


print(pressureGauges(morning=[3, 5, 2, 6], evening=[1, 6, 6, 6]))
