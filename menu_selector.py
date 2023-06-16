from file_manager import read_file
from parking_spot_manager import *
def start_process(path):
    spots = []
    str_list = read_file(path)
    for i in range(len(str_list)):
        list = str_list_to_class_list(str_list[i])
        spots.append(list)
        # 파일 읽기 및 리스트에 객체 추가
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:                             #리스트 출력
            print_spots(spots)
        elif select == 2:                           #필터 선택 및 적용
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            filtered_spots = []
            select = int(input('type:'))
            # 각 선택에 대한 필터링 적용
            if select == 1:
                keyword = input('type name:')
                filtered_spots = filter_by_name(spots, keyword)
                spots = filtered_spots
            elif select == 2:
                keyword = input('type city:')
                filtered_spots = filter_by_city(spots, keyword)
                spots = filtered_spots
            elif select == 3:
                keyword = input('type district:')
                filtered_spots = filter_by_district(spots, keyword)
                spots = filtered_spots
            elif select == 4:
                keyword = input('type ptype:')
                filtered_spots = filter_by_ptype(spots, keyword)
                spots = filtered_spots
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)        #위치 튜플 생성
                filtered_spots = filter_by_location(spots, locations)
                spots = filtered_spots
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:                               #반복 종료
            print("Exit")
            break
        else:
            print("invalid input")