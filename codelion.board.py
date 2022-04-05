# # <step 2 수업 : 함수 알아보기>

# def make_dolcelatte():
#   print("1. 얼음을 넣는다.")
#   print("2. 연유를 30ml 넣는다.")
#   print("3. 찬 우유를 넣는다.")
#   print("4. 에스프레소샷을 넣는다.")

# def make_blueberry_smoothie():
#   print("1. 블루베리 20g을 넣는다.")
#   print("2. 우유 300ml 넣는다.")
#   print("3. 얼음을 넣는다.")
#   print("4. 믹서기에 간다.")

# def make_simple_latte():
#   print("1. 커피를 넣는다.")
#   print("2. 우유를 넣는다.")
#   print("3. 신나게 섞는다.")

# make_simple_latte()
# make_dolcelatte()


# # <step 4 수업 : 이상형이 뭐에요? 제작 2>
# total_dictionary = {}

# while True:
#   question = input("질문을 입력해주세요 : ")
#   if question == "q" :
#     break
#   else:
#     total_dictionary[question] = ""

# print(total_dictionary)


# # <step 5 수업 : 이상형이 뭐에요? 제작 3>

# total_dictionary = {}

# while True:
#   question = input("질문을 입력해주세요 : ")
#   if question == "q" :
#     break
#   else:
#     total_dictionary[question] = ""

# for i in total_dictionary:
#   print(i)
#   answer = input("답변을 입력해주세요 :")
#   total_dictionary[i] =answer
# print(total_dictionary)

# # <step 6 수업 : 이상형이 뭐에요? 제작 4>

# total_list = []

# while True:
#   question = input("질문을 입력해주세요 : ")
#   if question == "q" :
#     break
#   else:
#     total_list.append{"질문" : question, "답변" : ""}

# for i in total_dictionary:
#   print(i)
#   answer = input("답변을 입력해주세요 :")
#   total_dictionary[i] =answer
# print(total_dictionary)

# # <step 7 수업 : 이상형이 뭐에요? 제작 5>

total_list = []

while True:
  question = input("질문을 입력해주세요 : ")
  if question == "q" :
    break
  else:
    total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
  print(i["질문"])
  answer = input("답변을 입력해주세요 :")
  i["답변"] = answer
print(total_list)

# # <step 8 수업 : 이상형이 뭐에요? 정리하기>

total_dictionary = {}

while True:
  question = input("질문을 입력해주세요 : ")
  if question == "q" :
    break
  else:
    total_dictionary[question] = ""

for i in total_dictionary:
  print(i)
  answer = input("답변을 입력해주세요 :")
  total_dictionary[i]] = answer
print(total_dictionary)