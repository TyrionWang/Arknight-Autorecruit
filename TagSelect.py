def recommend_tags(v, reader):
    all_tags = {'狙击干员', '术师干员', '先锋干员', '近卫干员', '重装干员', '医疗干员', '辅助干员', '特种干员', '近战位', '远程位',
                '输出', '支援机械', '防护', '生存', '治疗', '费用回复', '群攻', '减速', '支援', '快速复活', '削弱', '位移', '召唤',
                '控场', '爆发', '新手', '资深干员', '高级资深干员'}
    result = reader.readtext(v)
    current_tags = set()
    tag_num = 0
    temp_set = set()
    tag_info = dict()
    for item in result:
        temp_set.add(item[1])
        if item[1] in all_tags:
            tag_info[item[1]] = coordinate_change(item[0])  # 包含准备返回的tag信息
            tag_num += 1
            current_tags.add(item[1])
    if tag_num != 5:  # 检测到的tag数量出错
        return 404
    if "高级资深干员" in current_tags:
        return 666
    elif "支援机械" in current_tags:
        return [tag_info["支援机械"], 1]
    elif "资深干员" in current_tags != 0:
        return [tag_info["资深干员"], 9]
    elif current_tags & {"召唤", "控场", "爆发"} != set():
        temp_tag = current_tags & {"召唤", "控场", "爆发"}
        temp = temp_tag.pop()
        return [tag_info[temp], 9]
    elif current_tags & {"特种", "削弱", "快速复活", "支援", "位移"} != set():
        temp_tag = current_tags & {"特种", "削弱", "快速复活", "支援", "位移"}
        temp = temp_tag.pop()
        return [tag_info[temp], 9]
    else:
        return 400


# easyocr和airtest间的坐标转换
def coordinate_change(ocr_pos):
    pos_ax = ocr_pos[0][0]
    pos_ay = ocr_pos[0][1]
    pos_bx = ocr_pos[1][0]
    pos_cy = ocr_pos[2][1]
    air_pos = ((pos_ax + pos_bx) / 2, (pos_ay + pos_cy) / 2)
    return air_pos
