ACCOUNT = 'test'
PASSWORD = '123456'

print('请输入用户名')
user_account = input()

print('请输入密码')
user_password = input()

login_success: bool = ACCOUNT == user_account and PASSWORD == user_password

if login_success:
    print('登录成功')
else:
    print('账号或密码错误')
