# # import random

# # print(random.choice(["된장찌개","피자","제육볶음","치킨","떡볶이"]))
# # for x in range(30):
# #   print(random.choice(["된장찌개","피자","치킨","떡볶이","라면","감자튀김"]))
# #   print("이 문장도 반복되나")

# # import time

# # while True:
# #   print(random.choice(["된장찌개","피자","치킨","떡볶이","라면","감자튀김"]))
# #   print("이 문장도 반복되나")
# #   time.sleep(1)

# # lunch = random.choice(["된장찌개","피자","제육볶음"])
# # lunch = "냉장고"
# # dinner = random.choice(["김밥","쫄면","돈까스"])
# # print(lunch)

# # information = {"고향":"수원","취미":"영화관람","좋아하는 음식":"국수"}
# # print(information)
# # print(information.get("취미"))

# # information = {"특기":"피아노","사는 곳":"서울"}
# # print(information.get("특기"))
# # print(information.get("사는 곳"))

# # <step 7 수업>
# # information = {"고향":"수원","취미":"영화관람","좋아하는 음식":"국수"}
# # foods = ["된장찌개","피자","제육볶음"]
# # print(information.get("취미"))
# # information["특기"] = "피아노"
# # information["사는곳"] = "서울"
# # del information["좋아하는 음식"]
# # print(information)
# # print(len(information))
# # information.clear()
# # print(information)
# # print(foods[-2])
# # foods.append("김밥")
# # del foods[1]
# # print(foods)

# # <step 8 수업>
# # for x in range(30):
# #   print(x)

# # foods = ["된장찌개","피자","제육볶음"]
# # # print(foods[0])
# # # print(foods[1])
# # # print(foods[2])
# # for x in range(3):
# #   print(foods[x])
# # for x in foods:
# #   print(x)

# # information = {"고향":"수원","취미":"영화관람","좋아하는 음식":"국수"}
# # for x, y in information.items():
# #   print(x)
# #   print(y)

# # <step 9 수업 : 집합 알아보기>
# # foods=["된장찌개","피자","제육볶음"]
# # foods_set1 = (foods)
# # foods_set2 = set(["된장찌개","피자","제육볶음"])
# # print(foods_set1)
# # print(foods_set2)

# # <step 10 수업 : 집합 사용하기>
# # foods=["된장찌개","피자","제육볶음","된장찌개"]
# # foods_set = set(foods)
# # print(foods)
# # print(foods_set)

# # menu1 = set(["된장찌개","피자","제육볶음"])
# # menu2 = set(["된장찌개","떡국","김밥"])
# # menu3 = menu1 - menu2
# # print(menu3)

# # <step 11 수업 : 만약에>
# # import random

# # food = random.choice(["된장찌개", "피자", "제육볶음"])

# # if (food == "제육볶음"):
# #   print("곱빼기 주세요")
# # print("종료")

# # import random

# # food = random.choice(["된장찌개", "피자", "제육볶음"])

# # print(food)

# # if (food == "제육볶음"):
# #   print("곱빼기 주세요")
# # else:
# #   print("그냥 주세요")
# # print("종료")

# # <step 12 수업 : 오늘은 뭐 드실? 제작1>
# # lunch = ["된장찌개","피자","제육볶음","짜장면"]
# # # lunch.append("돈까스")
# # while True:
# #   item = input("음식을 추가 해주세요 : ")
# #   lunch.append(item)
# #   print(lunch)


# # <step 13 수업 : 오늘은 뭐 드실? 제작2>

# # lunch = ["된장찌개","피자","제육볶음","짜장면"]

# # while True:
# #   print(lunch)
# #   item = input("음식을 추가 해주세요 : ")
# #   if (item=="q"):
# #     break
# #   else:
# #     lunch.append(item)

# # print(lunch)
# # set_lunch = set(lunch)


# # <step 14 수업 : 오늘은 뭐 드실? 제작3>

# # set_lunch = set(["된장찌개","피자","제육볶음","짜장면"])
# # item = "짜장면"
# # set_lunch - set([item])
# # set_lunch= set_lunch - set([])
# # print(set_lunch)

# # set_dinner = set(["된장찌개","피자","제육볶음","짜장면"])
# # food = "짜장면"
# # set_dinner - set([food])
# # set_dinner = set_dinner - set([food])
# # print(set_dinner)

# # <step 15 수업 : 오늘은 뭐 드실? 제작4>
import random
import time

lunch = ["된장찌개","피자","제육볶음","짜장면"]

while True:
  print(lunch)
  item = input("음식을 추가 해주세요 : ")
  if (item=="q"):
    break
  else:
    lunch.append(item)
print(lunch)

set_lunch = set(lunch)
while True:
  print(set_lunch)
  item = input("음식을 삭제해주세요 : ")
  if(item == "q"):
    break
  else:
    set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")

print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(random.choice(list(set_lunch)))