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
        raise Exception(c)
