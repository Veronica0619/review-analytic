data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 10000 == 0:  #%代表求餘數
			print(len(data))
print('檔案讀取玩了，總共有', len(data), '筆資料')

print(data[0])

wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word]= wc[word] + 1
		else:
			wc[word]= 1 #新增新的key進wc字典
for word in wc: #word 就是字典的key
	if wc[word]> 1000000:
		print(word,wc[word])

while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		break
	if word in wc:		
		print(word,'出現了',wc[word] , '次')
	else:
		print('snoopy!!!沒有出現過哦')


	# print(words)
	# break

#print(data) 印出全部
#print(data[0])
#pirnt('------------------')
#print(data[1])

# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)

# print('留言的平均長度為', sum_len/len(data))


# # 清單做篩選


# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言小於100')
# print(new[0])
# print(new[1])


# # good = []
# # for d in data:
# # 	if 'good' in d:
# # 		good.append(d)
# # print('一共有', len(good), '筆留言有good')
# # print(good[0])


# new_good = [d for d in data if 'good' in d]  #上面的快寫法

# print('一共有', len(new_good), '筆留言有good')
# print(new_good[0])


# # bad = []
# # for d in data:
# # 	bad.append('bad' in d)
# # print(bad)


# bad = ['bad' in d for d in data]
# print(bad)

