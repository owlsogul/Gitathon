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

# git 활용도 점수 계산하는 함수
# 각 항목별 비율과
# 전체 팀들의 평균과 표준편차 필요
# 선택된 팀의 각 항목별 값 필요
def gitEval(commitRate,lineRate,branchRate,teamRate, avgTotalData, stdTotalData, teamRawData) :


    # 입력한 수를 기준으로 비율 계산
    # 소수점 둘 째자리로 반올림
    # percentage = [commitRate, lineRate, branchRate, teamRate]
    percentage = []
    percentage = calPercent(commitRate,lineRate,branchRate,teamRate)


    # 전체 평균 대비 한 팀의 commit수, 수정된 줄 수, merge된 branch 수, 팀원 기여도 점수 계산하기
    # 표준화
    teamRawData[0] = (teamRawData[0] - avgTotalData[0]) / stdTotalData[0] # -5 0.81
    teamRawData[1] = (teamRawData[1] - avgTotalData[1]) / stdTotalData[1] # -27.7 0.0
    teamRawData[2] = (teamRawData[2] - avgTotalData[2]) / stdTotalData[2] # 0.18 1.0
    teamRawData[3] = (teamRawData[3] - avgTotalData[3]) / stdTotalData[3] # -1.17 0.95

    # 정규화
    nomalData=[]
    nomalData = nomalization(teamRawData[0],teamRawData[1],teamRawData[2],teamRawData[3])

    # 계산

    gitScore = 0

    for i in range(0,4) :

        gitScore += round(percentage[i] * nomalData[i], 2)

        # 최종 결과값
    gitScore = gitScore * 100

    return gitScore
