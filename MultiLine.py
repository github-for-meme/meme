s = "https://www.multisoft.se/"
a = "1112031584"
a_l = [int(i) for i in a]
for i in range(1, len(a_l)):
    if a_l[i] % 2 == a_l[i - 1] % 2:
        i_max = max(a_l[i], a_l[i-1])
        s += str(i_max)
s += "/"
print(s)
