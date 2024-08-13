n = "out_test.txt"
s = "Hello out_test.txt"

with open(n, "w") as f:
    f.write(s)
with open(n, "r") as f:
    for line in f:
        print(line, end="")
