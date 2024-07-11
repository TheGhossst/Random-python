def append(S, W):
    append_str = W
    S += append_str
    return S
    
def delete(S, k):
    return S[:-k]
    
def prints(S, k):
    print(S[k - 1])

def process_operations(Q, ops):
    S = ""
    history = []

    for op in ops:
        parts = op.split()
        command = int(parts[0])

        if command == 1:
            history.append(S)
            S = append(S, parts[1])
        elif command == 2:
            history.append(S)
            S = delete(S, int(parts[1]))
        elif command == 3:
            prints(S, int(parts[1]))
        elif command == 4:
            S = history.pop()

if __name__ == "__main__":
    Q = int(input())
    ops = []
    for _ in range(Q):
        ops.append(input())

    process_operations(Q, ops)
