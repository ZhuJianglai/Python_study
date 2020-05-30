# coding=utf-8
from django.contrib.auth.models import User
from django.test import TestCase

from sign.models import Event,Guest


class IndexPageTest(TestCase):
    '''测试index登录首页'''

    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')

class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','admin@email.com','!QAZ2wsx')

    def test_add_admin(self):
        '''添加用户'''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@email.com")

    def test_login_action_username_password_null(self):
        test_data = {'username':'','password': ''}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or passeord error!", response.content)

    def test_login_action_username_password_null(self):
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post( '/login_action/', data=test_data )
        self.assertEqual( response.status_code, 200 )
        self.assertIn( b"username or passeord error!", response.content )

    def test_login_action_username_password_null(self):
        test_data = {'username': 'test', 'password': 'test123456'}
        response = self.client.post( '/login_action/', data=test_data )
        self.assertEqual( response.status_code, 200 )


class EventMangeTest(TestCase):
    '''测试发布管理'''

    def setUp(self):
        '''初始化测试发布'''
        User.objects.create_user( 'admin', 'admin@email.com', '!QAZ2wsx' )
        Event.objects.create( id=1, name='xiaomi5', limit=2000, address='beijing', status=1,
                              start_time='2018-03-20 12:20:00' )
        self.login_user = {'username': 'admin', 'password': '!QAZ2wsx'}

    def test_event_mange_success(self):
        '''测试发布会：小米5'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

    def test_event_manage_seach_success(self):
        '''测试发布会搜索页：xiaomi5'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {'name':"xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)


class GuestManageTest(TestCase):
    '''嘉宾管理'''
    def setUp(self):
        User.objects.create_user('admin', 'admin@email.com', '!QAZ2wsx')
        Event.objects.create(id=1,name='xiaomi5', limit=2000, address='beijing', status=1, start_time='2018-03-20 12:20:00')
        Guest.objects.create(realname='laozhu', phone=18611001100, email='laozhu@email.com', sign=0,event_id=1)
        self.login_user ={'username': 'admin', 'password': '!QAZ2wsx'}

    def test_guest_manage_success(self):
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'laozhu', response.content)
        self.assertIn(b'18611001100', response.content)

    def test_guest_manage_search_success(self):
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_realname/', {"realname":"laozhu"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'laozhu', response.content)
        self.assertIn(b'18611001100', response.content)


class SignIndexActionTest(TestCase):
    def setUp(self):
        User.objects.create_user( 'admin', 'admin@email.com', '!QAZ2wsx' )
        Event.objects.create(id=5, name='xiaomi5', limit=2000, address='beijing', status=1, start_time='2018-03-20 12:20:00')
        Event.objects.create(id=6, name='oneplus', limit=2000, address='shenzhen', status=1,start_time='2018-03-20 12:20:00' )
        Guest.objects.create(realname='abc', phone=17620092449, email='abc@email.com',  sign=0, event_id=5)
        Guest.objects.create(realname='abd', phone=15813388948, email='abd@email.com',  sign=1, event_id=6)
        self.login_user = {'username': 'admin', 'password': '!QAZ2wsx'}

    def test_sign_index_action_phone_null(self):
        '''手机号码为空'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/5/', {'phone': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error',response.content)

    def test_sign_index_action_phone_or_evvent_id_error(self):
        '''手机号码错误或id错误'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/6/', {'phone': '17620092449'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'event id or phone error', response.content)

    def test_sign_index_action_user_sign_has(self):
        '''用户已签道'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/6/', {'phone': '15813388948'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in.', response.content)

    def test_sign_action_sign_success(self):
        '''用户签道成功'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/5/', {'phone': '17620092449'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sign in success!', response.content)













