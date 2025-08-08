import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
import glob

# デフォルトのラベル設定
title_text = "セッション別 気分・満足度・幸福度の推移"
xlabel_text = "セッション"
ylabel_text = "スコア"
mood_label = "気分"
satisfaction_label = "満足度"
happiness_label = "幸福度"

# 日本語フォントの設定
def setup_japanese_font():
    """日本語フォントを設定する関数"""
    # WSL環境でよく使われる日本語フォントパス
    font_paths = [
        '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf',
        '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/truetype/noto/NotoSansCJK-Medium.ttc',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    ]
    
    # 利用可能なフォントを探す
    available_font = None
    for font_path in font_paths:
        if os.path.exists(font_path):
            available_font = font_path
            break
    
    if available_font:
        # フォントを直接指定
        font_prop = fm.FontProperties(fname=available_font)
        plt.rcParams['font.family'] = font_prop.get_name()
        print(f"使用フォント名: {font_prop.get_name()}")
        print(f"ファイルパス: {available_font}")
        return font_prop
    else:
        # フォールバック: システムフォントから日本語対応フォントを探す
        font_list = [f.name for f in fm.fontManager.ttflist]
        japanese_fonts = [f for f in font_list if any(keyword in f.lower() for keyword in ['gothic', 'mincho', 'noto', 'liberation'])]
        
        if japanese_fonts:
            plt.rcParams['font.family'] = japanese_fonts[0]
            print(f"使用フォント名: {japanese_fonts[0]}")
            print("ファイルパス: システムフォント")
            return None
        else:
            # 最後の手段: 英語フォントを使用
            plt.rcParams['font.family'] = 'DejaVu Sans'
            print("日本語フォントが見つかりません。英語のみで表示します。")
            global title_text, xlabel_text, ylabel_text, mood_label, satisfaction_label, happiness_label
            title_text = "Mood, Satisfaction, and Happiness Trends by Session"
            xlabel_text = "Session"
            ylabel_text = "Score"
            mood_label = "Mood"
            satisfaction_label = "Satisfaction"
            happiness_label = "Happiness"
            return None

# 日本語フォントを設定
font_prop = setup_japanese_font()

# データの読み込み
df = pd.read_csv('assessment_data.csv')

# グラフの作成
plt.figure(figsize=(10, 6))

# 各指標の折れ線グラフを描画
plt.plot(df['session'], df['mood'], marker='o', linewidth=2, label=mood_label, color='#FF6B6B')
plt.plot(df['session'], df['satisfaction'], marker='s', linewidth=2, label=satisfaction_label, color='#4ECDC4')
plt.plot(df['session'], df['happiness'], marker='^', linewidth=2, label=happiness_label, color='#45B7D1')

# グラフの設定（フォントプロパティを指定）
if font_prop:
    plt.title(title_text, fontsize=16, fontweight='bold', pad=20, fontproperties=font_prop)
    plt.xlabel(xlabel_text, fontsize=12, fontproperties=font_prop)
    plt.ylabel(ylabel_text, fontsize=12, fontproperties=font_prop)
    plt.legend(fontsize=11, prop=font_prop)
else:
    plt.title(title_text, fontsize=16, fontweight='bold', pad=20)
    plt.xlabel(xlabel_text, fontsize=12)
    plt.ylabel(ylabel_text, fontsize=12)
    plt.legend(fontsize=11)

plt.grid(True, alpha=0.3)

# 軸の設定
plt.xlim(0.5, len(df) + 0.5)
plt.ylim(0, 10)

# データポイントに値を表示
for i, row in df.iterrows():
    plt.annotate(f'{row["mood"]}', (row['session'], row['mood']), 
                textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    plt.annotate(f'{row["satisfaction"]}', (row['session'], row['satisfaction']), 
                textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    plt.annotate(f'{row["happiness"]}', (row['session'], row['happiness']), 
                textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# レイアウトの調整
plt.tight_layout()

# 画像として保存
plt.savefig('mood_trend_graph.png', dpi=300, bbox_inches='tight')
plt.savefig('mood_trend_graph.pdf', bbox_inches='tight')

print("グラフが正常に作成されました:")
print("- mood_trend_graph.png")
print("- mood_trend_graph.pdf")

# グラフを表示
plt.show()
