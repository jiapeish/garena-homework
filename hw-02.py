
def combine(N, M):
    res = []

    def backtrack(step, path):
        if len(path) == M:
            res.append(path.copy())
            return

        if step == N:
            return

        backtrack(step+1, path)

        path.append(step)
        backtrack(step+1, path)
        path.pop()

    backtrack(0, [])
    return sorted(res)

def main():
    res = combine(4, 2)
    print(res)

if __name__ == "__main__":
    main()