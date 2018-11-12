def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


def calPercent(c,l,b,t):

    result = []

    try:
        # 실수형으로 바꾸기
        c = float(c)
        l = float(l)
        b = float(b)
        t = float(t)

        total = c+l+b+t

        # 비율 계산 (7/4 = 1.75) 후 소수점 두째 자리에서 반올림
        c = round(c/total, 2)
        l = round(l/total, 2)
        b = round(b/total, 2)
        t = round(t/total, 2)

        # list로 반환
        result.append(c)
        result.append(l)
        result.append(b)
        result.append(t)

        return result


    except:
        raise Exception("비율 계산 중 오류가 발생하였습니다.")


# git활용도 평가 시
# 서로 다른 값의 범주 즉, commit 수, 수정된 줄 수 등의 표준화 한 값들을
# 0 ~ 1 사이로 정규화하는 함수

def nomalization(c,l,b,t):

    try:

        temp = []
        maxVal=""
        minVal=""
        temp.append(float(c))
        temp.append(float(l))
        temp.append(float(b))
        temp.append(float(t))

        # 4개의 Rate 중 max 값
        maxVal = max(temp)
        # 4개의 Rate 중 min 값
        minVal = min(temp)

        for i in range(0,4) :

            temp[i] = (temp[i]-minVal) / (maxVal - minVal)
            # 소수점 두째 자리에서 반올림
            temp[i] = round(temp[i], 2)

        return temp

    except:
        raise Exception("정규화 중 오류가 발생하였습니다.")
