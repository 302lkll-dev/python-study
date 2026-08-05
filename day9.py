total = 0

with open("budget.csv", "r", encoding="utf-8") as f:
    for 줄 in f:
        칸 = 줄.strip().split(",")      # ['포천', '1200']
        if 칸[0] == "지역":   # 제목 줄이면
            continue          # 아래 코드 다 무시하고 다음 for 바퀴로
        예산 = int(칸[1])                # '1200' → 1200 (숫자로!)
        total = total + 예산

print(f"총 예산: {total}")