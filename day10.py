import json
total = 0
큰지역 = []

with open("budget.csv", "r", encoding="utf-8") as f:
    for 줄 in f:
        칸 = 줄.strip().split(",")
        if 칸[0] == "지역":
            continue
        예산 = int(칸[1])
        total = total + 예산
        if 예산 > 1000:
            큰지역.append(칸[0])

print(f"총예산: {total}")
print(f"1000 이상 지역: {큰지역}")

결과 = {"총예산": total, "큰지역": 큰지역}
with open("분석결과.json", "w", encoding="utf-8") as f:
    json.dump(결과, f, ensure_ascii=False, indent=2)