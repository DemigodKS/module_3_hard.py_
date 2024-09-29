# 1-й вариант
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                      ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum (data_structure):
    x = 0
    y = 0
    for item in data_structure:
        # if isinstance(data_structure, list):
        if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            for word in item:
                if isinstance(word, int):
                    x += word
                elif isinstance(word, list):
                    for ww in word:
                        if isinstance(ww, set):
                            for j in ww:
                               if isinstance(j, tuple):
                                   for k in j:
                                       if isinstance(k, tuple):
                                           for k_ in k:
                                               if isinstance(k_, int):
                                                    x += k_
                                               elif isinstance(k_, str):
                                                    y += len(k_)
                                       elif isinstance(k, int):
                                           x += k
                                       elif isinstance(k, str):
                                           y += len(k)
                elif isinstance(word, tuple):
                    for i in word:
                        x += i
                elif isinstance(word, dict):
                    for value, key in word.items():
                        x += key
                        y += len(value)
        elif isinstance(item, dict):
            for value, key in item.items():
                x += key
                y += len(value)
        elif isinstance(item, str):
                y += len(item)

    return x + y
res = calculate_structure_sum(data_structure)
print(res)

#2-ой вариант
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    x = 0
    y = 0

    def structure(item):
        nonlocal x, y
        # for item in data:
        if isinstance(item, list) or isinstance(item, set) or isinstance(item, tuple):
            for i in item:
                structure(i)
        elif isinstance(item, dict):
            for value, key in item.items():
                structure(value)
                structure(key)
        elif isinstance(item, int) or isinstance(item, str):
            if isinstance(item, int):
                x += item
            elif isinstance(item, str):
                y += len(item)

    structure(data_structure)
    return x + y


res = calculate_structure_sum(data_structure)
print(res)
