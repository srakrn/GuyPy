# รับคำเข้ามา
word = input()
# ให้ i เท่ากับ 0
i = 0
# ประกาศตัวแปรไว้เก็บคำว่าถึงไหนแล้ว
printtxt = ""
# ระหว่างที่ i น้อยกว่าความยาวตัวอักษร (เช็คถึงตัวก่อนตัวสุดท้าย เพราะใช้ < และเช็คได้ถ้าเกรดเดอร์ไม่เหี้ย อีสัส)
while(i<len(word)):
    # ดึงค่าอักษรตัวที่ i
    letter = word[i]
    # ให้ตัวแปร pos วิ่งเช็คตัวอักษรตัวต่อๆ มา โดยให้เริ่มที่ตัวที่กำลังดูอยู่
    pos = i
    # ประกาศตัวแปร consecutive เป็นตัวแปรนับว่าติดกันมากี่ตัวแล้ว
    consecutive = 0
    # ระหว่างที่ pos ยังไปไม่เกินความยาวคำ และระหว่างที่อักษรตัวที่ i ยังเท่ากับตัวที่ pos
    while(pos < len(word) and letter == word[pos]):
        # เพิ่มค่า pos ไปหนึ่ง
        pos += 1
        # เพิ่มจำนวนตัวติดกันไป 1
        consecutive += 1
    # เตรียมข้อความที่จะ print ได้แก่ตัวอักษรและจำนวนที่นับได้
    printtxt += letter + " " + str(consecutive) + " "
    i += consecutive
print(printtxt[:-1])