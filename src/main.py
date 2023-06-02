# 自作関数のインポート
import read_csv, calc, decimal

# 有効数字3桁指定
decimal.getcontext().prec = 3

# mainの定義
def main():
  df = read_csv.load_csv('row_score.csv')
  gpa = calc.get_gpa(list(df['評価']), list(df['単位']))
  round_gpa = decimal.Decimal(gpa)
  print("あなたのGPAは，" + str(round_gpa+0) + "です．")    # 有効数字にするために0を加える必要がある


# main関数の実行
if __name__ == '__main__':
  main()
