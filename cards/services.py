from random import choice
from typing import List


class Learning:
    def __init__(self, quantity: int, all_ids: List):
        self.case_one, self.case_two, self.case_three = [], [], []
        self.temp_lst = []
        self.all_ids = all_ids
        self.quantity = quantity

    def gen_list_of_words(self) -> List:
        while len(self.temp_lst) < self.quantity:
            id = choice(self.all_ids)
            self.temp_lst.append(id)
            self.temp_lst = list(set(self.temp_lst))
        return self.temp_lst

    def get_random_id(self):
        return choice(self.temp_lst)

    def split_into_groups(self, type_group: List, word_id: int) -> int:
        if type_group == "-1":
            self.case_one.append(word_id)
            return -1
        elif type_group == "1":
            self.case_three.append(word_id)
            return 1
        else:
            self.case_two.append(word_id)
            return 0

    def check_word_in_list(self, word_id: int, lst: List) -> bool:
        return word_id in lst
