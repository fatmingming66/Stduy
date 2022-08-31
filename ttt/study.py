from panelWeChat.wx import DEFAULT_SECONDS


def by_class(self, class_name):
    """通过class定位单个元素"""
    try:
        self.d.implicitly_wait(DEFAULT_SECONDS)
        return self.d(className=class_name)
    except Exception as e:
        print("页面没有找到class为%s的元素" % class_name)
        raise e

if __name__ == '__main__':
    by_class()

