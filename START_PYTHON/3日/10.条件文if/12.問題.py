vote = input("투표를 해주세요(A, B) : ").upper()
voteA = vote.upper().count("A") #함수를 여러번 실행할 수 있다.
voteB = vote.upper().count("B")
print("A : %d, B : %d"%(voteA, voteB))
if voteA > voteB:
    print("A가 이겼습니다.")
elif voteA < voteB:
    print("B가 이겼습니다.")
else:
    print("비겼습니다.")
