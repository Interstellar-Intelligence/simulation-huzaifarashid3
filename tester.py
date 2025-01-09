from student import oxygen

def test_oxygen():
    test_values = [1,2,3,4]
    score = 0 
    for  i in test_values:
        output = oxygen(i)
        if 5 <= output <= 8:
            score += 2
        elif 0 < output < 5 or 8 < output < 10:
            score += 1
        else:
            score  -=1
    print(score)


def test_happiness():
    happiness = 0
    # happiness += score_oxygen()
    # happiness += score_pollution()


test_oxygen()