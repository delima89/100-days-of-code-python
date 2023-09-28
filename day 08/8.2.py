test_h = 0
test_w = 0
coverage =5
def paint_calc(height=test_h, width=test_w, cover=coverage):
    m2=height*width
    m2=m2/cover
    print(f"You'll need {round(m2+0.25)} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
