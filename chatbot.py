# =============================================================
# ライブラリ＆API認証情報
# =============================================================

import openai

openai.organization = "org-T7FVnXlxf9eTSNjdvniFtP7n"
openai.api_key = "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"


# =============================================================
# チャットボット関数
# =============================================================

def Ask_ChatGPT(message):
    # 応答設定
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # モデルを選択
        messages=[
            {"role": "user", "content": message,},
            {"role": "system", "content": "あなたは就職支援を行うメンターです。はいかいいえで答えられる質問をいくつかして質問者にいいアイデアを上げてください",}
        ],

        max_tokens=1024,  # 生成する文章の最大単語数
        n=1,  # いくつの返答を生成するか
        stop=None,  # 指定した単語が出現した場合、文章生成を打ち切る
        temperature=1.0,  # 出力する単語のランダム性（0から2の範囲） 0であれば毎回返答内容固定
    )

    # 応答
    response = completion.choices[0].message.content

    # 応答内容出力
    return response


# =============================================================
# チャットボット実行
# =============================================================

# 質問内容
message = "転職活動に困っています。何から始めたら良いですか？"

# ChatGPT起動
res = Ask_ChatGPT(message)

# 出力
print(res)
