def 짝수찾기(리스트):
    box=[]
    for n in 리스트:
        if n%2==0:
            box.append(n)
    return box
nums = [1, 2, 3, 4, 5, 6]
print(짝수찾기(nums))

def 짝수찾기(리스트):
    box = []                  # 빈 리스트 준비
    for n in 리스트:
        if n % 2 == 0:        # 짝수면
            box.append(n)     # box에 담기
    return box                # for 밖에서 box 돌려주기

nums = [1, 2, 3, 4, 5, 6]
print(짝수찾기(nums))