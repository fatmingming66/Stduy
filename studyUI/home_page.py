# -*- coding:utf-8 -*-
# Author:chenjianmin
# TIME: 2022/8/26 13:40
from pages.u2_base_page import BasePage


class YueYunHome:
    pass


class HomePage(BasePage):
    def __init__(self, device):
        super(YueYunHome, self).__init__(device)
        self.msg_icon = "com.zhoulesin.imuikit2:id/icon_msg"
        self.friend_icon = "com.zhoulesin.imuikit2:id/icon_friend"
        self.find_icon = "com.zhoulesin.imuikit2:id/icon_find"
        self.mine_icon = "com.zhoulesin.imuikit2:id/icon_mine"
        self.add_icon = "com.zhoulesin.imuikit2:id/iv_chat_add"
        self.create_group_btn = "com.zhoulesin.imuikit2:id/ll_create_group"
        self.chat_list = "com.zhoulesin.imuikit2:id/rv_message_list"
        self.chat_list_child = "com.zhoulesin.imuikit2:id/ll_content"

    def msg_icon_obj(self):
        """会话图标"""
        return self.by_id(id_name=self.msg_icon)

    def click_msg_icon(self):
        """点击底部会话图标"""
        return self.by_id(id_name=self.msg_icon).click()

    def click_friend_icon(self):
        """点击底部通讯录图标"""
        return self.by_id(id_name=self.friend_icon).click()

    def click_find_icon(self):
        """点击底部发现图标"""
        return self.by_id(id_name=self.find_icon).click()

    def click_mine_icon(self):
        """点击底部我的图标"""
        return self.by_id(id_name=self.mine_icon).click()

    def click_add_icon(self):
        """点击右上角+号图标"""
        return self.by_id(id_name=self.add_icon).click()

    def click_create_group_btn(self):
        """点击右上角+号图标"""
        return self.by_id(id_name=self.create_group_btn).click()

if __name__ == '__main__':
    xx = HomePage()

    






