# -*- coding:utf-8 -*-
# Author:chenjianmin
# TIME: 2022/8/26 10:18
# from studyUI.home_page import YueYunHome

# from base.common import
from base.base_page import logger
from base.common import get_android_version
from studyUI.home_page import YueYunHome
from base.common import get_devices

class SingleChat:
    pass

DEFAULT_SECONDS = 10

def GGR():
    pass


class BasePage(object):
    """
    第一层：对uiAutomator2进行二次封装，定义一个所有页面都继承的BasePage
    封装uiAutomator2基本方法，如：元素定位，元素等待，导航页面等
    不需要全部封装，用到多少就封装多少
    """

    def __init__(self, device):
        assert isinstance(device, object)
        self.d = device

    def init_driver(self):
        device = self.device_num()[0]  # 10.111.150.202:5555 这种格式.
        appium_port = self.device_num()[1]
        # 在这里填入安卓版本,避免跑不起来.
        browser = GGR().browser(devices=device, platformversion=get_android_version(device),
                                port=appium_port)  # 自己获取安卓版本
        logger.info(f"脚本当前连接的平板:{device},安卓版本：{get_android_version(device)},Appium端口:{appium_port}")
        return browser
        pass

    def notify(self):
        """ 脚本启动的一些注意事项提醒 """
        logger.debug("注意事项：1.SpeedPicker请开启快速拣货功能。\n2.注意平板连接到此电脑。\n3.注意先启动Appium服务。")

    def device_num(self):
        num = int(__file__.split('\\')[-1].split('.')[0].split('cn')[-1]) - 1  # 序号从0开始
        devices_ls = get_devices()
        try:
            return devices_ls[num], 4725 + num * 5  # 每个设备之间，间隔5个以上
        except:
            logger.warning("获取设备UDID失败了,检查一下.")
            pass


    def by_id(self, id_name):
        """通过id定位单个元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(resourceId=id_name)
        except Exception as e:
            print("页面中没有找到id为%s的元素" % id_name)
            raise e

    def by_id_matches(self, id_name):
        """通过id关键字匹配定位单个元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(resourceIdMatches=id_name)
        except Exception as e:
            print("页面没有找到id为%s的元素" % id_name)
            raise e

    def by_class(self, class_name):
        """通过class定位单个元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(className=class_name)
        except Exception as e:
            print("页面没有找到class为%s的元素" % class_name)
            raise e

    def by_text(self, text_name):
        """通过text定位单个元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(text_name)
        except Exception as e:
            print("页面没有找到text为%s的元素" % text_name)
            raise e

    def by_class_text(self,class_name,text_name):
        """通过text和class多重定位某个元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(className=class_name,text=text_name)
        except Exception as e:
            print("页面没有找到class为%s、text为%s的元素" % (class_name,text_name))
            raise e

    def by_text_match(self, text_match):
        """通过textMatches关键字匹配定位单个元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(textMatches=text_match)
        except Exception as e:
            print("页面中没有找到text为%s的元素" % text_match)
            raise e

    def by_desc(self,desc_name):
        """通过description定位单个元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(description=desc_name)
        except Exception as e:
            print("页面没有找到desc为%s的元素" % desc_name)
            raise e

    def by_xpath(self,xpath):
        """通过xpath定位单个元素【特别注意：只有用d.xpath，千万不能用d(xpath)】"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d.xpath(xpath)
        except Exception as e:
            print("页面没有找到xpath为%s的元素" % xpath)
            raise e

    def by_id_text(self,id_name,text_name):
        """通过id和text多重定位"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(resourceId=id_name,text=text_name)
        except Exception as e:
            print("页面中没有找到resourceId、text为%s、%s的元素" % (id_name,text_name))
            raise e

    def find_child_by_id_class(self,id_name,class_name):
        """通过id和class定位一组元素，并查找子元素"""
        try:
            self.d.implicitly_wait(DEFAULT_SECONDS)
            return self.d(resourceId=id_name).child(className=class_name)
        except Exception as e:
            print("页面中没有找到resourceId为%s、classNam为%s的元素" % (id_name,class_name))
            raise e

    def is_text_loc(self,text):
        """定位某个文本对象 (多用于判断某个文本是否存在)"""
        return self.by_text(text_name=text)

    def is_id_loc(self,id):
        """定位某个id对象（用于判断某个id是否存在）"""
        return self.by_id(id_name=id)
    def swipe_up(self):
        """当前页面向上滑动，步长为10"""
        return self.d(scrollable=True).swipe("up",steps=10)

    def swipe_down(self):
        """当前页面向下滑动，步长为10"""
        return self.d(scrollable=True).swipe("down", steps=10)

    def swipe_left(self):
        """当前页面向左滑动，步长为10"""
        return self.d(scrollable=True).swipe("left", steps=10)

    def swipe_right(self):
        """当前页面向右滑动，步长为10"""
        return self.d(scrollable=True).swipe("right", steps=10)


    def ChatPage(self, device):
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

    def HomePage(self, device):
        super(YueYunHome, self).__init__(device)
        self.msg_icon = "com.lousiness.imuikit2:id/icon_msg"
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

    def GroupPage(self, device):
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


if __name__ == '__main__':
            xx = BasePage()
            by_id =xx()
