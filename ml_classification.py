import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np # エラー回避のためにnumpyもインポート

def run_ml_workflow():
    """
    Day 4の課題である、タイタニックデータセットを用いた
    ロジスティック回帰モデルの訓練、評価を実行します。
    """
    # --- 1. データの読み込みと前処理 ---
    
    # train.csv を読み込みます
    try:
        df = pd.read_csv('train.csv')
    except FileNotFoundError:
        print("Error: train.csv not found. Please place it in the same directory.")
        return

    # a. Sex（性別）を数値に変換（女性=1, 男性=0）
    df['Sex'] = df['Sex'].map({'female': 1, 'male': 0})

    # b. Age（年齢）の欠損値を中央値で補完
    median_age = df['Age'].median()
    df['Age'].fillna(median_age, inplace=True)
    
    # c. 欠損値のある行の削除（今回は Embarked の欠損値を安全のために削除）
    df.dropna(subset=['Embarked'], inplace=True) 

    # --- 2. 特徴量 (X) と目的変数 (y) の定義 ---
    
    # 目的変数: Survived (生存フラグ)
    y = df['Survived']
    
    # 特徴量: Pclass, Fare, Age, Sex の4つを使用
    features = ['Pclass', 'Fare', 'Age', 'Sex']
    X = df[features]
    
    # --- 3. データの分割 (Train/Test Split) ---
    
    # 80%を訓練用、20%をテスト用に分割 (random_state=42 で結果を再現可能にします)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- 4. モデルの訓練と評価 ---
    
    # ロジスティック回帰モデルのインスタンス化と訓練
    # Max_iter を増やすことで収束しない警告を回避します
    model = LogisticRegression(max_iter=200) 
    model.fit(X_train, y_train) 

    # 精度（Accuracy）の算出と出力
    accuracy = model.score(X_test, y_test)

    print("-" * 40)
    print(f"特徴量: {features}")
    print(f"訓練データ数: {len(X_train)}")
    print(f"テストデータ数: {len(X_test)}")
    print(f"ロジスティック回帰モデルの予測精度: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("-" * 40)

if __name__ == "__main__":
    # mainブロックで関数を実行
    run_ml_workflow()