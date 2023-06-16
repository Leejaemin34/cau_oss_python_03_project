class parking_spot:
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {"name":"value1", "city":"value2", "district":"value3", "ptype":"value4", "longitude":"value5", "latitude":"value6"}
        self.__item["name"] = name
        self.__item["city"] = city
        self.__item["district"] = district
        self.__item["ptype"] = ptype
        self.__item["longitude"] = longitude
        self.__item["latitude"] = latitude
        # 생성자를 이용한 객체변수 생성(dictionary) 및 초기화
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
        # 딕셔너리 값을 일련의 str로 반환
    def get(self, keyword = 'name'):
        keyword = self.__item[keyword]
        return keyword
        # 객체변수 딕셔너리 값 반환
    
def str_list_to_class_list(string):
    spot_info = string.split(",")
    out = parking_spot(spot_info[1], spot_info[2], spot_info[3], spot_info[4], spot_info[5], spot_info[6])
    return out
# 입력된 스트링을 통해 객체 생성 및 리턴

def filter_by_name(spots, name):
    out = [spots[i] for i in range(len(spots)) if name in parking_spot.get(spots[i])]
    return out
# 자원명 필터링
def filter_by_city(spots, city):
    out = [spots[i] for i in range(len(spots)) if city in parking_spot.get(spots[i], "city")]
    return out
# 시도 필터링
def filter_by_district(spots, district):
    out = [spots[i] for i in range(len(spots)) if district in parking_spot.get(spots[i], "district")]
    return out
# 시군구 필터링
def filter_by_ptype(spots, ptype):
    out = [spots[i] for i in range(len(spots)) if ptype in parking_spot.get(spots[i], "ptype")]
    return out
# 주차장유형 필터링
def filter_by_location(spots, location):
    out = [spots[i] for i in range(len(spots)) if location[0] < float(parking_spot.get(spots[i], "latitude")) < location[1] and location[2] < float(parking_spot.get(spots[i], "longitude")) < location[3] ]
    return out
#위치 필터링

def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for i in range(len(spots)):
        print(f"{parking_spot.__str__(spots[i])}")
# 객체들을 출력

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)