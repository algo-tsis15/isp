
def to_sec(data):
    h,m,s=map(int,data.split(':'))
    return h*60*60+m*60+s

def to_time(data):
    s= data%60
    data=data//60
    m= data%60
    data=data//60
    h=data
    tmp=''
    tmp+=str(h).zfill(2)
    tmp+=':'
    tmp+=str(m).zfill(2)
    tmp+=':'
    tmp+=str(s).zfill(2)
    return tmp

def solution(play_time, adv_time, logs):
    s = []
    e = []
    time=to_sec(play_time)
    dp = [0 for i in range(time+1)]
    # 초로 변환하여 저장
    for i in logs:
        start, end = map(str, i.split('-'))
        s.append(to_sec(start))
        e.append(to_sec(end))
        dp[s[-1]]+=1
        dp[e[-1]]-=1

    adv_time = to_sec(adv_time)
    for i in range(1,len(dp)):
        dp[i]=dp[i]+dp[i-1]

    for i in range(1,len(dp)):
        dp[i]=dp[i]+dp[i-1]

    most_view=0
    max_time=0

    for i in range(adv_time-1,time):
        if i> adv_time:
            if most_view < dp[i]-dp[i-adv_time]:
                most_view=dp[i]-dp[i-adv_time]
                max_time=i-adv_time+1
        else:
            if most_view< dp[i]:
                most_view=dp[i]
                max_time=i-adv_time+1
    return to_time(max_time)

print(solution("00:00:10","00:00:2",["00:00:04-00:00:07","00:00:06-00:00:08"]))