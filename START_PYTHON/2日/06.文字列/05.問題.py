# "ㅂ"한자에 있는 문자를 이용하여 30cm자를 완성하시오

cm = int(input("몇 센티 :"))
row = "┌" + "─" *(cm - 2) + "┐"
column = "│" * cm
print(row + "\n" + column)
