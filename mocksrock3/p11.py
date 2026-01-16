def f(car, order):
    if order == 1:
        return sorted(car, key=lambda d: list(d.keys())[0])

    if order == 2:
        return sorted(car, key=lambda d: list(d.values())[0], reverse=True) 
cars = [{"KR333":138},{"WL555":497},{"DB444":341},{"MC222":412}]

print(f(cars, 1))
print(f(cars, 2))
        



