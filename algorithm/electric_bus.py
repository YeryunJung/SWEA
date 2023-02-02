T = int(input())
for test_case in range(1, T + 1):
    max_move, end, battery = map(int, input().split())
    station_list = list(map(int, input().split()))

    bus = count = 0
    while bus < end - max_move:
        bus += max_move
        if bus not in station_list:
            station = list(filter(lambda x: x < bus, station_list))
            if len(station) == 0 or station[-1] <= bus - max_move:
                count = 0
                break
            bus = station[-1]
        count += 1
    print(f'#{test_case} {count}')
