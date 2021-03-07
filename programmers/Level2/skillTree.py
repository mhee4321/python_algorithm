def solution(skill, skill_trees):
    skill = list(skill)
    answer = 0
    for i in skill_trees:
        post_skill = []
        for j in list(i):
            if j in skill:
                post_skill.append(j)

        for idx, j in enumerate(post_skill):
            if j != skill[idx]:
                answer += 1
                break
    return len(skill_trees) - answer

def solution2(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))