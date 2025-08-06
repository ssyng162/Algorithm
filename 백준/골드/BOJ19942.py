### 백준 19942: 다이어트

def dfs(idx, p, f, s, v, c, selected_ingredients):
    global min_cost
    global result_ingredients

    if c > min_cost:
        return

    if idx == N:
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if c < min_cost:
                min_cost = c
                result_ingredients = selected_ingredients.copy()
            elif c == min_cost:
                if result_ingredients is None:
                    result_ingredients = selected_ingredients.copy()
                elif selected_ingredients < result_ingredients:
                    result_ingredients = selected_ingredients.copy()
        return

    dfs(
        idx+1,
        p + ingredients[idx][0],
        f + ingredients[idx][1],
        s + ingredients[idx][2],
        v + ingredients[idx][3],
        c + ingredients[idx][4],
        selected_ingredients + [idx + 1]
    )

    dfs(idx+1, p, f, s, v, c, selected_ingredients)

N = int(input())
mp, mf, ms, mv = map(int, input().split())

ingredients = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')
result_ingredients = None

dfs(0, 0, 0, 0, 0, 0, [])

if result_ingredients is None:
    print(-1)
else:
    print(min_cost)
    print(*result_ingredients)