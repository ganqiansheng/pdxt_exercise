filename2 = 'mdoctorphoto'
fi1ename1 = 'liudehua2.webp'
with open (fi1ename1,'rb') as f1:
    pic = f1.read()
with open(filename2,'wb') as f2:
    f2.write(pic)


# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
#
#
# class test_table_win(QWidget):
#     update_tooltip_signal = pyqtSignal(object)
#
#     def __init__(self):
#         super(test_table_win, self).__init__(parent=None)
#         self.update_tooltip_signal.connect(self.update_tooltip_slot)
#         self.init_ui()
#
#     def init_ui(self):
#         self.setWindowTitle("测试ToolTip")
#         self.setGeometry(500, 400, 500, 300)
#         self.main_layout = QVBoxLayout()
#         self.main_layout.setContentsMargins(0, 0, 0, 0)
#         self.setLayout(self.main_layout)
#         self.TableWidget = QTableWidget(5, 3)
#         self.TableWidget.resize(self.width(), 225)
#         title_list = ["省份", "省会", "旅游景点"]
#         self.TableWidget.setHorizontalHeaderLabels(title_list)
#         self.TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
#         self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 列宽自动分配
#         # self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # 列宽手动调整
#         self.TableWidget.verticalHeader().setVisible(False)
#         self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
#         QTableWidget.resizeColumnsToContents(self.TableWidget)
#         QTableWidget.resizeRowsToContents(self.TableWidget)
#         self.TableWidget.setMouseTracking(True)
#         self.main_layout.addWidget(self.TableWidget)
#         """为TableWidget安装事件过滤器(关键)"""
#         self.TableWidget.installEventFilter(self)
#
#     def set_table_content(self, list1, list2, list3):
#         row = 0
#         for item1, item2, item3 in zip(list1, list2, list3):
#             self.TableWidget.setItem(row, 0, QTableWidgetItem(item1))
#             self.TableWidget.setItem(row, 1, QTableWidgetItem(item2))
#             self.TableWidget.setItem(row, 2, QTableWidgetItem(item3))
#             row = row + 1
#
#     # 通过计算坐标确定当前位置所属单元格
#     def update_tooltip_slot(self, posit):
#         self.tool_tip = ""
#         self.mouse_x = posit.x()
#         self.mouse_y = posit.y()
#         for r in range(self.TableWidget.rowCount()):
#             row_height = self.TableWidget.rowHeight(r)
#             self.col_width = 0  # 累计列宽
#             # 45是标题的行高,此处表格的行高不变，都是45
#             if row_height * r + 45 <= self.mouse_y <= (r + 1) * row_height + 45:
#                 for c in range(self.TableWidget.columnCount()):
#                     current_col_width = self.TableWidget.columnWidth(c)
#                     # 每一列的列宽可能不同
#                     if self.col_width <= self.mouse_x <= self.col_width + current_col_width:
#                         print("鼠标当前所在的行和列为:({},{})".format(r, c))
#                         item = self.TableWidget.item(r, c)
#                         if item != None:
#                             self.tool_tip = item.text()
#                         else:
#                             self.tool_tip = ""
#                         return self.tool_tip
#                     else:
#                         self.col_width = self.col_width + current_col_width
#
#     """事件过滤器(关键)"""
#
#     def eventFilter(self, object, event):
#         if object is self.TableWidget:
#             self.setCursor(Qt.ArrowCursor)
#             if event.type() == QEvent.ToolTip:
#                 print("当前鼠标位置为:", event.pos())
#                 self.update_tooltip_signal.emit(event.pos())
#                 # 设置提示气泡显示范围矩形框
#                 # QRect(x,y,width,height)
#                 rect = QRect(self.mouse_x, self.mouse_y, 30, 10)
#                 # 设置QSS样式
#                 self.TableWidget.setStyleSheet(
#                     """QToolTip{border:10px;
#                        border-top-left-radius:5px;
#                        border-top-right-radius:5px;
#                        border-bottom-left-radius:5px;
#                        border-bottom-right-radius:5px;
#                        background:#4F4F4F;
#                        color:#00BFFF;
#                        font-size:18px;
#                        font-family:"微软雅黑";
#                     }""")
#                 QApplication.processEvents()
#                 QToolTip.showText(QCursor.pos(), self.tool_tip, self.TableWidget, rect, 1500)
#
#                 """
#                 showText(QPoint, str, QWidget, QRect, int)
#                 #############参数详解###########
#                 #QPoint指定tooptip显示的绝对坐标,QCursor.pos()返回当前鼠标所在位置
#                 #str为设定的tooptip
#                 #QWidget为要展示tooltip的控件
#                 #QRect指定tooltip显示的矩形框范围,当鼠标移出该范围,tooltip将隐藏,使用该参数必须指定Qwidget!
#                 #int用于指定tooltip显示的时长(毫秒)
#                 """
#
#         return QWidget.eventFilter(self, object, event)
#
#
# if __name__ == "__main__":
#     import sys
#
#     province_list = ["四川", "广西", "贵州", "云南", "广东"]
#     city_list = ["成都", "南宁", "贵阳", "昆明", "广州"]
#     site_list = ["九寨沟、黄龙、峨眉山、青城山、乐山大佛、都江堰",
#                  "桂林漓江、钦州三娘湾、北海银滩、大新德天瀑布、百色乐业大石围天坑群",
#                  "黄果树瀑布、赤水丹霞、织金洞、红枫湖、梵净山、遵义会址",
#                  "怒江、九龙瀑布群、三江并流、西双版纳热带植物园、罗平螺丝田、玉龙雪山、丽江古城、香格里拉",
#                  "韶关丹霞山、广州塔、广州白云山、江门开坪碉楼、南澳岛、罗浮山"]
#     app = QApplication(sys.argv)
#     test_table = test_table_win()
#     test_table.set_table_content(province_list, city_list, site_list)
#     test_table.show()
#     sys.exit(app.exec_())
#
