# 自作関数のインポート
import read_csv, calc

def check_plus_minus(gpa1, gpa2):
    difference = gpa2 - gpa1
    if difference > 0:
        print("前年比 +" + str(format(difference, ".2f")))
    else:
        print("前年比 " + str(format(difference, ".2f")))

# mainの定義
def main():
  df = read_csv.load_csv('row_score.csv')
  df_2020 = df[df['年度'] == '2020']
  gpa_2020 = calc.get_gpa(list(df_2020['評価']), list(df_2020['単位']))
  df_2021 = df[df['年度'] == '2021']
  gpa_2021 = calc.get_gpa(list(df_2021['評価']), list(df_2021['単位']))
  df_2022 = df[df['年度'] == '2022']
  gpa_2022 = calc.get_gpa(list(df_2022['評価']), list(df_2022['単位']))
  gpa_all = calc.get_gpa(list(df['評価']), list(df['単位']))
  print("あなたの2020年度のGPAは，" + str(format(gpa_2020,".2f")) + "です．")
  print("あなたの2021年度のGPAは，" + str(format(gpa_2021,".2f")) + "です．")
  check_plus_minus(gpa_2020, gpa_2021)
  print("あなたの2022年度のGPAは，" + str(format(gpa_2022,".2f")) + "です．")
  check_plus_minus(gpa_2021, gpa_2022)
  print("あなたの現在のGPAは，    " + str(format(gpa_all,".2f")) + "です．")

# main関数の実行
if __name__ == '__main__':
  main()
