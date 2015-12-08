#-*- coding: utf-8 -*-

import hashlib

db = {}

def calc_md5(passward):
	md5 = hashlib.md5()
	md5.update(passward.encode('utf-8'))
	return md5.hexdigest()

def register(username, passward):
	
	db[username] = calc_md5(passward + username + 'the-salt')
	print('Register successfuly!\nYou can login')

def login(user, passward):
	user = input('Your username: ')
	passward = input('Your passward: ')	
	if user in db:
		if calc_md5(passward + user + 'the-salt') == db[user]:	
			print('%s login successfully' %user)
		else:
			print('Passward incorrect!, Please try again')

	else:
		print('%s doesn\'t exist'%user)

if __name__ == '__main__':
	user = input('You want name: ')
	passward = input('You want passward: ')
	register(user, passward)	
	login(user, passward)
