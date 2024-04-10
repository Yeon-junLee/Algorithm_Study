import sys

N, K = map(int, sys.stdin.readline().split())
elec = list(map(int, sys.stdin.readline().split()))
next_idx = {i : -1 for i in range(1, K + 1)}
using = []
answer = 0
for i in range(K):
    if len(using) < N:          # 플러그에 여유 공간이 있는 경우
        if elec[i] in using:
            try:
                next_idx[elec[i]] = elec.index(elec[i], i + 1, K)
            except:
                next_idx[elec[i]] = -1
            continue
        else:
            try:
                next_idx[elec[i]] = elec.index(elec[i], i + 1, K)
            except:
                next_idx[elec[i]] = -1
            using.append(elec[i])

    else:                       # 플러그에 여유 공간이 없는 경우
        if elec[i] in using:
            try:
                next_idx[elec[i]] = elec.index(elec[i], i + 1, K)
            except:
                next_idx[elec[i]] = -1
            continue
        else:
            maxloc = using[0]
            maxidx = next_idx[using[0]]
            for u in using:
                if next_idx[u] == -1:
                    maxloc = u
                    maxidx = next_idx[u]
                    break
                elif maxidx < next_idx[u]:
                    maxloc = u
                    maxidx = next_idx[u]
            answer += 1
            using.remove(maxloc)
            try:
                next_idx[elec[i]] = elec.index(elec[i], i + 1, K)
            except:
                next_idx[elec[i]] = -1
            using.append(elec[i])
print(answer)