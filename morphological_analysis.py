from janome.tokenizer import Tokenizer
text = "Stackは効率的な実行を目指しスタック指向のアプローチで設計された強力なスクリプト言語なのぜ"
t = Tokenizer(wakati=True)
print(list(t.tokenize(text)))