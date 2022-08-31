# -*- coding:utf-8 -*-
# Author:chenjianmin
# TIME: 2022/8/26 13:50
from pages.u2_base_page import BasePage


class ChatPage(BasePage):
    def __init__(self, device):
        super(SingleChat, self).__init__(device)
        self.msg_icon = "com.zhoulesin.imuikit2:id/icon_msg"
        self.friend_icon = "com.zhoulesin.imuikit2:id/icon_friend"
        self.find_icon = "com.zhoulesin.imuikit2:id/icon_find"
        self.mine_icon = "com.zhoulesin.imuikit2:id/icon_mine"
        self.content = "com.zhoulesin.imuikit2:id/et_content"
        self.send_button = "com.zhoulesin.imuikit2:id/btn_send"
        self.more_button = "com.zhoulesin.imuikit2:id/btn_more"
        self.album_icon = "com.zhoulesin.imuikit2:id/photo_layout"
        self.finish_button = "com.zhoulesin.imuikit2:id/btn_ok"

    def open_chat_by_name(self, name):
        """根据会话名打开会话"""
        return self.by_text(text_name=name).click()

    def send_text(self, text):
        """发送文本消息"""
        return self.by_id(id_name=self.content).send_keys(text)

    def click_send_button(self):
        """点击发送按钮"""
        return self.by_id(id_name=self.send_button).click()

    def click_bottom_side(self):
        """点击会话界面底部区域、唤起键盘"""
        return self.d.click(0.276, 0.973)

    def click_more_button(self):
        """点击+号按钮"""
        return self.by_id(id_name=self.more_button).click()

    def album_icon_obj(self):
        """相册图标"""
        return self.by_id(id_name=self.album_icon)

    def click_album_icon(self):
        """点击相册图标打开相册"""
        return self.by_id(id_name=self.album_icon).click()

    def select_picture(self, range_int):
        """点击相册中的图片选择图片"""
        return self.by_xpath(
            '//*[@resource-id="com.zhoulesin.imuikit2:id/recycler"]/android.widget.FrameLayout[%d]' % range_int).click()

    def click_finish_button(self):
        """点击完成按钮、发送图片"""
        return self.by_id(id_name=self.finish_button).click()





