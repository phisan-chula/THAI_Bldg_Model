#Research on Thai Building Modelling<br/>
งานวิจัย Open 3D Thai Building Model เป็นการผลิตข้อมูลแบบจำลองอาคาร LOD-1 ให้เป็น LOD-2 3 มิติ เพื่อการใช้งานทั่วๆไป<br/>
การแสดงผลแบบจำลองของเมือง Ciyt Model ที่ประกอบด้วยรูปสามมิติของตึกอาคารสิ่งปลูกสร้างผ่านระบบออนไลน์ อาจเลือกเทคนิคการแสดงผลได้ 4 แบบคือ<br/>

A) แบบจำลองสามมิติชนิด *Extrude model หรือ 3D Solid Model* ได้จากการสร้างรูปทรงหลายเหลี่ยมจากรอยพิมพ์ฐานอาคาร (foot-print) แล้วดึงยึดขึ้น หรือเริ่มจากเส้นรอบหลังคา roof-line ฉายลงบนผิวโลก (LOD-1) ตามข้อมูลความสูงอาคาร ทำให้ได้รูปทรงปริมาตรของอาคาร (LOD-2) ดังตัวอย่างปรากฏใน [3D Extrude Model](http://infraplus-dev.org:8084/Apps/main.html)<br/>

B) แบบจำลองสามมิติชนิด *3D Texture Model* ที่เกิดจาก 3D solid model แต่เสริมเติมผิวด้านข้างและหลังค่าด้วย textture ซึ่งมักจะใช้การถ่ายภาพจากพื้นดินหรือถ่ายภาพทางอากาศเฉียงเข้าหาตัวอาคาร ตัวอย่างแบบจำลองอาคารสามมิติแบบนี้จะมีปรากอัตลักษณ์ของอาคารทำให้ผู้ใช้ง่ายต่อการจดจำ ตัวอย่างปรากฏใน [3D Texture Model](https://http://infraplus-dev.org:8084/Apps/main.html)<br/>

C) แบบจำลองสามมิติ *3D point-cloud model* ที่อาจผลิตจากส่วนซ้อนของภาพถ่ายทางอากาศด้วยเทคนิด structure from motion (SfM) หรือได้จากการกราดด้วยเลเซอร์หรือไลดาร์ แบบจำลองชนิดนี้ทำได้ง่ายและค่อนข้างเป็นกระบวนการผลิตอัตโนมัติทั้งหมด ดังตัวอย่างปรากฏใน [3D Point-cloud Model](https://cu-pointcloud.web.app/viewer/CU-UAV/CU-pointcloud?x=665175.6&y=1518388.4)<br/>

      ขอบคุณ Microsoft BingMaps ได้ปล่อยข้อมูลรอยพิมพ์ฐานอาคารทั่วโลกกว่า 777 ล้านหลังคาเรือน โดยรอยพิมพ์ฐานอาคารได้จากภาพถ่ายรายละเอียดสูงจากดาวเทียมจาก คศ.2014 ถึง 2021 <br/>
ในพื้นที่ประเทศไทย ปรากฏรอยพิมพ์ฐานอาคาร 24,505,493 อาคาร เป็นข้อมูลบีบอัด 1.8GB ทีมวิจัยได้ทำการแบ่งออกเป็นรายจังหวัด โดยใช้ขอบเขตจาก GADM ver4.0 ผู้ที่สนใจสามารถดาวโหลดในรูปแบบ geopackage รายจังหวัดได้<br/>
This data is licensed by Microsoft under the Open Data Commons Open Database License (ODbL).
 <br/>
![Buiding Footprint at ChulaUniv](https://github.com/phisan-chula/Thai_Bldg_Model/blob/main/ML_Bldg_Chula.png)
<br/>
<br/>

#Research on Thai Building Modelling<br/>
|    | Name                     | AreaKm2   | NumBldg   | Size     | LINK                                                                                       |
|----|--------------------------|-----------|-----------|----------|--------------------------------------------------------------------------------------------|
|  0 | Amnat Charoen            | 3,371.2   | 183,873   | 76.9 MB  | [link](https://drive.google.com/file/d/1Wc-Fp3C03wIO4gb_2KADIJjvLU7qIzw5/view?usp=sharing) |
|  1 | Ang Thong                | 982.7     | 112,731   | 46.6 MB  | [link](https://drive.google.com/file/d/1hMd8KfJoeR9De1121mkdC28-KTVQOAdO/view?usp=sharing) |
|  2 | Bangkok Metropolis       | 1,611.2   | 1,101,690 | 548.3 MB | [link](https://drive.google.com/file/d/1eZXmdrXS8o5ZFjToz6fwFwesB4bUXQt8/view?usp=sharing) |
|  3 | Bueng Kan                | 4,204.9   | 149,759   | 57.2 MB  | [link](https://drive.google.com/file/d/1bCepLgJVKLYX2NxrNSG2DKq72F5DE7Lh/view?usp=sharing) |
|  4 | Buri Ram                 | 10,420.0  | 607,921   | 254.8 MB | [link](https://drive.google.com/file/d/1dXM88_w_A2bN8_P7qtJ_DDrI0LaeGe5p/view?usp=sharing) |
|  5 | Chachoengsao             | 5,372.8   | 299,289   | 144.5 MB | [link](https://drive.google.com/file/d/1pI1evpiz2eI9Ie7obW0P57FbpLEiiZcd/view?usp=sharing) |
|  6 | Chai Nat                 | 2,554.9   | 143,552   | 59.8 MB  | [link](https://drive.google.com/file/d/1k6uDNrjmZCtUfOXATqCRSuTEugAQbv_W/view?usp=sharing) |
|  7 | Chaiyaphum               | 13,177.7  | 458,867   | 186.9 MB | [link](https://drive.google.com/file/d/1mEYQM8Eds_KdQ80RWTkbuD6YxIBSNuHO/view?usp=sharing) |
|  8 | Chanthaburi              | 6,430.8   | 207,797   | 86.8 MB  | [link](https://drive.google.com/file/d/1m2k_WljewXych6am0hsygAF5mYy_bENu/view?usp=sharing) |
|  9 | Chiang Mai               | 23,339.4  | 973,280   | 409.1 MB | [link](https://drive.google.com/file/d/1Y-94mqNG2NsC7NOlSnjTdaNAlH0aHF2c/view?usp=sharing) |
| 10 | Chiang Rai               | 12,299.4  | 634,504   | 262.7 MB | [link](https://drive.google.com/file/d/1-mvw4H7abpQc1t-R5X968fDK1sqGnEMp/view?usp=sharing) |
| 11 | Chon Buri                | 4,596.1   | 564,246   | 235.1 MB | [link](https://drive.google.com/file/d/1_sSHCTcaEFxf_E_klkCPpgpl-xc8mTc0/view?usp=sharing) |
| 12 | Chumphon                 | 6,105.1   | 199,609   | 80.8 MB  | [link](https://drive.google.com/file/d/1qAQ1so_2I8rrr4LHieV4z2Fm5WR9G0O4/view?usp=sharing) |
| 13 | Kalasin                  | 7,200.3   | 423,285   | 174.9 MB | [link](https://drive.google.com/file/d/12Kvr0WVsp_2hMgIsHk-kEtJhNxFMan0Y/view?usp=sharing) |
| 14 | Kamphaeng Phet           | 8,996.5   | 283,740   | 127.9 MB | [link](https://drive.google.com/file/d/16LTQRDHNlG0DnXEira6S36lLuPI3kex8/view?usp=sharing) |
| 15 | Kanchanaburi             | 20,001.4  | 338,432   | 152.9 MB | [link](https://drive.google.com/file/d/1KiumquGh8bFRx_tj-LFR-VEohlsjt0hm/view?usp=sharing) |
| 16 | Khon Kaen                | 11,050.7  | 733,519   | 299.6 MB | [link](https://drive.google.com/file/d/1Z1y03JyxEQ2DqCmR5AR8r0cJOP253BUr/view?usp=sharing) |
| 17 | Krabi                    | 4,897.4   | 142,543   | 57.9 MB  | [link](https://drive.google.com/file/d/1D2Ijnlozk5x8bqHIm2o1cs_wZB00tdus/view?usp=sharing) |
| 18 | Lampang                  | 13,181.1  | 421,302   | 170.0 MB | [link](https://drive.google.com/file/d/1p_Dq-fPfvLOqlyNpn42W7v6apxUQ62jn/view?usp=sharing) |
| 19 | Lamphun                  | 4,721.3   | 244,786   | 103.0 MB | [link](https://drive.google.com/file/d/1BNlVGy5iSqchFEG6hsuCuTm6YglCCxuD/view?usp=sharing) |
| 20 | Loei                     | 11,033.7  | 251,135   | 97.8 MB  | [link](https://drive.google.com/file/d/1A7ihHdsGsZagaiSidLhd1keLD5gvozgM/view?usp=sharing) |
| 21 | Lop Buri                 | 6,478.0   | 292,554   | 112.5 MB | [link](https://drive.google.com/file/d/13LtC0m8RE6-Q-skXIHPNLjpEfbLMUhu9/view?usp=sharing) |
| 22 | Mae Hong Son             | 13,399.1  | 129,662   | 54.1 MB  | [link](https://drive.google.com/file/d/1GjGGtV1wYGsmvZty1BQxSJvMNwSzOwND/view?usp=sharing) |
| 23 | Maha Sarakham            | 5,827.1   | 402,219   | 168.5 MB | [link](https://drive.google.com/file/d/1YJSEavdldMdh_h_NuQ8ZHvpnSNr7mDyP/view?usp=sharing) |
| 24 | Mukdahan                 | 4,343.3   | 144,289   | 59.6 MB  | [link](https://drive.google.com/file/d/1PVkiK5uzpVVC4bO1S-UbKQbpxpXkDgwb/view?usp=sharing) |
| 25 | Nakhon Nayok             | 2,209.3   | 108,035   | 46.5 MB  | [link](https://drive.google.com/file/d/1cmHqs3imdStyz5H9TXORpdBUVjOyRUpd/view?usp=sharing) |
| 26 | Nakhon Pathom            | 2,212.0   | 334,405   | 142.5 MB | [link](https://drive.google.com/file/d/1N2CxK9fJ40gEoEl9Cvt0MZ9haRlLyuNo/view?usp=sharing) |
| 27 | Nakhon Phanom            | 5,714.0   | 287,362   | 117.2 MB | [link](https://drive.google.com/file/d/1o_CXCA6l7J6N5m9gKPXXPve1BTcRjzQh/view?usp=sharing) |
| 28 | Nakhon Ratchasima        | 21,417.5  | 1,110,461 | 518.4 MB | [link](https://drive.google.com/file/d/1SsTqTF3npPt7duIUjfD_Gcfhu05E7qWq/view?usp=sharing) |
| 29 | Nakhon Sawan             | 9,875.7   | 410,540   | 173.4 MB | [link](https://drive.google.com/file/d/1UuurjKuKVDden1T5lI3JiTaQ5SI7nj5M/view?usp=sharing) |
| 30 | Nakhon Si Thammarat      | 10,019.6  | 387,776   | 208.2 MB | [link](https://drive.google.com/file/d/1ggRPlCXRPVk_elE8tnL3NmcmWCwOMJux/view?usp=sharing) |
| 31 | Nan                      | 12,923.6  | 197,647   | 77.7 MB  | [link](https://drive.google.com/file/d/1T849wei3zsqLV_RM55i5B9JGm52OCjcN/view?usp=sharing) |
| 32 | Narathiwat               | 4,486.2   | 111,545   | 46.4 MB  | [link](https://drive.google.com/file/d/1xGKpqSmQIm41hc2zFHX97A7mAYbhG5gv/view?usp=sharing) |
| 33 | Nong Bua Lam Phu         | 4,322.4   | 224,383   | 100.2 MB | [link](https://drive.google.com/file/d/1dFevFXJ6i7fCZiTwxHxU4HWVRdICRTxo/view?usp=sharing) |
| 34 | Nong Khai                | 3,383.2   | 168,992   | 69.1 MB  | [link](https://drive.google.com/file/d/1uoEoHRk2J7UQvHHdGNxJtqDcNcj17hew/view?usp=sharing) |
| 35 | Nonthaburi               | 653.4     | 332,665   | 137.3 MB | [link](https://drive.google.com/file/d/16hbms1oUydtmi2ejWdJaoxb7db_NUwu0/view?usp=sharing) |
| 36 | Pathum Thani             | 1,562.2   | 349,838   | 146.5 MB | [link](https://drive.google.com/file/d/1s0mTkXl_bdrzN6288VrQqxljfmD-kOeS/view?usp=sharing) |
| 37 | Pattani                  | 1,964.7   | 104,361   | 42.8 MB  | [link](https://drive.google.com/file/d/1wbiCU3FtYqUzgseY6ums9c55Jgdu9Ozr/view?usp=sharing) |
| 38 | Phangnga                 | 4,043.2   | 95,958    | 39.1 MB  | [link](https://drive.google.com/file/d/1Gu9qvAgy9aJGNxc9kbyBZNZn-B5uNbXc/view?usp=sharing) |
| 39 | Phatthalung              | 3,854.2   | 185,164   | 75.9 MB  | [link](https://drive.google.com/file/d/1JfNZqXZXO8cld_dmNeB_Crx7pW1HQH7b/view?usp=sharing) |
| 40 | Phayao                   | 6,473.2   | 246,222   | 97.9 MB  | [link](https://drive.google.com/file/d/1iLOgWnc3WhfQr5xwM4M5PAWKKF4zr7QO/view?usp=sharing) |
| 41 | Phetchabun               | 12,907.2  | 415,404   | 177.5 MB | [link](https://drive.google.com/file/d/1ujK2ywsBuVJL--v3V3OrtMKNQGERfa67/view?usp=sharing) |
| 42 | Phetchaburi              | 6,340.8   | 234,298   | 110.2 MB | [link](https://drive.google.com/file/d/1qlwKoWswQIZm7VWRRwbGCT-zQcUGmJSd/view?usp=sharing) |
| 43 | Phichit                  | 4,495.5   | 194,266   | 78.7 MB  | [link](https://drive.google.com/file/d/1nAKpeaT31LfC_R7X_iwylfDrZxtn6WPi/view?usp=sharing) |
| 44 | Phitsanulok              | 11,078.1  | 356,446   | 163.6 MB | [link](https://drive.google.com/file/d/1X1RWEA31ZDouGe-e0hidNxE61pZMwCfB/view?usp=sharing) |
| 45 | Phra Nakhon Si Ayutthaya | 2,629.2   | 294,122   | 154.3 MB | [link](https://drive.google.com/file/d/1_EpW3z_an_Tjo4fi3_NNaPcTZDrpmm8t/view?usp=sharing) |
| 46 | Phrae                    | 6,815.3   | 214,598   | 84.8 MB  | [link](https://drive.google.com/file/d/1NHgmXjWBhJm5-wxAIvzXAwfEwYrpFHEr/view?usp=sharing) |
| 47 | Phuket                   | 560.6     | 131,775   | 54.3 MB  | [link](https://drive.google.com/file/d/1vKRinpClj8B8IaTDB6-o0vpKLZ6C5UYm/view?usp=sharing) |
| 48 | Prachin Buri             | 5,148.1   | 175,534   | 74.5 MB  | [link](https://drive.google.com/file/d/1HVp8FoAJJ-iNwKfrGy2x0fXU9fliUlvb/view?usp=sharing) |
| 49 | Prachuap Khiri Khan      | 6,559.3   | 240,724   | 125.7 MB | [link](https://drive.google.com/file/d/18dPb6OYa3PvMLpNqwYUrRH8H4xwEYpOM/view?usp=sharing) |
| 50 | Ranong                   | 3,181.3   | 63,712    | 25.7 MB  | [link](https://drive.google.com/file/d/1F93C2i3Ct7N6CnDV6lYzC_3glLdVgUJc/view?usp=sharing) |
| 51 | Ratchaburi               | 5,326.3   | 370,180   | 153.0 MB | [link](https://drive.google.com/file/d/1MhUj981wgeb4_PU-kt8WYqMf780lwegq/view?usp=sharing) |
| 52 | Rayong                   | 3,795.2   | 254,586   | 103.2 MB | [link](https://drive.google.com/file/d/1KVW4Xwjj5DU1BZLFOeklZ9VXf2d6N3E4/view?usp=sharing) |
| 53 | Roi Et                   | 8,117.6   | 545,990   | 211.1 MB | [link](https://drive.google.com/file/d/1gI2aun9eY4K1OJFOTsVf47NsoU8ZsRb4/view?usp=sharing) |
| 54 | Sa Kaeo                  | 7,097.8   | 219,608   | 91.0 MB  | [link](https://drive.google.com/file/d/132Fidugq1psa1QvMUyYfxYi-lJZlPgOZ/view?usp=sharing) |
| 55 | Sakon Nakhon             | 9,985.1   | 515,509   | 210.0 MB | [link](https://drive.google.com/file/d/1vZkZkUPh8VtymwMixoGhRvtYxdldVHmu/view?usp=sharing) |
| 56 | Samut Prakan             | 968.2     | 324,567   | 157.5 MB | [link](https://drive.google.com/file/d/173KhUkhnxbtJopkR6PuvCfycSjaqlSJi/view?usp=sharing) |
| 57 | Samut Sakhon             | 877.4     | 168,598   | 80.1 MB  | [link](https://drive.google.com/file/d/1V93G0XmG8ataia4FMfr2E0QORVMbjUMY/view?usp=sharing) |
| 58 | Samut Songkhram          | 417.2     | 72,208    | 33.3 MB  | [link](https://drive.google.com/file/d/1E3nn1Qdjd8j0yiRrCd2InWhk9i_o3N06/view?usp=sharing) |
| 59 | Saraburi                 | 3,683.0   | 270,249   | 114.5 MB | [link](https://drive.google.com/file/d/1_SttzNBIrauUi240IGQafokXj8F8vYHl/view?usp=sharing) |
| 60 | Satun                    | 2,710.8   | 88,409    | 35.0 MB  | [link](https://drive.google.com/file/d/18xm6GCDkAdJmKzPQSS_J8BNhyAMlmWNg/view?usp=sharing) |
| 61 | Si Sa Ket                | 9,176.6   | 572,719   | 256.2 MB | [link](https://drive.google.com/file/d/1RF82LP477AaJxPr8mZ7iZeKrh7zckKwo/view?usp=sharing) |
| 62 | Sing Buri                | 868.1     | 85,412    | 35.8 MB  | [link](https://drive.google.com/file/d/1bwEg9nHR9LkjFHMkqzbq5ISJTAp0_kCS/view?usp=sharing) |
| 63 | Songkhla                 | 7,676.4   | 348,687   | 141.6 MB | [link](https://drive.google.com/file/d/18itBrFJSe2xNRgJcYWxr2suP4Xw46_Vv/view?usp=sharing) |
| 64 | Sukhothai                | 7,014.4   | 267,899   | 120.7 MB | [link](https://drive.google.com/file/d/1a3SC4gKxqAy0Yyh1IDwePVDegVEM54sx/view?usp=sharing) |
| 65 | Suphan Buri              | 5,599.8   | 337,407   | 143.4 MB | [link](https://drive.google.com/file/d/1XALsBR5KiUVGu04Glve-oNhYpepVNC8V/view?usp=sharing) |
| 66 | Surat Thani              | 13,292.4  | 379,592   | 162.3 MB | [link](https://drive.google.com/file/d/1TTU4GVe38ynA7uVentgfBs6-EvimsR1c/view?usp=sharing) |
| 67 | Surin                    | 9,115.2   | 510,997   | 208.3 MB | [link](https://drive.google.com/file/d/1_Vh_GmtQQEm-QhVJRlAJzdJPosghWCq9/view?usp=sharing) |
| 68 | Tak                      | 17,967.6  | 284,318   | 110.7 MB | [link](https://drive.google.com/file/d/1A9579ON_Rmtm9D9o1TeaaZqaFX10I1N6/view?usp=sharing) |
| 69 | Trang                    | 4,895.8   | 191,442   | 78.6 MB  | [link](https://drive.google.com/file/d/1SA51wNOk5J_EWMroAkvJ1Qro7iWpOjRF/view?usp=sharing) |
| 70 | Trat                     | 2,924.9   | 72,816    | 29.0 MB  | [link](https://drive.google.com/file/d/1e65CyIoiZUP91tVYdLhJi5uioUhbchQQ/view?usp=sharing) |
| 71 | Ubon Ratchathani         | 16,033.4  | 836,149   | 360.6 MB | [link](https://drive.google.com/file/d/1zC3kr66uzFaOKul35voXa1h6P68zzeZc/view?usp=sharing) |
| 72 | Udon Thani               | 11,588.2  | 668,287   | 275.8 MB | [link](https://drive.google.com/file/d/1jziHVVcbuFqBUVE12H7PdefH5Ic03VMP/view?usp=sharing) |
| 73 | Uthai Thani              | 6,907.6   | 122,040   | 51.7 MB  | [link](https://drive.google.com/file/d/1qI48q9QuFlLzxPuVQJ57KG-Rp8pR-ZaV/view?usp=sharing) |
| 74 | Uttaradit                | 8,189.0   | 204,742   | 85.4 MB  | [link](https://drive.google.com/file/d/13Le8r4kDML19bZFeb6Bb5qYCCSi_ckUm/view?usp=sharing) |
| 75 | Yala                     | 4,461.9   | 107,950   | 42.8 MB  | [link](https://drive.google.com/file/d/151SPckkFEu8s95PYwKf_jPGKNQHMT6Py/view?usp=sharing) |
| 76 | Yasothon                 | 4,257.6   | 228,011   | 92.0 MB  | [link](https://drive.google.com/file/d/1haK8RU1cWpldsRP8ZlUZAaFVy9otSfSS/view?usp=sharing) |
<br/>
<br/>
