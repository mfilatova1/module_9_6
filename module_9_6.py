def all_variants(text):
    for i in range(1, len(text)+1):
        for k in range(len(text)):
            if k + i > len(text):
                continue
            yield text[k:k+i]


a = all_variants("abc")
for i in a:
    print(i)







