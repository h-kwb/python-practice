try:
  number = int(input("数を入力してください。\n正負を判定します。"))

  if number > 0:
    print(f"{number}は、正の数です。")
  elif number == 0:
    print(f"{number}は、0です。")
  else:
    print(f"{number}は、負の数です。")
except ValueError:
  print("数字を入力してください。")
