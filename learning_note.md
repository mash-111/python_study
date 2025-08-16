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

はい、ここまでの学習内容をマークダウン形式のノートにまとめます。
Git、CLI、ファイル操作、stashなど、すべて整理しました。

---

# 学習ノート（Python + CLI + Git 初級）

## 1. CLI（コマンドライン）基本操作

### 1.1 ファイル作成

```bash
# 新規ファイル作成（上書き）
echo "Hello from Python!" > hello.py

# ファイルに追記
echo "追加のテキスト" >> hello.py
```

* `>` … 上書き
* `>>` … 追記（append）

---

### 1.2 ディレクトリ作成

```bash
mkdir project        # ディレクトリ作成
mkdir -p path/to/dir # 中間ディレクトリもまとめて作成
```

* `-p` … 中間フォルダがない場合も作成（存在してもエラーにならない）

---

## 2. Git 基礎操作

### 2.1 ブランチ操作

```bash
git branch                  # ローカルブランチ一覧
git branch -r               # リモートブランチ一覧
git checkout main           # 既存ブランチへ移動
git checkout -b feature/calc  # 新規ブランチ作成＆移動
```

* 新規ブランチは作成時点の元ブランチ内容をコピーする
* **未コミットの変更も作成先ブランチに持ち越される**

---

### 2.2 push と `-u` の意味

```bash
git push -u origin main
```

* `-u` → ローカルブランチとリモートブランチを紐付け（以降 `git push` / `git pull` だけでOK）

---

### 2.3 リモート名とブランチ名

* `origin/main` … `origin` というリモートの `main` ブランチ
* リモートブランチの確認：

```bash
git branch -r
```

---

### 2.4 fetch と pull

```bash
git fetch
```

* リモートの更新をローカルにダウンロードするだけ（作業ブランチには影響なし）

```bash
git pull
```

* `fetch` + 自分のブランチへの **merge** または **rebase**

---

## 3. マージとコンフリクト

* `git merge` は **未コミットの変更は反映しない**（コミット済みの変更だけ）
* コンフリクトがあると merge は中断され、解消して `git commit` が必要
* マージ途中で中断するには：

```bash
git merge --abort
```

---

## 4. .gitignore

```bash
# .DS_Store を無視する例
.DS_Store
```

* `.gitignore` に追加 → 新規ファイルの追跡対象から外れる
* すでに追跡中のファイルは `git rm --cached file` で追跡解除

---

## 5. git stash

### 5.1 基本

```bash
git stash          # 変更を退避してワーキングツリーをクリーンに
git stash pop      # 最新の stash を戻して削除
git stash apply    # 最新の stash を戻すが削除しない
```

### 5.2 複数 stash の管理

```bash
git stash list           # stash 一覧
git stash pop stash@{2}  # 特定 stash を戻す
```

* stash は **後入れ先出し（LIFO）** で管理される
* 古い stash を戻すとコンフリクトの可能性大

---

## 6. コミットのやり直し

### 6.1 最新コミットを修正

```bash
git commit --amend
```

* コミットメッセージやステージ内容を修正
* push 済みの場合は注意（履歴が変わる）

---

### 6.2 コミットからファイルを外す

```bash
git reset HEAD^ -- file.py   # コミットから外して unstaged に戻す
git restore --staged file.py # ステージから外すだけ
```

---

## 7. 補足

* `.DS_Store` … macOS Finder が作るフォルダ表示設定ファイル
* `git reset --soft HEAD^` … コミットだけ取り消して add 状態は残す
* `git reset HEAD^ -- file.py` … 特定ファイルだけコミットから外してワークツリーに戻す

---
