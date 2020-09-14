# -*- coding: UTF-8 -*-

# 日常生活的心理測驗
# https://kac0813.pixnet.net/blog/post/38597221

score = 0

answer = input("""
1.花瓶重重摔在地上，破成碎片，你覺得看到這情景的人會說什麼？
(A) 哎呀！這麼貴的花瓶！
(B) 唉！已經打破了，也是無可奈何的事。
(C) 為了避免有人受傷，還是趕怪把碎片收拾乾淨。
答案：""")

if (answer.upper() == 'A'):
    score += 3
if (answer.upper() == 'B'):
    score += 1
if (answer.upper() == 'C'):
    score += 4

answer = input("""
2.當一件重要的事做失敗，遭到重大打擊時，你會如何？
(A) 就像呼吸快停止般，胸口苦悶。
(B) 腦袋一片空白，什麼辦法也想不出來。
(C) 難受得想吐，心情壞到極點。
答案：""")

if (answer.upper() == 'A'):
    score += 3
if (answer.upper() == 'B'):
    score += 4
if (answer.upper() == 'C'):
    score += 1

answer = input("""
3.晚上鑽到被窩裡後，在還沒睡著前，心中常會想哪些事？
(A) 第二天的事，或此後計畫作的事。
(B) 今天一天發生的事，以及過去的事。
(C) 淨想些與現實脫節的事。
答案：""")

if (answer.upper() == 'A'):
    score += 4
if (answer.upper() == 'B'):
    score += 2
if (answer.upper() == 'C'):
    score += 3

answer = input("""
4.小孩在海邊逐浪嬉戲，突然發出一聲尖叫，你認為他叫些什麼？
(A) 哇！可怕！
(B) 哇！水好冰！
(C) 哇！好好玩！
答案：""")

if (answer.upper() == 'A'):
    score += 4
if (answer.upper() == 'B'):
    score += 3
if (answer.upper() == 'C'):
    score += 2

answer = input("""
5.當你想去看一部以恐怖聞名的電影時，你會跟誰一起去？
(A) 一個人去。
(B) 和男友一起去。
(C) 和女性朋友一起去。
答案：""")

if (answer.upper() == 'A'):
    score += 1
if (answer.upper() == 'B'):
    score += 3
if (answer.upper() == 'C'):
    score += 2

answer = input("""
6.一個路人在路上發現了一只不曉得裝了什麼東西的箱子，你覺得那個人會怎麼做？
(A) 心裡雖覺得裡面可能裝有炸彈，卻仍往箱子走近。
(B) 覺得心裡毛毛的，便避開繞路而過。
(C) 因為擔心車子經過會造成危險，便移開它。
答案：""")

if (answer.upper() == 'A'):
    score += 1
if (answer.upper() == 'B'):
    score += 4
if (answer.upper() == 'C'):
    score += 2

answer = input("""
7.你認為哪一個季節最適合邂逅理想的情人？
(A) 陽光燦爛的盛夏季節。
(B) 落葉飛舞的深秋。
(C) 花兒初開的早春。
答案：""")

if (answer.upper() == 'A'):
    score += 1
if (answer.upper() == 'B'):
    score += 3
if (answer.upper() == 'C'):
    score += 4

answer = input("""
8.你覺得剛從土中抽芽的植物，將來會變成什麼？
(A) 開出美麗的花朵。
(B) 結出許多果實。
(C) 長出繁密、茂盛的樹葉。
答案：""")

if (answer.upper() == 'A'):
    score += 3
if (answer.upper() == 'B'):
    score += 1
if (answer.upper() == 'C'):
    score += 2

answer = input("""
9.你和朋友打算聚餐，如果下列餐廳的價錢都一樣，你會選擇哪一種？
(A) 選擇多，沒有特定料理的自助餐。
(B) 附帶甜點的日式定食。
(C) 附沙拉、飲料的義大利麵。
答案：""")

if (answer.upper() == 'A'):
    score += 1
if (answer.upper() == 'B'):
    score += 4
if (answer.upper() == 'C'):
    score += 2

answer = input("""
10.當你趕著往巴士站跑時，卻發現巴士不等你就開走了，這時你會怎麼想？
(A) 如果早一點出門就好了。
(B) 為什麼就不能等我一下？
(C) 真令人生氣！
答案：""")

if (answer.upper() == 'A'):
    score += 2
if (answer.upper() == 'B'):
    score += 3
if (answer.upper() == 'C'):
    score += 1

if (score > 30):
    print("""
    A類型：

    你沒有辦法跟那種強人所難、易怒、過度拘泥小節的異性交往
    ，你比較適合胸襟寬大、個性沈穩、單純和樸素的人。
    """)

if (score >= 25 and score <= 30):
    print("""
    B類型：

    你沒有辦法忍受那種粗線條的人，你喜歡的是自我意識強，較
    有個性的人;比如說，他會執著於某些事，對異性的喜好也能充
    分理解。另外，也是重視用餐或約會等氣氛的人。
    """)

if (score >= 18 and score <= 24):
    print("""
    C類型：

    自我要求嚴格的你，喜歡的類型是跟你一樣態度誠實的人，而
    且你希望能對任何人都很親切，且待人熱誠。
    """)

if (score < 17):
    print("""
    D類型：

    由於你是怕受傷的類型，因此，你較適合的是擁有纖細性格，
    對文學、藝術有相當素養，對電影和小說也有興趣的異性。這
    種異性才能瞭解你易感、脆弱的心靈。
    """)

