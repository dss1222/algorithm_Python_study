def solution(participant, completion):
    Dict = {}
    sumHash = 0

    # Dict : Participant의 딕셔너리 만들기
    # participant의 sum(hash) 구하기

    for i in participant:
        Dict[hash(i)] = i
        print(Dict[hash(i)])
        sumHash += hash(i)
        print(hash(i))
    # completion의 sum(hash) 빼기
    for j in completion:
        sumHash -= hash(j)
        print(Dict[hash(j)])
        print(hash(j))
    return sumHash

participant = ["mislav", "stanko", "mislav", "ana"]
completion	= ["stanko", "ana", "mislav"]

print(solution(participant, completion))