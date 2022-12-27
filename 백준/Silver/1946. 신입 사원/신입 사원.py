import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):

    N = int(input())

    applicant_list = []
    for _ in range(N):
        document, interview = map(int,input().split())
        applicant_list.append((document, interview))
    applicant_list.sort()

    best_score = 1000000
    count = 0
    for idx, each in enumerate(applicant_list):
        if best_score > each[1]:
            count += 1
            best_score = each[1]

    print(count)