# easyocr和airtest间的坐标转换
def coordinate_change(ocr_pos):
    pos_ax = ocr_pos[0][0]
    pos_ay = ocr_pos[0][1]
    pos_bx = ocr_pos[1][0]
    pos_cy = ocr_pos[2][1]
    air_pos = ((pos_ax + pos_bx) / 2, (pos_ay + pos_cy) / 2)
    return air_pos
