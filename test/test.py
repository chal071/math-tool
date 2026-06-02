def main():
    scores = {
        "数学": None,
        "英语": None,
        "物理": None,
        "化学": None,
        "生物": None
    }

    scores = get_scores(scores)

    scores = check_scores(scores)

    scores = edit_scores(scores)

    media = calculate_media(scores)

    level = calculate_level(media)

    print("最终成绩如下:")
    show_scores(scores)

    print(f"平均成绩为: {media}")
    print(f"等级为: {level}")


def get_scores(scores):
    for subject in scores:
        print(f"请输入{subject}的成绩:")
        try:
            score = float(input())
            if score < 0 or score > 100:
                raise ValueError("成绩必须在0到100之间。")
        except ValueError as e:
            print(f"输入无效：{e}")
        else:
            scores[subject] = score
    return scores

def check_scores(scores):
    for subject,score in scores.items():
        while score is None:
            print(f"{subject}的成绩未输入，请重新输入。")
            try:
                new_score = float(input(f"请输入新的{subject}成绩:"))
            except ValueError as e:
                print(f"输入无效：{e}")
            else:
                if new_score < 0 or new_score > 100:
                    print("成绩必须在0到100之间。")
                else:
                    scores[subject] = new_score
                    break
    return scores

def calculate_level(media):
    if media >= 90:
        return "A"
    elif media >= 80:
        return "B"
    elif media >= 70:
        return "C"
    elif media >= 60:
        return "D"
    else:
        return "E"
    
def edit_scores(scores):
    print("是否需要修改成绩？(y/n)")
    choice = input().lower()
    exit_choice = False
    exit_edit = False
    exit_score_num = False

    while not exit_choice:
        if choice == 'y':
            exit_choice = True
        elif choice == 'n':
            return scores
        else:
            print("输入无效，请输入'y'或'n'。")
    show_scores(scores)

    while not exit_score_num:
        print("请输入要修改的科目:")
        try:
            subject = input().strip()
            if subject not in scores:
                print("科目不存在。")
            else:
                exit_score_num = True
        except ValueError:
            print("输入无效。")

    while not exit_edit:
        print(f"请输入新的成绩:")
        try:
            new_score = float(input())
            if new_score < 0 or new_score > 100:
                raise ValueError("成绩必须在0到100之间。")
        except ValueError as e:
            print(f"输入无效：{e}")
        else:
            scores[subject] = new_score
            exit_edit = True
    return scores

def show_scores(scores):
    for subject, score in scores.items():
        print(f"{subject}的成绩为: {score}")

def calculate_media(scores):
    total = 0
    for score in scores.values():
        total += score
    return total / len(scores)
main()