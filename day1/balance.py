months = [
    ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"], 
    ["ינואר", "פברואר", "מרץ", "אפריל", "מאי", "יוני", "יןלי ", "אוגוסט", "ספטמבר", "אוקטובר", "נובמבר", "דצמבר"]
    ]

incomes = [150, 250, 350, 400, 500, 700, 550, 200, 160, 450, 320, 700]
outcomes = [100, 270, 540, 250, 150, 300, 500, 250, 100, 500, 100, 200]



lang_code=int(input("Enter language code:\n 1 - EN\n 2 - RU\n 3 - HE\n"))-1
month_number = int(input("Enter month number [1--12]:\n")) - 1
print (
    f"""
        month name {months[lang_code][month_number]}
        incomes: {incomes[month_number]}
        outcomes: {outcomes[month_number]}
        balance: {incomes[month_number] - outcomes[month_number]}
    """)

for next_mont_number in range(len(months[0])):
    print(
        f"""
        month n {[next_mont_number]}\t month name {months[lang_code][next_mont_number]}
        incomes: {incomes[next_mont_number]}
        outcomes: {outcomes[next_mont_number]}
        balance: {incomes[next_mont_number] - outcomes[next_mont_number]}
        """)
for next_mont_number in range(len(months[0])):
    if incomes[next_mont_number] - outcomes[next_mont_number] <0:
        print (
            f"""
            month n {[next_mont_number]}\t month name {months[lang_code][next_mont_number]}
            incomes: {incomes[next_mont_number]}
            outcomes: {outcomes[next_mont_number]}
            balance: {incomes[next_mont_number] - outcomes[next_mont_number]}
            """)