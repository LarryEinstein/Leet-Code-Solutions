def find_glass_portion(poured_quantity: float, glass_row: int, glass_column: int) -> float:
    """
    Champagne tower.
    - poured_quantity: how much liquid you pour into the top (in 'glass units')
    - glass_row: 1-indexed row number (top glass is row 1)
    - glass_column: 1-indexed column within that row (leftmost is 1)

    Returns the portion filled in the target glass, capped to 1.0.
    """
    if glass_row < 1:
        raise ValueError("glass_row must be >= 1")
    if glass_column < 1 or glass_column > glass_row:
        raise ValueError("glass_column must be between 1 and glass_row (1-indexed)")

    # dp[r][c] = amount of liquid that arrives at row r, col c (0-indexed)
    dp = [[0.0] * (glass_row + 1) for _ in range(glass_row + 1)]
    dp[0][0] = float(poured_quantity)

    for r in range(glass_row):
        for c in range(r + 1):
            overflow = max(0.0, dp[r][c] - 1.0)
            if overflow > 0.0:
                dp[r + 1][c] += overflow / 2.0
                dp[r + 1][c + 1] += overflow / 2.0

    amount_in_target = dp[glass_row - 1][glass_column - 1]
    return min(1.0, amount_in_target)


if __name__ == "__main__":
    print(find_glass_portion(234, 13, 4))
    print(find_glass_portion(1, 2, 1))  # 0.0