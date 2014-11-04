# -*- coding: utf-8 -*- 
import random
import vk
import time

vkapi = vk.API('4597440', 'Your login','Your password',scope=2097151++262144) #Takes token from vk.com
s = vkapi.access_token
print 'Starting'
print 'Atention ! Check if the user is in community.'
time.sleep(1)
id_community = -77885032 #Id community
id_post = 9 #Id post in wall
h_rep = 41 #Quantity repost`s
list_users = [] 
a = 0
for a in range(0,h_rep):
	answer = vkapi('wall.getReposts',owner_id=id_community,post_id=id_post,count=1,offset=a)
	id_user = answer['items'][0]['to_id']
	if id_user > 0:
		member_group = vkapi('groups.isMember',group_id=id_community/-1,user_id=id_user)
		time.sleep(0.3) 
		if member_group == 1:
			list_users.append(id_user)
			reposrnul = vkapi('users.get',user_ids=id_user)
			time.sleep(0.3) 
			name_reposter = reposrnul[0]['first_name'].encode('utf-8') + ' ' + reposrnul[0]['last_name'].encode('utf-8')
			print str(id_user)+ ' ' + name_reposter			
		else:
			pass
		
	else:
		pass
	a+=a
	time.sleep(0.3)
		
winner =  random.choice(list_users)
id_winner =  winner
winner = vkapi('users.get',user_ids=winner)
name_winner = str(id_winner)+' '+winner[0]['first_name'].encode('utf-8') + ' ' + winner[0]['last_name'].encode('utf-8') 
print name_winner #Print id and name winner

for key in list_users:
	if key > 0:
		pass
	else:
		list_users.remove(key)
print 'Quantity users: ' + str(len(list_users))






















