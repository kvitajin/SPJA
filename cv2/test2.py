# DEFINE THE FUNCTIONS ACCORDING TO THE ASSIGMENT
def filter_numbers(list):
    tmp=[i for i in list if (type(i) == float) or (type(i) == int)]
    return sorted(tmp)


def average_length(list):
    sum = 0
    num = 0
    for i in list:
        sum += len(i)
        num += 1
    return sum / num


def overlapping(fuck, name):
    for i in fuck:
        for j in name:
            if i == j:
                return True
            continue
    return False


def number_of_letters(str):
    tmp = {}
    for i in str:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    return tmp


def f(x):
    return (x ** 2 - 2 * x)


# def minmax(f, a, b):
#     wtf = (min, max)
#     tmp = a
#     vys = f(tmp)
#     wtf[min] = vys
#     wtf[max] = vys
#     while (1):
#         vys = f(tmp)
#         if vys < min:
#             wtf[min] = vys
#         elif vys > max:
#             wtf[max] = vys
#         else:
#             continue
#         if tmp>b:
#             tmp+=1
#         else: break
#     return wtf

def minmax(f, a, b):
    tmp = a
    vys = f(tmp)
    min =max = vys
    while (1):
        vys = f(tmp)
        if vys < min:
            min = vys
        elif vys > max:
            max = vys


        if tmp<b:
            tmp+=1
        else:
            break
    return (min, max)


# UNCOMMENT THE FOLLOWING FUNCTION CALLS
print(filter_numbers([1.2, "sdas", 4, [12], 3.4, "12", -3, True, 5, 8.1]))
print(average_length(["plzen", "liberec", "ostrava", "praha", "brno"]))
print(overlapping([1, 2, 3], [4, 5, 6]))
print(overlapping([1, 2, 3], [3, 4, 5]))
print(number_of_letters("ababdacabbdabc"))
print(minmax(f, -5, 5))
