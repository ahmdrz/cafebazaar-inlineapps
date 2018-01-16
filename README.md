# cafebazaar-inlineapps
simple crawler that can index all of the Cafebazaar inline applications.

#### To get top 3 apps run based on users who rates

```
python main.py -c 3
```

#### To get top 3 apps run based on rates only

```
python main.py -c 3 -s true
```

---

```bash
usage: main.py [-h] [-s SORT] [-c COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -s SORT, --sort SORT  sort only with rates, default is count of each rate * corresponding rate
  -c COUNT, --count COUNT
                        count of inline-apps

```

---

results at `Tue Jan 16, 17:34:00` based on :

```
number : 0
name : فال حافظ - غزل و تفسیر
users : 579
rate : {1: 36, 2: 17, 3: 15, 4: 30, 5: 481} (2640)
-----------------
number : 1
name : قرآن کریم (بدون نصب)
users : 505
rate : {1: 31, 2: 13, 3: 21, 4: 28, 5: 412} (2292)
-----------------
number : 2
name : فال حافظ
users : 463
rate : {1: 41, 2: 8, 3: 16, 4: 39, 5: 359} (2056)
-----------------
number : 3
name : تمشک (خرید آنی شارژ)
users : 261
rate : {1: 73, 2: 13, 3: 19, 4: 16, 5: 140} (920)
-----------------
number : 4
name : واژه یاب (‌برنامه آنی)
users : 160
rate : {1: 10, 2: 3, 3: 6, 4: 10, 5: 131} (729)
-----------------
number : 5
name : دیلماج - مترجم آنی
users : 159
rate : {1: 23, 2: 4, 3: 8, 4: 14, 5: 110} (661)
-----------------
number : 6
name : لرزه نگار آنی
users : 134
rate : {1: 16, 2: 7, 3: 8, 4: 9, 5: 94} (560)
-----------------
number : 7
name : نظریو: نظرسنجی آنی با هدیه
users : 228
rate : {1: 140, 2: 13, 3: 14, 4: 9, 5: 52} (504)
-----------------
number : 8
name : آموزش لغات انگلیسی (Casco)
users : 109
rate : {1: 14, 2: 3, 3: 5, 4: 12, 5: 75} (458)
-----------------
number : 9
name : لرزه‌نگر آنی
users : 96
rate : {1: 14, 2: 1, 3: 2, 4: 7, 5: 72} (410)
-----------------
number : 10
name : لینکک
users : 75
rate : {1: 8, 2: 0, 3: 2, 4: 5, 5: 60} (334)
-----------------
number : 11
name : روزآغاز
users : 71
rate : {1: 5, 2: 1, 3: 3, 4: 1, 5: 61} (325)
-----------------
number : 12
name : قرون - قیمت ارز و سکه
users : 54
rate : {1: 3, 2: 2, 3: 2, 4: 2, 5: 45} (246)
-----------------
number : 13
name : خبر ورزشی ، آنی با خبر شو
users : 56
rate : {1: 7, 2: 2, 3: 2, 4: 5, 5: 40} (237)
-----------------
number : 14
name : تمشک (خرید آنی بسته اینترنت)
users : 52
rate : {1: 15, 2: 0, 3: 4, 4: 1, 5: 32} (191)
-----------------
number : 15
name : نبض بازار (آنی)
users : 47
rate : {1: 10, 2: 1, 3: 2, 4: 5, 5: 29} (183)
-----------------
number : 16
name : دکه - اخبار سیاسی، ورزشی و تکنولوژی
users : 37
rate : {1: 1, 2: 0, 3: 4, 4: 4, 5: 28} (169)
-----------------
number : 17
name : بیست جوک
users : 40
rate : {1: 8, 2: 4, 3: 4, 4: 1, 5: 23} (147)
-----------------
number : 18
name : ترب (اپ آنی)
users : 37
rate : {1: 8, 2: 3, 3: 1, 4: 2, 5: 23} (140)
-----------------
number : 19
name : سرسبد (رستوران و کافه‌گردی)نسخه آنی
users : 27
rate : {1: 3, 2: 0, 3: 0, 4: 2, 5: 22} (121)
-----------------
number : 20
name : برترین ها _ اخبار و مطالب داغ (آنی)
users : 26
rate : {1: 4, 2: 1, 3: 2, 4: 4, 5: 15} (103)
-----------------
number : 21
name : بیت نرخ (قیمت بیت‌کوین)
users : 22
rate : {1: 5, 2: 0, 3: 3, 4: 0, 5: 14} (84)
-----------------
number : 22
name : شوت - نتایج زنده
users : 17
rate : {1: 0, 2: 0, 3: 0, 4: 3, 5: 14} (82)
-----------------
number : 23
name : لایک بگیر اینستاگرام - نسخه آنی
users : 26
rate : {1: 12, 2: 2, 3: 2, 4: 0, 5: 10} (72)
-----------------
number : 24
name : بوکسام (آنی)
users : 17
rate : {1: 3, 2: 1, 3: 3, 4: 1, 5: 9} (63)
-----------------
number : 25
name : کارین (اپ آنی) - در تهران
users : 15
rate : {1: 3, 2: 0, 3: 1, 4: 0, 5: 11} (61)
-----------------
number : 26
name : نی نی بان _ راهنمای کودکیاری (آنی)
users : 13
rate : {1: 3, 2: 1, 3: 1, 4: 1, 5: 7} (47)
-----------------
number : 27
name : آفر (آنی)
users : 10
rate : {1: 1, 2: 0, 3: 0, 4: 0, 5: 9} (46)
-----------------
number : 28
name : کامنت بگیر اینستاگرام - نسخه آنی
users : 14
rate : {1: 7, 2: 1, 3: 0, 4: 0, 5: 6} (39)
-----------------
number : 29
name : کرفس (برنامه آنی)
users : 0
rate : {1: 0, 2: 0, 3: 0, 4: 0, 5: 0} (0)
-----------------
```