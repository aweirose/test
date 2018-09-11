from django.http import HttpResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from wechatpy.replies import create_reply, ImageReply, TextReply
from wechat.models import Users, Menu_click_count
from wechatpy import WeChatClient

client = WeChatClient('wxe107b5305c822984', '6ab57d5431be57957aa2747dd29a0f1a')


class WeixinView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        token = 'DerickRose'
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        try:
            check_signature(token, signature, timestamp, nonce)
            return super(WeixinView, self).dispatch(request, *args, **kwargs)
        except InvalidSignatureException:
            return HttpResponse('error')

    def get(self, request):
        return HttpResponse(request.GET.get('echostr', None))

    def post(self, request):
        msg = parse_message(request.body)
        print(msg)
        if msg.type == 'text':
            reply = create_reply('这是条文字消息', message=msg)
        elif msg.type == 'image':
            reply = create_reply('这是条图片消息', message=msg)
        elif msg.type == 'voice':
            reply = create_reply('这是条语音消息', message=msg)
        elif msg.type == 'event':
            openid = request.GET.get('source', None)
            print(openid)
            # inf = client.user.get(openid)
            if msg.event == 'subscribe':
                reply = create_reply('感谢你的关注', message=msg)
                # Users.objects.create(nickname=inf.nickname, headimgurl=inf.headimgurl,
                #                      sex=inf.sex, country=inf.country,
                #                      province=inf.province, city=inf.city,
                #                      subscribe_time=inf.subscribe_time, openid=inf.openid)
                # print('666666')
            # elif msg.event == 'unsubscribe':
            #     Users.objects.get(openid=inf.openid).delete()
            # elif msg.event == 'click':
            #     reply = ImageReply(message=msg)
            #     media_id = '9kT9-alo_ph3g2I45zACW5X59Dqxbf45k-0Z89XXOSta_H_gqfnAhJvG557pqOEM'
            #     reply.media_id = media_id
            #     Menu_click_count.picture_click_count += 1
            # elif msg.event == 'view':
            #     Menu_click_count.url_click_count += 1
        else:
            reply = create_reply('这是条其他类型消息', message=msg)
        return HttpResponse(reply.render(), content_type=" ")


def link(request):
    return HttpResponse('rose is my favorite player')


