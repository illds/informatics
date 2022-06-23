import re
import random, sys
students = ["Берехелис А.Б. P3112", "Борисов Б.Б. P3132", "Васильев В.В. P3114",
            "Волненко Д.А. P3112", "Гасюк А.А. P311345", "Демидович Д.Д. P3112",
            "Дорожкин И.Д. P31112", "Абдурасул К.М. P3132", "Степанов С.С. P3112",
            "Сухарева С.С. P3114", "Филюшкин К.С. P3112", "Эрбаев И.Ю. P3112"]

for testnumber in range(5):
    test = []
    for j in range(random.randint(2, len(students))):
        test.append(students[random.randint(0, len(students)-1)])

    final_list = []
    print(f"Тест №{testnumber+1}:")
    for i in range(len(test)):
        print(test[i])
        
    for part in test:
        initials = re.findall(r"([А-Я]\.)\1\sP3112", part)
        if len(initials) == 0:
            final_list.append(part)
            
    print("\nИтоговый список:")
    for i in range(len(final_list)):
        print(final_list[i])
    print("~~~~~~~~~~~~~~~~~~~~")
