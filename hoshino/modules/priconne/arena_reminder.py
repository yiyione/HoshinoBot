from hoshino.service import Service

svtw = Service('pcr-arena-reminder-tw', enable_on_default=False)
svjp = Service('pcr-arena-reminder-jp', enable_on_default=False)
maiyaocn = Service('pcr-maiyao-reminder-cn', enable_on_default=True)
msg = '骑士君、准备好背刺了吗？'

@maiyaocn.scheduled_job('cron', hour='0')
async def pcr_reminder_cn0():
    await maiyaocn.broadcast('骑士君，该买药了！', 'pcr-reminder-cn', 0.2)

@maiyaocn.scheduled_job('cron', hour='6')
async def pcr_reminder_cn6():
    await maiyaocn.broadcast('骑士君，该买药了！', 'pcr-reminder-cn', 0.2)

@maiyaocn.scheduled_job('cron', hour='12')
async def pcr_reminder_cn12():
    await maiyaocn.broadcast('骑士君，该买药了！', 'pcr-reminder-cn', 0.2)

@maiyaocn.scheduled_job('cron', hour='18')
async def pcr_reminder_cn18():
    await maiyaocn.broadcast('骑士君，该买药了！', 'pcr-reminder-cn', 0.2)

@svtw.scheduled_job('cron', hour='14', minute='45')
async def pcr_reminder_tw():
    await svtw.broadcast(msg, 'pcr-reminder-tw', 0.2)

@svjp.scheduled_job('cron', hour='13', minute='45')
async def pcr_reminder_jp():
    await svjp.broadcast(msg, 'pcr-reminder-jp', 0.2)
