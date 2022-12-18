"""
Try it here: https://replit.com/@Param302/Foundational-Term-1-Score-Calculator-IITM-BS-Degree
"""


class CalculateTotalScore:

    def __init__(self, final: float, q1: float, q2: float, gaas: float, pa_bonus: float) -> None:
        self.final = final
        self.q1 = q1
        self.q2 = q2
        self.gaas = gaas
        self.pa_bonus = pa_bonus

    @property
    def gaa(self) -> float:
        """Calculate Graded Assignment Average (GAA) of best 10 weekly assignment scores."""
        return sum(sorted(self.gaas, reverse=True)[:10]) / 10

    def first_formula(self) -> float:
        """T = 0.6F + 0.2max(Qz1, Qz2)
        excluded 0.1GAA"""
        return (0.6 * self.final) + (0.2 * (max(self.q1, self.q2)))

    def second_formula(self) -> float:
        """T = 0.4F + 0.2Qz1 + 0.3Qz2
        excluded 0.1GAA"""
        return (0.4 * self.final) + (0.2 * self.q1) + (0.3 * self.q2)

    def best_score(self) -> float:
        first_formula_score = 0.1 * self.gaa + self.first_formula()
        second_formula_score = 0.1 * self.gaa + self.second_formula()
        print(
            f"1st Formula [T = 0.1GAA + 0.6F + 0.2max(Qz1, Qz2)]\nScore: {first_formula_score:.2f}"
        )
        print(
            f"2nd Formula [T = 0.1GAA + 0.4F + 0.2Qz1 + 0.3Qz2]\nScore: {second_formula_score:.2f}"
        )

        if first_formula_score >= second_formula_score:
            total = first_formula_score
            print("1st formula score is used for evaluating total marks")
        else:
            total = second_formula_score
            print("2nd formula score is used for evaluating total marks")

        return total

    @staticmethod
    def get_grade(total_score: float) -> tuple:
        if total_score >= 90:
            return 'S', 10
        elif 90 >= total_score >= 80:
            return 'A', 9
        elif 80 >= total_score >= 70:
            return 'B', 8
        elif 70 >= total_score >= 60:
            return 'C', 7
        elif 60 >= total_score >= 50:
            return 'D', 6
        elif 50 >= total_score >= 40:
            return 'E', 4
        return 'U', 0


subjects = {}


def main() -> None:
    print("=" * 80)
    print(
        "Python program to calculate Total score of your Foundational Term 1 subjects\n"
    )
    print(
        "⚠ Disclaimer ⚠\nThis maybe inaccurate, please don't consider this score as final score, actual score may vary.\n"
    )
    n_subjects = int(
        input("How many subjects you have opted in Sept term ?\n"))
    while not (n_subjects in (1, 2, 3, 4)):
        print("Invalid subjects, min 1 or max 4 can be opted in a term.")
        n_subjects = int(
            input("How many subjects you have opted in Sept term ?\n"))
    for _ in range(n_subjects):
        print('\n', "-" * 50, sep='')
        subject = input("Enter subject name: ")
        n_weeks = int(
            input(f"How many weekly assignments do you have in {subject}?\n"))
        while n_weeks < 11 or n_weeks > 12:
            print(
                "Invalid total weeks, there are not more than 12 weeks or not less than 11 weeks.")
            n_weeks = int(
                input(f"How many weekly assignments do you have in {subject}?\n"))

        gaas = [
            float(input(f"Enter week {i} graded assignment score (%): ")) for i in range(1, n_weeks+1)
        ]

        q1 = float(input("\nEnter Quiz 1 score (%) (0 if not attempted): "))
        q2 = float(input("Enter Quiz 2 score (%) (0 if not attempted): "))

        if not any((q1, q2)):
            print(
                f"Sorry!\nYou have not attempted both quizzes so, you have failed in {subject}.\nYour current Grade is 'WQ' and grade point is 0\nYou have to repeat this course.\nAll the best!!!"
            )
            continue

        final = float(
            input("\nEnter End Term score (%) (0 if not attempted): "))
        subjects[subject] = [final]
        if not final:
            print(
                "You have to do the makeup exam.\nYour Grade is 'I'.\nAll the best!!!"
            )
            continue

        pa_bonus = float(input("\nEnter Practice assignment bonus marks: "))

        calc_score = CalculateTotalScore(final, q1, q2, gaas, pa_bonus)
        total_score = calc_score.best_score()
        total = total_score + \
            calc_score.pa_bonus if total_score <= 95 else total_score + \
            (100 - total_score)
        grade, point = calc_score.get_grade(total)

        print(
            f"\nYour Total score of {subject} is: {total_score:.2f} approx. (without mock bonus)")

        if total_score < 40:
            quiz_2_survey = min(40 - total_score, 5)
            print(
                f"Sorry!\nYou have failed in {subject}.\nYour marks are: \n If you have given *Quiz 2* and you have filled the survey, then you'll get upto 5 marks, i.e. [{total_score:.2f} + {quiz_2_survey:.2f} = {total_score+quiz_2_survey:.2f}]\nIf it's still less than 40, then you have to repeat the course.\nAll the best!!!"
            )
        else:
            print(
                f"{'*'*50}\nCongratulations!!!\nYou have passed in {subject} 1\nYou can opt {subject + ' 2' if subject[0].lower()!='c' else 'Python'} in upcoming term.\nAll the best!\n{'*'*50}"
            )
            print(
                f"\nYour Final score (T) of {subject} is: {total:.2f} approx.\nYour Grade is: '{grade}' and grade point is {point}\n")
            print(
                "Note: Mock bonus marks are not included, so your total score may increase."
            )

        subjects[subject].insert(0, total)
        subjects[subject].insert(1, grade)
        subjects[subject].insert(2, point)
    print('-' * 80, "\nYour Final scores are:")
    print(f" {'_'*39}")
    print("| Subject         |  Score   |    Grade  |")
    print(f"|{'-'*17}|{'-'*10}|{'-'*11}|")
    for sub in subjects:
        print(
            f"| {sub:<15} | {subjects[sub][0]: 3.2f}  |    {subjects[sub][1]} ({subjects[sub][2]: >2}) |")
    print(f"|{'_'*39}|")
    print(
        '=' * 80,
        "\nIf you have found any bug, please send the screenshot with the issue to Parampreet Singh.\nYou can also share your feedback.\nThank you for using this program!!! :)\nSocial handles:\nGithub: @Param302\nKaggle: @param302\nTelegram: @Param_302\nTwitter: @param3021\n",
        '=' * 80)


if __name__ == "__main__":
    main()
