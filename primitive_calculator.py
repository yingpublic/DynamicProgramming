# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence_dp(n):
    MinNumSeq = [0] * (n + 1)
    MinNumSeq[1] = 0
    LastLocation = [0] * (n + 1)
    LastLocation[1] = 1
    for i in range(2, n + 1):
        MinNumSeq[i] = i + 10
        NumSeq = MinNumSeq[i - 1] + 1
        if NumSeq < MinNumSeq[i]:
            MinNumSeq[i] = NumSeq
            LastLocation[i] = i - 1
        if i % 3 == 0:
            NumSeq = MinNumSeq[i // 3] + 1
            if NumSeq < MinNumSeq[i]:
                MinNumSeq[i] = NumSeq
                LastLocation[i] = i // 3
        if i % 2 == 0:
            NumSeq = MinNumSeq[i // 2] + 1
            if NumSeq < MinNumSeq[i]:
                MinNumSeq[i] = NumSeq
                LastLocation[i] = i // 2
    return MinNumSeq, LastLocation

def OutputSequence(n):
    MinNumSeq, LastLocation = optimal_sequence_dp(n)
    # print("MinNumSeq: " , MinNumSeq)
    # print("LastLocation: " , LastLocation)
    sequence = [n]
    while n > 1:
        n = LastLocation[n]
        sequence.append(n)
    sequence.reverse()
    return sequence


input = sys.stdin.read()
n = int(input)
# sequence = list(optimal_sequence(n)) # starter code with wrong algorithms
sequence = list(OutputSequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


