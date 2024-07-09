## fib_api について

指定した n 番目のフィボナッチ数を返す REST API を作成した．

<br>

## 使用方法

以下の URL にアクセスする．

https://fib-api-9n1v.onrender.com/fib

クエリパラメータに n(取得したいフィボナッチ数の番号：1 以上の整数)を指定する．

デプロイは [Render.com](https://render.com/)で行った．Render.comのフリープランの仕様上，非アクティブ状態が15分続くと停止状態になる.停止状態からリクエストを送ると再度起動するが，応答までに時間がかかる(2分程度)．

### 【例】99 番目のフィボナッチ数を取得する場合

#### ① URL から呼び出す場合

IN：

https://fib-api-9n1v.onrender.com/fib?n=99

OUT:

```
{
  "result":218922995834555169026
}
```

#### ② curl コマンドを使用して呼び出す場合

IN：

```
curl -X GET -H "Content-Type: application/json" "https://fib-api-9n1v.onrender.com/fib?n=99"
```

OUT:

```
{
  "result":218922995834555169026
}
```

<br>

## 使用言語とライブラリ

Python 3.11.9

`FastAPI`
Python で Web API を構築するためのフレームワーク．

`Uvicorn`
Python 用の ASGI(Asynchronous Server Gateway Interface) Web サーバ．

`pytest`
Python 用に設計されたユニットテストを自動化するフレームワーク．

<br>

## ファイル構成

```
.
├── README.md
├── app
│   ├── __init__.py（ディレクトリをパッケージとして認識させるためのファイル）
│   ├── fibonacci.py（n番目のフィボナッチ数を計算）
│   ├── main.py（インスタンスの生成，モデル・エンドポイントの定義）
│   └── test
│       ├── __init__.py（ディレクトリをパッケージとして認識させるためのファイル）
│       └── test_main.py（ユニットテストを行う）
└── requirements.txt（使用するライブラリの一覧）
```
