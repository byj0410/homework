movie_rank=["닥터스트레인지", "스플릿", "럭키"] #41

movie_rank.append("배트맨") #42

#43^
movie_rank.insert(1, "슈퍼맨")

#44^
movie_rank.remove("럭키")
del movie_rank[3]

#45^
del movie_rank[2:]
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")

#46^
lang1=["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2

#47
nums=[1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

#48^
nums=[1, 2, 3, 4, 5]
print(sum(nums))

#49^
cook = ["피자", 김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#50^
nums=[1, 2, 3, 4, 5]
print(sum(nums)/len(nums))
