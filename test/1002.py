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

# 인덱스 연산
idx1 = pd.Index([1,2,3])
idx2 = pd.Index([2,3,4])

# union : 중복값은 제거 
print(idx1.union(idx2))

# intersection : 교집합
print(idx1.intersection(idx2))

