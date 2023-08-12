import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

game_id = 1

def plot_pitch( field_dimen = (106.0,68.0), field_color ='white', linewidth=2, markersize=20):
    fig,ax = plt.subplots(figsize=(12,8)) # create a figure 
    # decide what color we want the field to be. Default is green, but can also choose white
    if field_color=='green':
        ax.set_facecolor('white')
        lc = 'whitesmoke' # line color
        pc = 'w' # 'spot' colors
    elif field_color=='white':
        lc = 'k'
        pc = 'k'
    # ALL DIMENSIONS IN 
    border_dimen = (3,3) # include a border arround of the field of width 3m
    meters_per_yard = 0.9144 # unit conversion from yards to meters
    half_pitch_length = field_dimen[0]/2. # length of half pitch
    half_pitch_width = field_dimen[1]/2. # width of half pitch
    signs = [-1,1] 
    # Soccer field dimensions typically defined in yards, so we need to convert to meters
    goal_line_width = 8*meters_per_yard
    box_width = 20*meters_per_yard
    box_length = 6*meters_per_yard
    area_width = 44*meters_per_yard
    area_length = 18*meters_per_yard
    penalty_spot = 12*meters_per_yard
    corner_radius = 1*meters_per_yard
    D_length = 8*meters_per_yard
    D_radius = 10*meters_per_yard
    D_pos = 12*meters_per_yard
    centre_circle_radius = 10*meters_per_yard
    # plot half way line # center circle
    ax.plot([0,0],[-half_pitch_width,half_pitch_width],lc,linewidth=linewidth)
    ax.scatter(0.0,0.0,marker='o',facecolor=lc,linewidth=0,s=markersize)
    y = np.linspace(-1,1,50)*centre_circle_radius
    x = np.sqrt(centre_circle_radius**2-y**2)
    ax.plot(x,y,lc,linewidth=linewidth)
    ax.plot(-x,y,lc,linewidth=linewidth)
    for s in signs: # plots each line seperately
        # plot pitch boundary
        ax.plot([-half_pitch_length,half_pitch_length],[s*half_pitch_width,s*half_pitch_width],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length],[-half_pitch_width,half_pitch_width],lc,linewidth=linewidth)
        # goal posts & line
        ax.plot( [s*half_pitch_length,s*half_pitch_length],[-goal_line_width/2.,goal_line_width/2.],pc+'s',markersize=6*markersize/20.,linewidth=linewidth)
        # 6 yard box
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*box_length],[box_width/2.,box_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*box_length],[-box_width/2.,-box_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length-s*box_length,s*half_pitch_length-s*box_length],[-box_width/2.,box_width/2.],lc,linewidth=linewidth)
        # penalty area
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*area_length],[area_width/2.,area_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*area_length],[-area_width/2.,-area_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length-s*area_length,s*half_pitch_length-s*area_length],[-area_width/2.,area_width/2.],lc,linewidth=linewidth)
        # penalty spot
        ax.scatter(s*half_pitch_length-s*penalty_spot,0.0,marker='o',facecolor=lc,linewidth=0,s=markersize)
        # corner flags
        y = np.linspace(0,1,50)*corner_radius
        x = np.sqrt(corner_radius**2-y**2)
        ax.plot(s*half_pitch_length-s*x,-half_pitch_width+y,lc,linewidth=linewidth)
        ax.plot(s*half_pitch_length-s*x,half_pitch_width-y,lc,linewidth=linewidth)
        # draw the D
        y = np.linspace(-1,1,50)*D_length # D_length is the chord of the circle that defines the D
        x = np.sqrt(D_radius**2-y**2)+D_pos
        ax.plot(s*half_pitch_length-s*x,y,lc,linewidth=linewidth)
        
    # remove axis labels and ticks
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    # set axis limits
    xmax = field_dimen[0]/2. + border_dimen[0]
    ymax = field_dimen[1]/2. + border_dimen[1]
    ax.set_xlim([-xmax,xmax])
    ax.set_ylim([-ymax,ymax])
    ax.set_axisbelow(True)
    
    return fig,ax

