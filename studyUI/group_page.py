# -*- coding:utf-8 -*-
# Author:chenjianmin
# TIME: 2022/8/26 14:10
from pages.u2_base_page import BasePage


class GroupPage(BasePage):
    def __init__(self, device):
        super().__init__(device)
        self.friend_list = "com.zhoulesin.imuikit2:id/rv_friend_list"
        self.friend_list_child = "com.zhoulesin.imuikit2:id/iv_select"
        self.confirm_btn = "com.zhoulesin.imuikit2:id/tv_confirm"
        self.more_icon = "com.zhoulesin.imuikit2:id/img_right"
        self.group_name = "群聊名称"
        self.group_name_edit_context = "com.zhoulesin.imuikit2:id/et_group_name"
        self.finish_btn = "com.zhoulesin.imuikit2:id/tv_btn"
        self.group_icon = "com.zhoulesin.imuikit2:id/ll_my_group"
        self.group_list = "com.zhoulesin.imuikit2:id/rv_group_list"
        self.group_list_child = "com.zhoulesin.imuikit2:id/name"

    def select_group_member(self):
        """选择群成员，全部选择"""
        friend_list = self.by_id(self.friend_list).child(resourceId=self.friend_list_child)
        for i in range(len(friend_list)):
            friend_list[i].click()

    def click_confirm_btn(self):
        """点击确认按钮"""
        return self.by_id(id_name=self.confirm_btn).click()

    def click_more_icon(self):
        """点击群聊设置中右上角的更多图标"""
        return self.by_id(id_name=self.more_icon).click()

    def modify_group_name(self, group_name):
        """点击群聊设置中右上角的更多图标"""
        self.by_text(self.group_name).click()
        self.by_id(self.group_name_edit_context).send_keys(group_name)
        self.by_id(self.finish_btn).click()

    def click_group_icon(self):
        """点击群组图标，进入群组列表"""
        return self.by_id(self.group_icon).click()


