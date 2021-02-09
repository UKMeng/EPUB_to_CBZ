import ebooklib
from ebooklib import epub
import re
import os
from pyquery import PyQuery as pq
test = epub.read_epub('1.epub')

# 图片并未按顺序命名，需要从
count = 0
for item in test.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    print('==================================')
    img_name = 'img/' + os.path.splitext(os.path.split(item.get_name())[1])[0].zfill(4) + '.jpg' # html/1.html -> img/0001.jpg
    a = ebooklib.utils.parse_html_string(item.get_content()) # 解析字符串
    doc = pq(a)
    item_name = re.sub('\\.\\./', '', doc('img').attr('src')) # 获得文件名 '../image/vol.moe-007031.jpg' 并去除前面的'../'
    item = test.get_item_with_href(item_name) # get_item_with_href() 通过文件名查找item
    print('----------------------------------')
    with open(img_name, 'wb') as f:
        f.write(item.get_content())
    print('==================================')



#name = 'image/' + str(count).zfill(3) + '.jpg'   # zfill()给字符串的数字补0
# 保存图片
#item = test.get_item_with_href('image/cover.jpg') # get_item_with_href() 通过文件名查找item
#name = 'cover.jpg'
#with open(name, 'wb') as f:
    #f.write(item.get_content())

'''
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/#" lang="en" xml:lang="en">
  <head/>
  <body><div class="fs">&#13;
        <div>&#13;
                <img src="../image/vol.moe-007031.jpg" alt="Comic Book Images" class="singlePage"/>&#13;
        </div>&#13;
</div>&#13;
</body>
</html>
'''