def plot(DATADIR, game_id):
    events = pd.read_csv(DATADIR)
    q = 1
    with open(DATADIR, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            # 指定した文字列が見つかったらデータを保存し、リストを初期化する
            if target_string not in row['Ball']:
                fig, ax = plot_pitch()
                #ホーム
                ax.plot(data2['Home_1_x'].iloc[q], data2['Home_1_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_2_x'].iloc[q], data2['Home_2_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_3_x'].iloc[q], data2['Home_3_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_4_x'].iloc[q], data2['Home_4_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_5_x'].iloc[q], data2['Home_5_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_6_x'].iloc[q], data2['Home_6_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_7_x'].iloc[q], data2['Home_7_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_8_x'].iloc[q], data2['Home_8_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_9_x'].iloc[q], data2['Home_9_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_10_x'].iloc[q], data2['Home_10_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['Home_11_x'].iloc[q], data2['Home_11_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
                ax.plot(data2['ball_x'].iloc[q], data2['ball_y'].iloc[q], 'ko', markersize=10,alpha=0.5)

                #アウェイ
                ax.plot(data1['Away_15_x'].iloc[q], data1['Away_15_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_16_x'].iloc[q], data1['Away_16_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_17_x'].iloc[q], data1['Away_17_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_18_x'].iloc[q], data1['Away_18_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_19_x'].iloc[q], data1['Away_19_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_20_x'].iloc[q], data1['Away_20_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_21_x'].iloc[q], data1['Away_21_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_22_x'].iloc[q], data1['Away_22_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_23_x'].iloc[q], data1['Away_23_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_24_x'].iloc[q], data1['Away_24_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['Away_25_x'].iloc[q], data1['Away_25_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
                ax.plot(data1['ball_x'].iloc[q], data1['ball_y'].iloc[q], 'ko', markersize=10,alpha=0.5)
                plt.savefig(f'/Users/jungbang1014/高専/ゼミ/卒業研究/data-science/sam/isolate_data/game2/tracking_base_away/{q}/plot{q}.png')
                q += 1
    

def isolate_plot_event_data(DATADIR,game_id):
    min_frame = []
    max_frame = []
    if game_id == 1:
        n = 86
    elif game_id == 2:
        n = 86
    for i in range(15,n): #ここの数字で区切りが選べる
        eventfile = 'game%d/events/output_file_%d.csv' % (game_id,i) # filename
        events = pd.read_csv('{}/{}'.format(DATADIR, eventfile)) # read data
        min_frame = events['End Frame'].min()
        max_frame = events['End Frame'].max()
        for q in range(min_frame, max_frame+1):
            fig, ax = plot_pitch()
            
            #textstring = events['Type'] + ': ' + events['From']
            #ax.text( events['Start X'], events['Start Y'], textstring, fontsize=10, color="k")
            #ホーム
            ax.plot(data2['Home_1_x'].iloc[q], data2['Home_1_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_2_x'].iloc[q], data2['Home_2_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_3_x'].iloc[q], data2['Home_3_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_4_x'].iloc[q], data2['Home_4_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_5_x'].iloc[q], data2['Home_5_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_6_x'].iloc[q], data2['Home_6_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_7_x'].iloc[q], data2['Home_7_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_8_x'].iloc[q], data2['Home_8_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_9_x'].iloc[q], data2['Home_9_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_10_x'].iloc[q], data2['Home_10_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['Home_11_x'].iloc[q], data2['Home_11_y'].iloc[q], 'bo', markersize=10,alpha=0.5)
            ax.plot(data2['ball_x'].iloc[q], data2['ball_y'].iloc[q], 'ko', markersize=10,alpha=0.5)

            #アウェイ
            ax.plot(data1['Away_15_x'].iloc[q], data1['Away_15_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_16_x'].iloc[q], data1['Away_16_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_17_x'].iloc[q], data1['Away_17_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_18_x'].iloc[q], data1['Away_18_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_19_x'].iloc[q], data1['Away_19_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_20_x'].iloc[q], data1['Away_20_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_21_x'].iloc[q], data1['Away_21_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_22_x'].iloc[q], data1['Away_22_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_23_x'].iloc[q], data1['Away_23_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_24_x'].iloc[q], data1['Away_24_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['Away_25_x'].iloc[q], data1['Away_25_y'].iloc[q], 'ro', markersize=10,alpha=0.5)
            ax.plot(data1['ball_x'].iloc[q], data1['ball_y'].iloc[q], 'ko', markersize=10,alpha=0.5)
            #print(q)
            plt.savefig(f'/Users/jungbang1014/高専/ゼミ/卒業研究/data-science/sam/isolate_data/game1/tracking_plot_image/{i}/plot{q}.png')
        print("1シーンの作成が終了しました。")
    
    return min_frame, max_frame

def process_csv_file(input_file_path, target_string):
    # 読み込むデータを一時的に保持するリスト
    temp_data = []
    file_num = 1

    with open(input_file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        header = next(csv_reader)  # ヘッダー行を読み飛ばす
        last_column_index = len(header) - 1  # 最後の列のインデックスを取得
        
        for row in csv_reader:
            # 指定した文字列が見つかったらデータを保存し、リストを初期化する
            if target_string in row['Ball']:
                if temp_data:
                    save_data_to_file(temp_data, file_num)
                    file_num += 1
                    temp_data.clear()
            temp_data.append(row)

        # 最後の部分のデータも保存する
        if temp_data:
            save_data_to_file(temp_data, file_num)

def save_data_to_file(data, file_num):
    file_name = f"/Users/jungbang1014/高専/ゼミ/卒業研究/data-science/sam/isolate_data/game{game_id}/tracking_base_away/plot{file_num}.csv"
    with open(file_name, "w", encoding="utf-8", newline='') as output_file:
        if data:  # データが存在する場合のみCSVファイルに書き込む
            writer = csv.DictWriter(output_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerow(data[0])  # ヘッダー行を書き込む
            writer.writerows(data[1:])  # データ行を書き込む

# 2つ目と3つ目のCSVファイルとの比較を行い、一致する部分までの内容を新しいファイルとして作成する関数
def create_result_file2(df, values, result_file):
    result_data = pd.DataFrame()
    for index, value in enumerate(values):
        if value in df['Time [s]'].iloc[:index+1].values:
            result_data = df.iloc[:index+1].copy()  # result_dataにデータを追加する
            break
    save_data_to_file(result_data, result_file)

def create_result_file(target_string,input_file_path):
    # 読み込むデータを一時的に保持するリスト
    global j
    
    temp_data = []
    file_num = 1

    with open(input_file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # 指定した文字列が見つかったらデータを保存し、リストを初期化する
            if target_string[file_num] == 0:
                if temp_data:
                    save_data_to_file(temp_data, file_num)
                    file_num += 1
                    temp_data.clear()
            elif target_string[file_num] in row.values():
                if temp_data:
                    save_data_to_file(temp_data, file_num)
                    file_num += 1
                    temp_data.clear()
            temp_data.append(row)
        # 最後の部分のデータも保存する
        if temp_data:
            save_data_to_file(temp_data, file_num)

def tracking_data(DATADIR,game_id,teamname):
    '''
    tracking_data(DATADIR,game_id,teamname):
    read Metrica tracking data for game_id and return as a DataFrame. 
    teamname is the name of the team in the filename. For the sample data this is either 'Home' or 'Away'.
    '''
    teamfile = '/Sample_Game_%d/Sample_Game_%d_RawTrackingData_%s_Team.csv' % (game_id,game_id,teamname)
    # First:  deal with file headers so that we can get the player names correct
    csvfile =  open('{}/{}'.format(DATADIR, teamfile), 'r') # create a csv file reader
    reader = csv.reader(csvfile) 
    teamnamefull = next(reader)[3].lower()
    print("Reading team: %s" % teamnamefull)
    # construct column names
    jerseys = [x for x in next(reader) if x != ''] # extract player jersey numbers from second row(各選手の位置を背番号から取得)
    columns = next(reader)
    for i, j in enumerate(jerseys): # create x & y position column headers for each player
        columns[i*2+3] = "{}_{}_x".format(teamname, j)
        columns[i*2+4] = "{}_{}_y".format(teamname, j)
    columns[-2] = "ball_x" # column headers for the x & y positions of the ball
    columns[-1] = "ball_y"
    # Second: read in tracking data and place into pandas Dataframe
    tracking = pd.read_csv('{}/{}'.format(DATADIR, teamfile), names=columns, index_col='Frame', skiprows=3)
    return tracking

def to_metric_coordinates(data,field_dimen=(106.,68.) ):
    '''
    Convert positions from Metrica units to meters (with origin at centre circle)
    '''
    x_columns = [c for c in data.columns if c[-1].lower()=='x']
    y_columns = [c for c in data.columns if c[-1].lower()=='y']
    data[x_columns] = ( data[x_columns]-0.5 ) * field_dimen[0]
    data[y_columns] = -1 * ( data[y_columns]-0.5 ) * field_dimen[1]
    ''' 
    ------------ ***NOTE*** ------------
    Metrica actually define the origin at the *top*-left of the field, not the bottom-left, as discussed in the YouTube video. 
    I've changed the line above to reflect this. It was originally:
    data[y_columns] = ( data[y_columns]-0.5 ) * field_dimen[1]
    ------------ ********** ------------
    '''
    return data



def main():
    file_path = '/Users/jungbang1014/高専/ゼミ/卒業研究/data-science/sam/isolate_data'
    isolate_plot_event_data(file_path,game_id)
    DATADIR = '/Users/jungbang1014/高専/ゼミ/卒業研究/data-science/sam/data' % (game_id,game_id)
    #plot(DATADIR, game_id)
    
    
if __name__ == "__main__":
    target_string = 'NaN'
    DATADIR1 = '/Users/jungbang1014/高専/ゼミ/卒業研究/data-science/new_sam/data'
    data1 = tracking_data(DATADIR1, game_id, 'Away')
    data1 = to_metric_coordinates(data1)

    data2 = tracking_data(DATADIR1, game_id, 'Home')
    data2 = to_metric_coordinates(data2)
    main()