import random


def generate_lotto_numbers():
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    return lotto_numbers

recommended_numbers = generate_lotto_numbers()
print("로또 추천 번호:", recommended_numbers)



def count_common_elements(list1, list2):
    commen_elements = set(list1) & set(list2)
    return len(commen_elements)

list1 = [4]
list2 = [4]

common_count = count_common_elements(list1, list2)
print("같은 요소의 개수: ", common_count)