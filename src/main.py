# 自作関数のインポート
import read_csv, calc

# mainの定義
def main():
  df = read_csv.load_csv('score_drop.csv')
  gpa = calc.get_gpa(list(df['評価']), list(df['単位']))
  df['int単位'] = df['単位'].astype(int)
  shuutoku = df['int単位'].sum()
  rakudai = df['単位'].eq('0').sum()

  print("あなたの習得単位数は" + shuutoku.astype(str) + "です")
  print("あなたの落第単位科目数は" + rakudai.astype(str) + "です")
  print("あなたのGPAは，" + str(gpa) + "です．")

# main関数の実行
if __name__ == '__main__':
  main()
