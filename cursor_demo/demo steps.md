# キャリア支援AI活用デモ手順

## ケース情報の管理

### 1. 出典の紹介
case_file_example/小栗 工藤 2019 立教大学臨床心理学研究.pdf

### 2. 匿名化済みprofileの整形【エージェント】

**プロンプト**:
```
case_file_example/00_profile.md
はキャリア相談のケースのプロフィール情報のメモです。資料として見やすいようにマークダウンのフォーマットを整形して。
である調で、必要に応じて箇条書きも使って。内容は削らないで。
```

### 3. ケースメモの整理【エージェント】

**プロンプト**:
```
case_file_example/01_session1.md
はキャリア相談の面談メモです。概要を整理してください。必要に応じて箇条書きを使用して。最後に、冒頭に要点の
まとめを追加して。
```

### 4. yzane.markdown‑pdf のインストール
- Serch Extensions in Marketplace: "Markdown PDF"
- **マークダウンのプレビュー**: `Shift + Ctrl + v`
- **PDF出力**: `F1` → `markdown‑pdf: Export (pdf)` → サイドバー再読み込み

### 5. これまでの経過の確認【エージェント】

**プロンプト**:
```
case_file_example
のsession 1 ～ 3 の.mdファイルを確認してこのケースのクライアントのプロフィールとこれまでの対応の概要を示して。
それを同じフォルダに概要.mdとして保存して。
```


## ブログ執筆

### 1. 情報収集（ChatGPT）

### 2. 下書き保存

キャリア支援で使えるAI_下書き.txt

### 3. ブログ用マークダウンに書き換え【エージェント】

**プロンプト**:
```
このファイルはブログ記事の下書き。ブログ記事としてマークダウンの形式を整えて、.mdファイルで保存して
blog_writing/キャリア支援で使えるAI_下書き.txt
```

### 4. はてなブログにコピペ

- マークダウン形式にするのを忘れずに
- https://blog.hatena.ne.jp/psyai-consulting/psyai-consulting.hatenablog.jp/

### 5. ブログ記事の修正【エージェント】

**プロンプト**:
```
blog_writing/キャリア支援で使えるAI_下書き.md
の最後に新しいセクションを追加して、下記の内容を入れて。

Github＋Cursorの活用
① ケース管理・記録業務の自動化
代表的な OSS／事例
Open Case Management (OCM)
NPO 法務支援向けに作られた汎用ケース管理 OSS。クライアント情報・進捗・添付ファイルを Web UI で扱える構成になっており、質問項目を YAML で定義できるので、Cursor に
"intake_form.yaml の Legal Issue を Career Concern に書き換えて"
のように指示するだけで面談票をキャリア相談用に一括変換できます。
https://github.com/aworley/ocm?utm_source=chatgpt.com

Family Promise Case Management
ホームレス支援団体 Family Promise が作ったケース管理アプリ。Spring Boot＋PostgreSQL の構成で、デプロイ知識がなくても Docker-Compose が同梱されているため、Cursor で

"docker-compose.yml のポート番号を 8080→9090 に"
といった環境調整だけで動作確認→GitHub へ PR が可能です。
https://github.com/brianjknight/Family-Promise-Case-Management?utm_source=chatgpt.com

ArkCase Case Management（デモ動画）
政府系も採用する OSS。動画内ではフォーム追加や権限設定を GUI で変更する様子が紹介されており、「フォーム雛形をエクスポート→GitHub でバージョン管理→Cursor で一括編集」という流れの参考になります。
https://www.youtube.com/watch?v=rP0EPKzzsTI&utm_source=chatgpt.com

活用のコツ
記録様式（Markdown／YAML）を GitHub でバージョン管理 → 誰がどこを変えたか履歴が残る
Cursor の自然言語置換で複数ファイルを一度に更新し、テンプレ誤配布を防止

② データ分析・エビデンスベース実践
代表的な OSS／事例
Therapist Recommender
面談ログ（テキスト）を NLP でトピック分類し、相性の良いセラピストを推薦する研究コード。自組織の匿名化データを input.csv に差し替え、Cursor に
"手元の csv に合わせて列名を mapping し直して"
と依頼すれば、数行の修正で自前データに適用できます。
https://github.com/camerongridley/TherapistRecommender?utm_source=chatgpt.com

Log Analyzer Script (Python)
一般ログ解析用のスクリプトですが、面談記録 CSV を指定して「就職内定・未内定でフィルタ→月次推移をグラフ化」といった処理を追加する改造例が多く報告されています。Cursor で関数化→コミットまで 1 コマンド。
https://github.com/silvermete0r/logs_analyzer_script_py?utm_source=chatgpt.com

Career Analyzer
キャリア満足度を測り「転職リスク」を可視化する CLI ツール。スクリプト内の質問項目や重み付けを Cursor に自然言語で編集させ、エビデンス指標を面談前後で比較する用途に転用され始めています。
https://github.com/emidombek/career-analyzer?utm_source=chatgpt.com

活用のコツ
分析コードを PR レビュー → 統計手法の妥当性チェックをチーム文化に
結果グラフやレポートも Markdown で同じリポジトリに置き、Evidence-Based Practice (EBP) を継続的にアップデート

③ プロンプト＆教材の共有知化
代表的な OSS／事例
Awesome-ChatGPT-Prompts
世界最大級のプロンプト集。"Act as a Motivational Coach" など動機づけ面談に流用できるサンプルが豊富で、「自分用バージョン」をフォーク→Cursor で翻訳や事例追加→PR 共有する流れが一般的です。
https://github.com/f/awesome-chatgpt-prompts?utm_source=chatgpt.com

ChatGPT System Prompts – Career Counselor
キャリアカウンセラー用のベースプロンプトを単独ファイルで提供。Pull Request で「学生／転職者／管理職向け」のバリエーションを差分管理しやすい構成になっています。
https://github.com/mustvlad/ChatGPT-System-Prompts/blob/main/prompts/educational/career-counselor.md?utm_source=chatgpt.com

Prompt-Library
"自己紹介スニペットを動的に差し込む" 手法を解説しながらプロンプトを収集しているリポジトリ。Cursor で YAML 設定を一括生成し、活用例と成果を Issues に残す事例報告が増えています。
https://github.com/danielrosehill/Prompt-Library?utm_source=chatgpt.com

活用のコツ
プロンプトを Markdown＋Pull Request で共有すれば、著作権・バイアスレビューも履歴管理
Cursor の multi-file search で「〇〇法」「STAR 法」などキーワード検索→該当プロンプトを即編集
```

