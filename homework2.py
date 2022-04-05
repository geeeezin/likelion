money = int(input("금액을 넣어주세요 : "))

while True :
  menu={"콜라":500, "커피":400, "사이다":300, "율무차":200}
  goods = list(menu.keys())
  prices = list(menu.values())

  print("[이화네 음료수]")
  print("현재금액 :" , money , "원")

  for i in range(len(goods)):
    print(i+1, ". ", goods[i]," - ", prices[i], "원")
  
  order = int(input("음료를 선택해주세요 : "))-1

  change = money - prices[order]

  if change < 0:
    print("금액이 부족합니다.")
    break
  elif change == 0 :
    print ("잔액은 0원입니다. 이용해주셔서 감사합니다.")
    break
  else :
    print ("잔액은 ", change, "원 입니다.")
    question = str(input("추가로 구매하시겠습니까?(Y/N): "))
    if question == "Y" :
      continue
    else :
      break

    

  

