#質問を画面に表示
print("これから無人島でしばらく一人で生活しなくてはなりません。")
print("好きなものを一つだけ持って行くとしたら何を持って行く?")
print("1: ナイフ")
print("2: 携帯電話")
print("3: 漫画")

#ユーザーから回答を入力
s = input("答えは?")
i = int(s)

#無効な答えかどうかを調べる
if i < 1:
    print("範囲外")
    quit()
if i > 3:
    print("範囲外")
    quit()

#答えを表示
print("\n------\n")
print("無人島生活から、将来の恋人について分かります。")
if i == 1:
    print("現実的な道具を選んだあなたは..")
    print("現実的な身の丈にあった相手を選ぶでしょう")
elif i == 2:
    print("誰かとつながる道具を選んだあなたは..")
    print("話し好きな賑やかな相手が相応しいでしょう。")
elif i == 3:
    print("実用よりも娯楽アイテムを選んだあなたは..")
    print("夢見がちなので、理想がとても高いでしょう。")