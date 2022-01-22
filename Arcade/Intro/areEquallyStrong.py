# Call two arms equally strong if the heaviest weights they each are able to lift are equal.

# Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft < yourRight:
        yourWeak, yourStrong = yourLeft, yourRight
    else:
        yourWeak, yourStrong = yourRight, yourLeft
    if friendsLeft < friendsRight:
        friendsWeak, friendsStrong = friendsLeft, friendsRight
    else: 
        friendsWeak, friendsStrong = friendsRight, friendsLeft
    return yourWeak == friendsWeak and friendsStrong == yourStrong