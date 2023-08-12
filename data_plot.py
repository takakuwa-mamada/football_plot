import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import random

game_id = 1

if game_id == 1:
    n = 636
    
elif game_id == 2:
    n = 636


for i in range(1, 2):
    # トラッキングデータを読み込む
    data = pd.read_csv('/Users/jungbang1014/高専/ゼミ/卒業研究/data-science/sam/modified_data/game%d/output_file_%d.csv' % (game_id,i)) 

    # サッカーコートを描画する関数
    def draw_soccer_field():
        fig, ax = plt.subplots()

        # ゴールライン、タッチライン
        ax.plot([0, 0], [0, 68], color="black")
        ax.plot([0, 106], [68, 68], color="black")
        ax.plot([106, 106], [68, 0], color="black")
        ax.plot([106, 0], [0, 0], color="black")

        # センターライン
        ax.plot([53, 53], [0, 68], color="black")

        # 軸設定
        ax.set_aspect('equal')
        ax.set_xlim(0, 106)
        ax.set_ylim(0, 68)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        #ax.set_title('Soccer Field')

        return ax

    # プロット用のサブプロットを作成
    ax = draw_soccer_field()

    # プレイヤーの動きをプロット
    players = data['From'].unique()
    for player in players:
        player_data = data[data['From'] == player]
        ax.plot(player_data['Start X'], player_data['Start Y'], marker='o', label=player)

    # パスの軌跡をプロット
    passes = data[data['Type'] == 'PASS']
    for i, row in passes.iterrows():
        ax.plot([row['Start X'], row['End X']], [row['Start Y'], row['End Y']], 'b-')
    
    # プロットの設定
    ax.legend()
    # グラフを表示
    plt.show()