### 6. Githubへのコミット【エージェント】

- git hubとつながっている前提
- `git add ., commit, push`

**確認**: https://github.com/keitakiuchi/career_consul_AI_demo

## OSS（オープンソースソフトウェア）の活用

### 1. career-analyzer

https://github.com/emidombek/career-analyzer?utm_source=chatgpt.com

- リポジトリのクローン→cursorで開く

https://psyai-consulting.hatenablog.jp/entry/2025/07/24/141410

## データ集計とレポートを自分で

### 1. データセット作成【エージェント】

適当にアセスメント結果を追加（session 2, 3には追加済み）
---
## アセスメント
気分：3
満足度：2
幸福度：1


---

**プロンプト**:
```
case_file_example
内のsession1.md, 2.md, 3.mdから、アセスメントの結果をそれぞれ読み込んで、
data_report_example
内にassessment_data.csvとしてデータセットを作成して
```

### 2. グラフの作成【エージェント】

**プロンプト**:
```
グラフを作成したい。
data_report_example/assessment_data.csv
のデータを使って、気分、満足度、幸福度の推移を1つの折れ線グラフにして
コードはpythonで書いて同じフォルダ内に保存。結果は画像ファイル（assessment_trends.png）で同じフォルダ内に保存。日本語フォントが使えるようにして。
```

**追加プロンプト**:
```
日本語が豆腐にならないよう、フォント名ではなくフォントファイルのパスから直接登録してください。
WSL/Linux 前提。/usr/share/fonts/... を再帰探索し、存在する日本語フォント（IPAex/IPA/Takao など）をglob で検索→最初に見つかった候補を使用。
matplotlib.font_manager.addfont(path) と FontProperties(fname=path).get_name() を使って登録・設定。
plt.rcParams["font.family"] に取得した実フォント名を設定し、axes.unicode_minus=False、pdf.fonttype=42、ps.fonttype=42 を必ず指定。
見つからなければ英語ラベルにフォールバック。
コンソールに 「使用フォント名」と「ファイルパス」 を必ず print。
既存のラベルや描画処理は変更しないこと。ファイル名は変えない。
```
※これはGPT-5も使いつつ、何度か試行錯誤してたどり着きました...

### 3. レポート作成【エージェント】

**プロンプト**:
```
case_file_example
内のsession1.md, 2.md, 3.md内の記述の情報と
data_report_example/assessment_trend.png
を使って、レポートを作成して。出力はdata_report_example内に、.mdファイルで。グラフの画像（assessment_trend.png）を必ず入れて。
```

**注意**: 今回はゼロから作らせたが、フォーマットを指定すれば、それに合わせて作成可能。ただし、マークダウンやLaTexのフォーマットが望ましい。

### 4. PDF出力

`F1` → `markdown‑pdf: Export (pdf)`

