# obsws-python-settings
当リポジトリのコードを使いPythonライブラリの１つである"obsws-python"を使ってテキストソースの編集や、ソースIDなどの取得が可能です。

## はじめに
ここで公開しているコードは["obsws-python"](https://pypi.org/project/obsws-python/1.1.0/#description)内の主にset_input_settingsおよびset_scene_item_enabledの使い方についての一部です。
また、"obsws-python"と類似の機能を提供しているライブラリとして"obs-websocket-py"がありますが、後者で当リポジトリのコードは機能しないことをご留意ください。

## 環境
※動作確認は以下の環境のみ
* Python3.12.4
* obsws-python1.7.0
* OBS Studio29.1.3

## インストール

Python環境を未構築の方は[こちら](https://www.python.jp/install/windows/install.html)を参考にPython3.12.4をインストールください。

動作に必要なライブラリは以下でインストールしてください。
```bash
pip install obsws-python

# 必要があれば
pip install setuptools
```

## 使い方

#### 基本
1. .envファイルに必要な情報を入力する。
2. OBS Studioを起動しておく
3. 利用したいプログラムを実行する

#### text_settings.py
###### output_source_id
シーン内に配置されているソース(テキスト、画像など)のIDを出力します。
IDを確認したいソースを含むシーンの名前を"scene_name"に入れてプログラムを実行してください。

###### output_settings
指定したソースに入力されている設定の一覧を表示します。
調べたいソースの名前を"source_name"に入れてプログラムを実行してください。

###### change_text_display
指定したソースの表示(*True*)と非表示(*False*)を切り替えられます。
*"item_id"*と"sccene_name"にそれぞれソースIDとシーンの名前を指定してプログラムを実行してください。

###### change_text_settings
テキストソースの設定を変更することができます。
変更したいテキストの名前を"source_name"に指定し、settings内の変更したい設定の値を変更してプログラムを実行してください。
各項目の説明は以下のとおりです。

* *"font": {"size": int, "face": str}*...*size*でテキストのサイズを、*face*でフォントを変更できます。
* *"text": str*...テキストの内容を変更できます。
* *"vertical": bool*...テキストを*True*で縦書き、*False*で横書きにします。
* *"color": int*...テキストの色を*0 ~ 16777215*の値で変更できます。※
* *"opacity": int*...テキストの不透明度を*0 ~ 100*の値で変更できます。
* *"gradient": bool*...グラデーションの有無を指定できます。
* *"gradient_color": int*...グラデーションの色を*0 ~ 16777215*の値で変更できます。※
* *"bk_color": int*:...テキストの背景色を*0 ~ 16777215*の値で変更できます。※
* *"bk_opacity": int*:...テキストの背景色の不透明度を*0 ~ 100*の値で変更できます。
* *"align": str*...水平方向の位置揃えを*left, center, right*で指定できます。
* *"valign": str*...垂直方向の位置揃えを*top, center, bottom*で指定できます。
* *"outline": bool*"...テキストの輪郭線の有無を指定できます。
* *"outline"_size*: int"...輪郭線の太さを指定できます。
* *"outline"_color*: int...輪郭線の色を*0 ~ 16777215*の値で変更できます。※
* *"outline"_opacity*: int*...輪郭線の透明度を*0 ~ 100*の値で変更できます。

※ 色の値の指定には下記の利用を推奨します

#### color_code_converter.py
プログラムを実行するとコンソール上で変換したいカラーコードを求められるので入力してください。
実行結果として得られた整数値を"change_text_settings"の*settings*にある色の値として入力すれば、指定の色が反映されます。

## 機能
* OBS　Studioのシーン内にあるソースIDの取得
* OBS Studioのソースに含まれる設定情報の取得
* OBS Studioのテキストソースの設定変更
* 16進数のカラーコードをOBS Studioに適した形式で10進数に変換

## FAQ
#### .envに入力する情報がわからない
各項目の設定方法は[YGPuzzleGTANT](https://x.com/roiyaruRIZ)氏の[こちらの記事](https://note.com/213414)を参照ください。

#### 他の設定も行いたい
当リポジトリで公開しているコードはOBS Studioの、主にテキストソースの設定変更をする操作の一部です。
他の部分の操作については["obsws-python"](https://pypi.org/project/obsws-python/1.1.0/#description)の説明、またはOBS Studioにて「ファイル」>「設定フォルダを表示」>「basic」>「scenes」より当該シーンのjsonファイルから、変更したい設定を確認してください。

##### その他
上記でも解決できない、または上記にはない問題が発生した際にはお手数ですが[*Issues*](https://github.com/t4ned4/create-aituber/issues)を残していただくか、taneda.bp@gmail.comまでご連絡ください。

#### ライセンス

当リポジトリのコードは"obsws-python"のライセンスに基づき、
GPLライセンスの下で公開しています。

*Copyright (c) 2024 t4ned4*

*This program is free software; you can redistribute it and/or*
*modify it under the terms of the GNU General Public License*
*as published by the Free Software Foundation; either version 2*
*of the License, or any later version.*

*This program is distributed in the hope that it will be useful,*
*but WITHOUT ANY WARRANTY; without even the implied warranty of*
*MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the*
*GNU General Public License for more details.*

*You should have received a copy of the GNU General Public License*
*along with this program. If not, see http://www.gnu.org/licenses/.*
