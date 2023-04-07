import re
import pprint
def solution(word, pages):

    total_score = []
    basic_score = {}
    exlink_cnt = {}
    to_me_link = {}

    for page in pages:
        title = re.search('<meta property="og:url" content="(https://\S+)"', page).group(1)
        basic_score[title] = 0
        exlink_cnt[title] = 0

        for find in re.findall('[a-zA-Z]+', page):
            if find.upper() == word.upper():
                basic_score[title] += 1

        for link in re.findall('<a href="(https://\S+)"', page):
            exlink_cnt[title] += 1
            if link in to_me_link:
                to_me_link[link].append(title)
            else:
                to_me_link[link] = [title]

    print(basic_score)
    print(exlink_cnt)
    print(to_me_link)

    max_score = -1
    max_idx = -1
    for idx, title in enumerate(basic_score.keys()):
        tmp = 0

        if title in to_me_link:
            for ex in to_me_link[title]:
                tmp += (basic_score[ex] / exlink_cnt[ex])

        score = basic_score[title] + tmp
        total_score.append(score)
        if score > max_score:
            max_score = score
            max_idx = idx

    print(total_score)
    print(max_idx)
    return max_idx