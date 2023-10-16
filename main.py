import math
import fractions

# [機能A]@アリス担当 #############
def func_A ():
  f = fractions.Fraction
  t1 = f(2,3)
  t2 = f(4,6)
  ans = t1 + t2
  print(f'{t1} + {t2} = {ans} (= {float(ans):.2f})') 

# [機能B]@ボブ担当 ###############


# メイン処理 ####################
if __name__ == "__main__": 

  print("start.")

  ## 機能Aの実行
  func_A()
  
  ## 機能Bの実行

  print("end.")