# 集合運算
# https://tw.saowen.com/a/1d0eaad763f245fba95e7d59a3c7c814ab1e7bc73e7a9d7b5280f81ba38af07c
# http://www.howsoftworks.net/python-tutorial-sets

E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

print(4 in E) # 4 是否存在 E 集合內

print("E 和 N 的聯集=",E | N) # 印出 E 和 N 集合內的元素，若多筆重覆，只會顯示一筆，其餘筆將會過濾掉不顯示。

print("E 和 N 的交集=",E & N) # 印出 E 和 N 集合內同時存在的相同元素

print("E 和 N 的差集=",E - N) # 印出 E，不包含在 N 的元素。

print("E 和 N 的差分集=",E ^ N) # 印出 E 和 N 集合元素，但不印出的相同的元素


