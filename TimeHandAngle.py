def calc_angle(time):
    big_hand = int(time.partition(':')[0])
    little_hand = int(time.partition(':')[2])
    if big_hand >= 12:
        big_hand -= 12
    big_hand_angle = float((big_hand)*30)
    for i in range(little_hand):
        big_hand_angle += .5
    little_hand_angle = 6 * little_hand
    return 360 - big_hand_angle - little_hand_angle

print(calc_angle('3:10'))
