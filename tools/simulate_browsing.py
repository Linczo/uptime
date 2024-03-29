def process_url(url):
    # 创建浏览器实例
    driver = webdriver.Chrome()

    try:
        # 打开网页
        driver.get(url)
        print(f"成功打开网页: {url}")

        # 最大化窗口
        driver.maximize_window()
        print("窗口已最大化")

        window_size = driver.get_window_size()  # 获取窗口大小

        # 随机选择一种操作并执行5次
        for _ in range(5):
            operation = random.randint(1, 3)  # 1: 模拟点击, 2: 模拟移动鼠标, 3: 模拟滚动网页

            if operation == 1:  # 模拟点击
                try:
                    # 随机生成点击位置的坐标
                    x = random.randint(0, window_size['width'])
                    y = random.randint(0, window_size['height'])
                    # 执行点击操作
                    element = driver.find_element("tag name", "body")
                    ActionChains(driver).move_to_element_with_offset(element, x, y).click().perform()
                    print(f"模拟点击成功：坐标({x}, {y})")
                    time.sleep(1)
                except NoSuchElementException:
                    print("无法找到元素")
                    continue

            elif operation == 2:  # 模拟移动鼠标
                actions = ActionChains(driver)
                for _ in range(5):
                    x_offset = random.randint(-100, 100)
                    y_offset = random.randint(-100, 100)
                    actions.move_by_offset(x_offset, y_offset)
                    print(f"模拟鼠标移动成功：偏移量({x_offset}, {y_offset})")
                    time.sleep(1)
                actions.perform()

            else:  # 模拟滚动网页
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                      "window.scrollTo(0, 0);")
                print("模拟滚动到页面底部和顶部")
                time.sleep(2)

        # 刷新网页
        driver.refresh()
        print("刷新网页")
        time.sleep(2)

        # 维持网页打开一段时间
        time.sleep(15)

    except Exception as e:
        print(f"执行操作时出现异常: {str(e)}")

    finally:
        # 关闭浏览器
        driver.quit()
        print("浏览器已关闭")

        # 设置输出值为成功打开的网页URL
        output_name = f"URL_{url}"
        os.environ[output_name] = url
