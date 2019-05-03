'''
This application was created by John Dinkleberg
Do not modify without permission
If you do modify then you risk breaking the program
'''


def get_total_score(score):
    total_score = 0
    total_score += score
    return total_score


def intro_questions():
    conductor = input("Enter your name ")
    name = input("Enter interviewee's name ")
    time_zone = input("Enter interviewee's time zone ")
    date_of_hire = input("Enter the date ")
    call_sign = input("What will his call sign be? ")
    return conductor, name, time_zone, date_of_hire, call_sign


def Chain_of_command(score):
    print("What is the chain of command starting at the lowest rank?")
    e = 0
    while e == 0:
        try:
            c_score = float(input("Points earned (1 - 10): "))
            c_score = get_total_score(c_score)
            e = 1
        except ValueError:
            e = 0
    return c_score


def rank_questions(score):
    asked_questions = []
    questions_asked = 0
    question = 0
    e = 0
    question_dict = {1: "Who is the current Director of the ERD? ",
                     2: "Who is the current Assistant Director of the ERD? ",
                     3: "Who is the current ERD Captain? ",
                     4: "Who is the current Fire and Rescue Captain? ",
                     5: "Why do we have a chain of command? "}
    while questions_asked < 5:
        e = 0
        e1 = 0
        while question not in question_dict:
            while e == 0:
                try:
                    question = int(input("Pick a question (1 - 5): "))
                    if question not in asked_questions:
                        question = question
                        e = 1
                    else:
                        question = -1
                        e = 1
                except:
                    e = 0
        print(question_dict[question])
        while e1 == 0:
            try:
                g_score = float(input('Points earned (1 - 10): '))
                e1 += 1
            except:
                e1 = 0
        score += g_score
        asked_questions.append(question)
        question = -1
        questions_asked += 1
    score = get_total_score(score)
    return score


def general_questions(score):
    asked_questions = []
    questions_asked = 0
    question = -1
    question_dict = {1: "List one core value of EMS ",
                     2: "How do you decide who is treated first? ",
                     3: "Can you commit crime or partake in illegal " \
                        "activities while on duty? ",
                     4: "Are you allowed to go off duty as a Probationary" \
                        "EMT? ",
                     5: "Is there any EMS regulation regarding the clothing " \
                        "you wear? ",
                     6: "While on duty you witness a crime, is your EMS " \
                        "neutrality preventing you from being able to " \
                        "report this crime? "}
    while questions_asked < 6:
        e = 0
        e1 = 0
        while question not in question_dict:
            while e == 0:
                try:
                    question = int(input("Pick a question (1 - 5): "))
                    if question not in asked_questions:
                        question = question
                        e = 1
                    else:
                        question = -1
                        e = 1
                except:
                    e = 0
        print(question_dict[question])
        while e1 == 0:
            try:
                g_score = float(input('Points earned (1 - 10): '))
                e1 += 1
            except:
                e1 = 0
        score += g_score
        asked_questions.append(question)
        question = -1
        questions_asked += 1
    score = get_total_score(score)
    return score


def sop_questions(score):
    asked_questions = []
    questions_asked = 0
    question = -1
    question_dict = {1: "What are the vehicle emergency codes and when should" \
                        " be used? ",
                     2: "What is the minimum distance you must remain from an" \
                        " ongoing gun fight? ",
                     3: "Who is exempt from EMS Custody? ",
                     4: "As a probie EMT can you have a ride along? "}
    while questions_asked < 4:
        e = 0
        e1 = 0
        while question not in question_dict:
            while e == 0:
                try:
                    question = int(input("Pick a question (1 - 5): "))
                    if question not in asked_questions:
                        question = question
                        e = 1
                    else:
                        question = -1
                        e = 1
                except:
                    e = 0
        print(question_dict[question])
        while e1 == 0:
            try:
                g_score = float(input('Points earned (1 - 10): '))
                e1 += 1
            except:
                e1 = 0
        score += g_score
        asked_questions.append(question)
        question = -1
        questions_asked += 1
    score = get_total_score(score)
    return score


def role_play_questions(score):
    asked_questions = []
    questions_asked = 0
    question = -1
    question_dict = {1: "I crashed my car into a telephone pole at " \
                        "Vinewood.  My wrist really hurts and my car is " \
                        "broken - 911 Dispatch",
                     2: "The patient was involved in a gunfight and is " \
                        "riddled with injuries. They can barely speak or move" \
                        "and appears to be in critical condition - police guy",
                     3: "You revive someone after a gunfight has taken " \
                        "place, but the patient runs away from you! what do "\
                        "you do?"}
    while questions_asked < 3:
        e = 0
        e1 = 0
        while question not in question_dict:
            while e == 0:
                try:
                    question = int(input("Pick a question (1 - 5): "))
                    if question not in asked_questions:
                        question = question
                        e = 1
                    else:
                        question = -1
                        e = 1
                except:
                    e = 0
        print(question_dict[question])
        while e1 == 0:
            try:
                g_score = float(input('Points earned (1 - 10): '))
                e1 += 1
            except:
                e1 = 0
        score += g_score
        asked_questions.append(question)
        question = -1
        questions_asked += 1
    score = get_total_score(score)
    return score


def equipment_questions(score):
    asked_questions = []
    questions_asked = 0
    question = -1
    question_dict = {1: "Is it okay for civs to call 911 to ask for help?",
                     2: "What are the speed limits when in code 1?" }
    while questions_asked < 2:
        e = 0
        e1 = 0
        while question not in question_dict:
            while e == 0:
                try:
                    question = int(input("Pick a question (1 - 5): "))
                    if question not in asked_questions:
                        question = question
                        e = 1
                    else:
                        question = -1
                        e = 1
                except:
                    e = 0
        print(question_dict[question])
        while e1 == 0:
            try:
                g_score = float(input('Points earned (1 - 10): '))
                e1 += 1
            except:
                e1 = 0
        score += g_score
        asked_questions.append(question)
        question = -1
        questions_asked += 1
    score = get_total_score(score)
    return score


def pass_or_fail(score):
    if score == 210:
        return True
    elif score >= 90:
        return True
    else:
        return False


def fail_file(conductor, name, date, score):
    file = open('personal_file.txt', 'w')
    data_file = f'''
    Name: {name}
    Date Of Failure: {date}
    Test Score: {score}
    {name} can retake the test in 24 hours from {date}
    Approved By: {conductor}
    '''
    file.write(data_file)
    file.close()


def pass_file(conductor, name, date, time_zone, call_sign, score):
    fname = name.replace(' ', '_')
    file = open(f'{fname}.txt', 'w')
    data_file = f'''
    Name: {name}
    Date Of Hire: {date}
    Time Zone: {time_zone}
    Test Score: {score}
    Position: Probie EMT
    Callsign: {call_sign}
    Strikes: N/A
    Approved By: {conductor}
    '''
    file.write(data_file)
    file.close()


def main():
    score = 0
    c, n, tz, doh, call_sign = intro_questions()
    COC_score = Chain_of_command(score)
    rank_score = rank_questions(COC_score)
    general_score = general_questions(rank_score)
    sop_score = sop_questions(general_score)
    rp_score = role_play_questions(sop_score)
    equipment_score = equipment_questions(rp_score)
    exam = pass_or_fail(equipment_score)
    if exam is True:
        pass_file(c, n, doh, tz, call_sign, equipment_score)
    else:
        fail_file(c, n, doh, equipment_score)
    # TODO: Git hub posting
    return score


if __name__ == '__main__':
    main()
