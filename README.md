# Python QR Code Generator

このプロジェクトは、ユーザーが入力したテキストからQRコードを生成し、それを表示またはPNGファイルとして保存するシンプルなPythonアプリケーションです。GUIはTkinterを使用して作成されており、任意のテキストを入力してQRコードを即座に生成できます。

## 主な機能

- テキスト入力によるQRコードの動的生成
- 生成されたQRコードのGUI上での表示
- 生成されたQRコードのPNGファイルとしての保存

## セットアップ方法

このプロジェクトを使用するには、Pythonと必要なパッケージをインストールする必要があります。以下の手順に従ってください。

1. リポジトリをクローンする

```bash
git clone https://github.com/velaciela-ringWing2007/PythonQRCodeGenerator.git
```

2. 必要なパッケージをインストールする

```bash
pip install qrcode[pil]
```

png保存するのでpillowを同時に院スコールするために、[pil]で一緒にinstallするらしい。

## 使用方法

1. アプリケーションを実行します。

```bash
python qr_code_generator.py
```

Lets Enjooooy