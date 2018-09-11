from django.db import models


class Users(models.Model):
    #SUBSCRIBE_STATUS = ((0, u'未关注'), (1, u'已关注'))
    SEX = ((0, '未知'), (1, '男'), (2, '女'))

    #subscribe_status = models.IntegerField('用户关注状态', choices=SUBSCRIBE_STATUS, default=0)
    openid = models.CharField('openid', max_length=50, blank=True, null=True)
    nickname = models.CharField('昵称', max_length=50, blank=True, null=True)
    headimgurl = models.TextField('头像', max_length=50, blank=True, null=True)
    sex = models.IntegerField('性别', choices=SEX, default=0)
    country = models.CharField('国家', max_length=50, blank=True, null=True)
    province = models.CharField('省份', max_length=50, blank=True, null=True)
    city = models.CharField('城市', max_length=50, blank=True, null=True)
    subscribe_time = models.BigIntegerField('关注时间', blank=True, null=True)

    def __str__(self):
        return '已关注用户:%s(id=%s)' % (self.nickname, self.id)

    class Meta:
        verbose_name = "已关注用户"
        verbose_name_plural = "已关注用户"


class Menu_click_count(models.Model):
    picture_click_count = models.IntegerField('用户点击图片总次数', blank=True, null=True)
    url_click_count = models.IntegerField('用户点击链接总次数', blank=True, null=True)
    #scan_count = models.IntegerField('用户扫码总次数', blank=True, null=True)

    def __str__(self):
        counts = self.picture_click_count + self.url_click_count
        return '菜单点击量:%s' % counts

    class Meta:
        verbose_name = "菜单点击量"
        verbose_name_plural = "菜单点击量"
