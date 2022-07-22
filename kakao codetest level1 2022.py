def solution(id_list, report, k):
    n = len(id_list)
    mail_cnt = {id_list[i]: 0 for i in range(n)}
    respondent_cnt = {id_list[i]: 0 for i in range(n)}
    respondent_declarant = {id_list[i]: [] for i in range(n)}

    for i in range(len(report)):
        a, b = report[i].split()
        if a not in respondent_declarant[b]:
            respondent_declarant[b].append(a)  # 피신고자 , 신고자들 dict
            respondent_cnt[b] += 1

    for key in respondent_cnt:
        if respondent_cnt[key] >= k:
            for tmp in respondent_declarant[key]:
                mail_cnt[tmp] += 1

    answer = [mail_cnt[key] for key in mail_cnt]
    return answer
a=["muzi", "frodo", "apeach", "neo"]
b=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
print(solution(a,b,k))