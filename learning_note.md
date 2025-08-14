# **学習ノート Day 1（2025-08-14）**

## **今日の目標**

* ターミナル（CLI）でファイル作成・操作に慣れる
* GitHubへのPush方法を理解する
* SSH経由でPushできるようにする
* Pythonの簡単なスクリプトを実行する

---

## **1. CLI（ターミナル）操作**

### 基本コマンド

| コマンド                         | 説明                     |
| ---------------------------- | ---------------------- |
| `pwd`                        | 現在のフォルダを確認             |
| `ls`                         | フォルダ内のファイルを表示          |
| `cd <フォルダ名>`                 | フォルダ移動                 |
| `mkdir <フォルダ名>`              | フォルダ作成                 |
| `touch <ファイル名>`              | 空ファイル作成                |
| `rm <ファイル>`                  | ファイル削除                 |
| `rm -r <フォルダ>`               | フォルダごと削除               |
| `echo '文字列' > ファイル名`         | ファイル作成・書き込み（ターミナルから直接） |
| `cat << EOF > ファイル名 ... EOF` | 複数行ファイル作成              |

### 注意

* `echo "文字列"` で `dquote>` が出た場合は、クオートが閉じていない状態
* `Ctrl + C` でキャンセルし、正しいクオートで再入力

---

## **2. Python 基礎**

### 1行スクリプト例

```python
# hello.py
print("Hello from Python!")
```

* 実行コマンド：

```bash
python3 hello.py
```

* 出力：

```
Hello from Python!
```

---

## **3. Git & GitHub 基礎**

### SSH設定

1. SSHキー作成

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

2. 公開鍵コピー

```bash
cat ~/.ssh/id_ed25519.pub
```

3. GitHubに登録（Settings → SSH and GPG keys → New SSH key）

### リモート登録

```bash
git remote add origin git@github.com:username/python_study.git
```

---

### Git操作の流れ

```bash
git init                   # リポジトリ初期化
git add hello.py           # ステージに追加
git commit -m "First commit" # コミット
git branch -M main         # ローカルブランチ名を main に変更
git push -u origin main    # 初回Push（-uで紐付け）
```

#### ポイント

* `-M` → ブランチ名を強制変更、リモートと名前を揃えるため
* `-u` → ローカルとリモートを紐付ける。初回Pushのみ必要、次回からは `git push` だけでOK
* SSHならパスワード不要でPushできる

---

## **4. 振り返りテスト（今日の内容確認）**

1. ターミナルで今いるフォルダを確認するコマンドは？
2. ターミナルで直接ファイルに「Hello from Python!」と書き込むコマンドは？
3. ローカルGitブランチを `main` に変更するコマンドは？
4. SSHで初回Pushするコマンドは？

---

## **5. 今日のまとめ**

* CLI操作とPythonファイル作成の基本を理解
* GitHubにSSHでPushする方法を体験
* 今後のブランチ操作や共同開発の準備完了

---

💡 次回の学習予告：

* Python：変数・計算・文字列操作
* CLI：フォルダ検索・ファイル中身検索
* Git：変更確認（`git status` / `git diff`）、ブランチ作成

---