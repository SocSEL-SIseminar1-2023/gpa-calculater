# 自作関数のインポート
import read_csv, calc

# mainの定義
def main():
  n = input("計算したいcsvファイルを入力してください")
  try:
    df = read_csv.load_csv(n)
  except FileNotFoundError:
    print('File not found.')
  gpa = calc.get_gpa(list(df['評価']), list(df['単位']))
  print("あなたのGPAは，" + str(gpa) + "です．")

# main関数の実行
if __name__ == '__main__':
  main()
