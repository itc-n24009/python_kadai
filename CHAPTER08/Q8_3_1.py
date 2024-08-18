import collections
data = "すもももももももものうち"
count = collections.Counter(data)
data_dict = collections.defaultdict(list)
for x, y in count.items():
    data_dict[y].append(x)
print(data_dict[1])
