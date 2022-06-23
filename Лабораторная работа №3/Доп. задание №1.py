import re
tests = ["Студент Вася вспомнил, что на своей лекции Балакшин П.В. ",
         "упоминал про старшекурсников, которые буду ему",
         "помогать: Анищенко А.А. и Машина Е.А.,",
         "но также он напомнил своим соседям: Эрбаев И.Ю. и Степанов А.А.,",
         "Машина Е.А. может спрашивать о регулярных выражениях."]

for testnumber in range(len(tests)):
    test = tests[testnumber]
    print(f"Тест №{testnumber+1}:\n{test}\n")

    print("Фамилии:")
    initials = re.findall(r"\b[А-Я][а-я]*\s[А-Я]\.[А-Я]\.", test)
    for i in initials:
        print(i)
    if len(initials)==0:
        print("Не обнаружено.")
    print("\n")
