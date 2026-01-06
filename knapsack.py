# ============================================
# 0/1 Knapsack Problem
# Metode : Dynamic Programming
# Studi Kasus : Toko Online Aksesoris Gadget
# ============================================

def knapsack(capacity, weights, profits, n):
    # Tabel DP
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Proses pengisian tabel DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Menentukan item yang dipilih
    selected_items = []
    total_weight = 0
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            total_weight += weights[i - 1]
            w -= weights[i - 1]

    return dp[n][capacity], selected_items, total_weight


# ==========================
# DATA ITEM
# ==========================
items = [
    "Power Bank",
    "Headset Bluetooth",
    "Charger Fast",
    "Kabel Data",
    "Mouse Wireless",
    "Keyboard Mini",
    "Stand HP",
    "Flashdisk",
    "Speaker Mini",
    "Webcam"
]

weights = [6, 4, 5, 3, 4, 7, 2, 1, 6, 8]
profits = [60, 40, 45, 30, 35, 55, 20, 15, 50, 65]

capacity = 35
n = len(items)

# ==========================
# EKSEKUSI PROGRAM
# ==========================
max_profit, chosen_items, total_weight = knapsack(
    capacity, weights, profits, n
)

# ==========================
# OUTPUT (WAJIB SCREENSHOT)
# ==========================
print("===== HASIL KNAPSACK 0/1 =====")
print("Kapasitas Maksimum :", capacity, "kg")
print("Nilai Maksimum     :", max_profit)
print("Total Berat        :", total_weight, "kg")
print("\nItem Terpilih:")

for i in reversed(chosen_items):
    print(
        f"- {items[i-1]} | Berat: {weights[i-1]} kg | Profit: {profits[i-1]}"
    )
