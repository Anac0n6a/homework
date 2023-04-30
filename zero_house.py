#86779227
def house_calc(street_distance: int, street: int):
    distance = []
    zero = None
    for iteration, element in enumerate(street):
        if element == 0:
            zero = iteration
            distance.append(0)
            continue
        if (element != 0 and zero != None):
            distance.append(iteration - zero)
        else:
            distance.append(street_distance)
    zero = None
    for iteration, element in reversed(list(enumerate(street))):
        if element == 0:
            zero = iteration
            continue
        if (element != 0 and zero != None and distance[iteration] > zero - iteration):
            distance[iteration] = (zero - iteration)
    return distance

if __name__ == '__main__':
    street_distance = int(input())
    street = [int(num) for num in input().split(' ')]
    print(*house_calc(street_distance, street))
