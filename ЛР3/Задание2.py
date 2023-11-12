def find_common_participants(gr1, gr2, comma = ','):
    participants1 = gr1.split(comma)
    participants2 = gr2.split(comma)
    set1 = set(participants1)
    set2 = set(participants2)
    group = set1.intersection(set2)
    return sorted(list(group))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
final_group = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", final_group)

