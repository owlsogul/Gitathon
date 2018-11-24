
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

        # 비율 계산 (7/4 = 1.75)
        c = round(c/total,2)
        l = round(l/total,2)
        b = round(b/total,2)
        t = round(t/total,2)

        # list로 반환
        result.append(c)
        result.append(l)
        result.append(b)
        result.append(t)

        return result


    except:
        raise Exception("비율 계산 중 오류가 발생하였습니다.")


# git 활용도 점수 계산하는 함수
# 각 항목별 비율과
# 전체 팀들의 평균과 표준편차 필요
# 선택된 팀의 각 항목별 값 필요
# z점수와 표준 점수 계산
def gitEval(commitRate,lineRate,branchRate,teamRate, avgTotalData, stdTotalData, teamRawData) :


    # 입력한 수를 기준으로 비율 계산
    # 소수점 둘 째자리로 반올림
    # percentage = [commitRate, lineRate, branchRate, teamRate]
    percentage = []
    percentage = calPercent(commitRate,lineRate,branchRate,teamRate)

    # 전체 평균 대비 한 팀의 commit수, 수정된 줄 수, merge된 branch 수, 팀원 기여도 점수 계산하기
    # 표준화 z점수
    if stdTotalData[0] != 0 and stdTotalData[1] != 0 and stdTotalData[2] != 0 and stdTotalData[3] != 0 :

        teamRawData[0] = (teamRawData[0] - avgTotalData[0]) / stdTotalData[0] # -5 0.81
        teamRawData[1] = (teamRawData[1] - avgTotalData[1]) / stdTotalData[1] # -27.7 0.0
        teamRawData[2] = (teamRawData[2] - avgTotalData[2]) / stdTotalData[2] # 0.18 1.0
        teamRawData[3] = (teamRawData[3] - avgTotalData[3]) / stdTotalData[3] # -1.17 0.95

    else :

        if stdTotalData[0] == 0 :
            teamRawData[0] = 0
        if stdTotalData[1] == 0 :
            teamRawData[1] = 0
        if stdTotalData[2] == 0 :
            teamRawData[2] = 0
        if stdTotalData[2] == 0 :
            teamRawData[2] = 0

    # 표준 점수
    teamRawData[0] = teamRawData[0]*stdTotalData[0] + avgTotalData[0]
    teamRawData[1] = teamRawData[1]*stdTotalData[1] + avgTotalData[1]
    teamRawData[2] = teamRawData[2]*stdTotalData[2] + avgTotalData[2]
    teamRawData[3] = teamRawData[3]*stdTotalData[3] + avgTotalData[3]

    # 계산

    gitScore = 0

    for i in range(0,4) :

        gitScore += percentage[i] * teamRawData[i]
        # gitScore += round(percentage[i] * nomalData[i], 2)


    # 최종 결과값
    gitScore = float(format(gitScore, '.2f'))
    # gitScore = gitScore * 100

    return gitScore
