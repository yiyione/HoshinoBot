import random
import jwt
from datetime import timedelta

from nonebot import on_command
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

sv = Service('jwtLogin')

def get_config():
    return util.load_config(__file__)

def generateToken(ctx, ignore_super_user=False):
    user_id = ctx['user_id']
    config = get_config()
    return jwt.encode({'uid': user_id}, config['secret'], algorithm='HS256')

@sv.on_command('token', aliases=('登录凭证', '密码'), only_to_me=True)
async def getToken(session):
    if session.ctx['message_type'] == 'group':
        await session.send('请私聊机器人token,以获取web登录凭证。')
    else:
        await session.send(generateToken(session.ctx))
