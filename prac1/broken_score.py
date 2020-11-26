def main():
    """
    CP1404/CP5632 - Practical
    Broken program to determine score status
    """
    # TODO: Fix this!
    score = float(input("Enter score: "))
    while score<0 or score>100:
    #if score < 0:, use while to form a loop.
        print("Invalid score")
        score = float(input("Enter score: "))
        if 90>score >=50 :
            #change if to elif
            print("Passable")
        elif score>=90:
        #if score > 90:
            print("Excellent")
    #if score < 50:
        else:
            print("Bad")
main()