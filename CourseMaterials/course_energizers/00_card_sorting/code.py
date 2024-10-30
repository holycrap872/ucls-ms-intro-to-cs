import time


class Cards:
    def shuffle(self) -> None:
        pass

    def sort(self) -> None:
        pass


def break_up_into_groups(x):
    pass


def get_cards() -> Cards:
    return Cards()


def hand_left(cards: Cards):
    pass


def celebrate_quietly():
    pass


def receive_right() -> Cards:
    return Cards()


best_so_far = 120
break_up_into_groups(3)
cards = get_cards()

while True:
    cards.shuffle()

    hand_left(cards)
    cards = receive_right()

    start_time = time.time()
    cards.sort()
    end_time = time.time()

    total_time = end_time - start_time
    print(total_time)

    if total_time < best_so_far:
        celebrate_quietly()
        best_so_far = total_time
