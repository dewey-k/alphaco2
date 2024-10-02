import pandas as pd
from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005670", "ACTS", 1185]
]

columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
df.set_index("종목코드", inplace=True)
# print(df)

# ascending = True (기본값) : 오름차순
# ascending = False : 내림차순
# print(df.sort_values(by='종목명',ascending=False)) # 내림차순
# print(df.sort_values(by='종목명',ascending=True)) # 오름차순

# print(df.sort_index()) # 기본값
# print(df.sort_index(ascending=False)) # 역순

# 인덱스 연산 : 합집합, 교집합, 차집합의 원리를 사용하여 데이터 병합할 때 사용
idx1 = pd.Index([1,2,3])
idx2 = pd.Index([2,3,4])

# union : 중복값은 제거 
#print(idx1.union(idx2))

# intersection : 교집합
#print(idx1.intersection(idx2))

# difference : 차집합
#print(idx1.difference(idx2))

# GroubBy 연산
from pandas import DataFrame

data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = DataFrame(data=data, columns=columns)
# print(df)

# DataFrameGroubBy 타입으로 변환했다가, DataFrame 타입으로 다시 변환
result = df.groupby('테마')[['PER','PBR']].mean()
# print(result, type(result))

# 내보내기
# result.to_csv("output/theme_stock.csv")
# result.to_excel("output/theme_stock.xlsx")

# print(df.groupby('테마').get_group('2차전지(생산)'))
# print(df.groupby('테마').get_group('시스템반도체'))
# print(df.groupby('테마').get_group('해운'))

# parse_dates는 datetime 형식으로 자동 변환하여 데이터 처리하는 read_#() 메서드의 매개변수
df4 = pd.read_excel("ss_ex_1.xlsx" , parse_dates=['일자'], index_col=0)
print(df4.head())

