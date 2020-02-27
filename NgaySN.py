ngay_ht = 24
thang_ht = 8
ngay_sinh = 24
thang_sinh = 12
so_ngay = 0
kc = 0
temp = 0
temp1 = 0
thang = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if thang_sinh == thang_ht and ngay_sinh < ngay_ht:
    total = ngay_sinh - ngay_ht
else:
    drange = list(range(thang_ht + 1, thang_sinh))
    if thang_ht > thang_sinh:
        drange = list(range(thang_ht + 1, 13))
        drange += list(range(1, thang_sinh))
    print (drange)
    total = sum([thang[t] for t in drange])
    total += thang[thang_ht] - ngay_ht + ngay_sinh
print("Total",total)

if thang_sinh > thang_ht:
    if thang_sinh - thang_ht == 1:
        so_ngay = thang[thang_ht] - ngay_ht + ngay_sinh
        print(so_ngay)
    for i in range((thang_ht + 1), thang_sinh):
        kc += thang[i]
        so_ngay = thang[thang_ht] - ngay_ht + ngay_sinh + kc
    print(so_ngay)

if thang_sinh == thang_ht and ngay_sinh >= ngay_ht:
    so_ngay = ngay_sinh - ngay_ht
    print(so_ngay)

if thang_sinh < thang_ht:
    for i in range((thang_ht + 1), 13):
        temp += thang[i]

    for z in range(1, thang_sinh):
        temp1 += thang[z]
    kc = temp + temp1
    so_ngay = thang[thang_ht] - ngay_ht + ngay_sinh + kc
    print(so_ngay)

if thang_sinh == thang_ht and ngay_sinh < ngay_ht:
    so_ngay = 365 - (ngay_ht - ngay_sinh)
    print(so_ngay)
