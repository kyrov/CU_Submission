#----------------------------------------
# Q3: Checker
#----------------------------------------
pos = input().strip()  # รับมามีอย่างน้อย 1 ตัวแน่ ๆ
row = ''
col = ''
if len(pos) <= 3: 
    # แบบที่ 1
    f1 = False
    f2 = False
    row = pos[0]
    for i in range(len(pos)):
        if(i!=0 and pos[i] != ' '):
            col += pos[i]
    if(row.isalpha()):
        f1 = False
    else:
        f1 = True
    if(not col.isdigit()):
        f2 = True
    if(f2 == False and col != ''):
        if(int(col) >= 1 and int(col) <= 52):
            f2 = False
        else:
            f2 = True
    if(f1 == False and f2 == False  and col != ''):
        if(ord(row) >= ord('A') and ord(row) <= ord('Z')):
            if((ord(row)-ord('A'))%2==0):
                if(int(col)%2==0):
                    print('Black')
                else:
                    print('White')
            else:
                if(int(col)%2==1):
                    print('Black')
                else:
                    print('White')
        else:
            if((ord(row)-ord('a'))%2==0):
                if(int(col)%2==0):
                    print('Black')
                else:
                    print('White')
            else:
                if(int(col)%2==1):
                    print('Black')
                else:
                    print('White')
    elif(f1 == True and f2 == False):
        print("Invalid row")
    elif(f1 == False and f2 == True):
        print("Invalid column")
    else:
        print("Invalid row and column")
else:
    # แบบที่ 2 (กรณีนี้ค่อยทำทีหลังก็ได้ เพราะยุ่งกว่า แต่ให้คะแนนแค่ 20%)
    # หาค่าของตัวอักษรแถว มาใส่ในตัวแปร  row ถ้าหาไม่พบ ก็ให้เป็นสตริงว่าง ๆ
    # หาค่าของเลขคอลัมน์ มาใส่ในตัวแปร  col ถ้าหาไม่พบ ก็ให้เป็นสตริงว่าง ๆ
    # ในกรณีที่ยังไม่ได้เขียนแบบที่ 2 ก็เขียนคำสั่งนี้ไว้ก่อน (ไม่งั้น ระบบจะฟ้องว่าหลัง else ไม่มีคำสั่ง)
    f1 = False
    f2 = False
    if(pos[0]=='r'):
        row,col = pos.split(',')
    else:
        col,row = pos.split(',')
    i=0
    while(row[i]!='='):
        i+=1
    row = row[i+1:]
    i=0
    while(col[i]!='='):
        i+=1
    col = col[i+1:]
    row = row.strip()
    col = col.strip()
    if(row.isalpha() and len(row)==1):
        f1 = False
    else:
        f1 = True
    if(not col.isdigit()):
        f2 = True
    if(f2 == False and col != ''):
        if(int(col) >= 1 and int(col) <= 52):
            f2 = False
        else:
            f2 = True
    if(f1 == False and f2 == False  and col != ''):
        if(ord(row) >= ord('A') and ord(row) <= ord('Z')):
            if((ord(row)-ord('A'))%2==0):
                if(int(col)%2==0):
                    print('Black')
                else:
                    print('White')
            else:
                if(int(col)%2==1):
                    print('Black')
                else:
                    print('White')
        else:
            if((ord(row)-ord('a'))%2==0):
                if(int(col)%2==0):
                    print('Black')
                else:
                    print('White')
            else:
                if(int(col)%2==1):
                    print('Black')
                else:
                    print('White')
    elif(f1 == True and f2 == False):
        print("Invalid row")
    elif(f1 == False and f2 == True):
        print("Invalid column")
    else:
        print("Invalid row and column")


row = row.strip()
col = col.strip()
#-----------------------------------------
valid_row = True
valid_col = True

# ตรวจค่าของสตริง row ถ้าผิด ก็เปลี่ยนตัวแปร valid_row ให้เป็น False




# ตรวจค่าของสตริง col ถ้าผิด ก็เปลี่ยนตัวแปร valid_col ให้เป็น False







#-----------------------------------------  
# ตรวจค่าของตัวแปร valid_row และ valid_col
# เพื่อแสดงข้อผิดพลาด ถ้ามีค่าเป็น False (มี 3 กรณี)
# ถ้าไม่มีข้อผิดพลาด ก็ค่อยตัดสินใจว่าจะแสดง Black หรือ White ตามสีพื้นของช่อง row, colrow, col