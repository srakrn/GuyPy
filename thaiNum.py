in_txt = input("Enter digits: ")
out_txt = ""
arabic_number = "0123456789"
thai_number = "๐๑๒๓๔๕๖๗๘๙"
for c in in_txt:
  k = arabic_number.index(c) if c in arabic_number else k=-1
  if k<0:
    out_txt += c
  else:
    out_txt += thai_number[k]
print(out_txt)
