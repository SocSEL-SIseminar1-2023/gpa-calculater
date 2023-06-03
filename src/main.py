# 自作関数のインポート
import read_csv, calc
from decimal import Decimal, ROUND_HALF_UP

# mainの定義
def main():
  df = read_csv.load_csv('row_score.csv')
  gpa = calc.get_gpa(list(df['評価']), list(df['単位']))
  round_gpa = Decimal(str(gpa)).quantize(Decimal('0.01'), ROUND_HALF_UP)
  print("あなたのGPAは，" + str(round_gpa) + "です．") 


# main関数の実行
if __name__ == '__main__':
  main()
