from django.utils.safestring import mark_safe  #mark_safe：安全字符串

class MyPage:

    def __init__(self, page_num, page_num_count, req_path, per_page_num, page_num_show):

        self.page_num = page_num
        self.page_num_count = page_num_count
        self.req_path = req_path
        self.per_page_num = per_page_num  # 每页显示多少条数据
        self.page_num_show = page_num_show  # 显示的页码数

        # 如果有异常就默认当前页
        try:
            self.page_num = int(self.page_num)
        except Exception:
            self.page_num = 1

        # 计算有多少页 如果商不为0页数就加一 总的页码数
        a, b = divmod(self.page_num_count, self.per_page_num)
        if b:
            self.page_num_count = a + 1
        else:
            self.page_num_count = a

        # 如果小于1就让他去当前页，大于总页数就让他去最后一页
        if self.page_num <= 0:
            self.page_num = 1
        elif self.page_num >= self.page_num_count:
            self.page_num = self.page_num_count

        # 每页展示的页码数
        half_show = self.page_num_show // 2  # 2
        if self.page_num - half_show <= 0:
            start_page_num = 1
            end_page_num = self.page_num_show + 1
        elif self.page_num + half_show >= self.page_num_count:
            start_page_num = self.page_num_count - self.page_num_show + 1
            end_page_num = self.page_num_count + 1
        else:
            start_page_num = self.page_num - half_show  # 3
            end_page_num = self.page_num + half_show + 1  # 7

        self.start_page_num = start_page_num
        self.end_page_num = end_page_num

    # 每页显示多少条数据  开始
    @property
    def start_data_num(self):
        return (self.page_num - 1) * self.per_page_num

    # 每页显示多少条数据  结束
    @property
    def end_data_num(self):
        return self.page_num * self.per_page_num

    # 前端页码
    def page_html(self):
        page_num_range = range(self.start_page_num, self.end_page_num)
        print("hallo world:",page_num_range)
        page_html = ''

        # 上一页
        if self.page_num <= 1:
            page_pre_html = f'<span class="previous_page disabled">Previous</span>'

        else:
                page_pre_html = f'<a class="previous_page" rel="prev" href="{self.req_path}?page={self.page_num-1}&amp;q=django+blog&amp;type=Repositories">Previous</a>'
        page_html += page_pre_html

        # 页码标签 并且有选中状态
        from math import ceil
        for i in page_num_range:
            if i == self.page_num:
                page_html += f'<em class="current" data-total-pages="100">{i}</em>'
            elif  self.page_num<=6:
                page_html+= f'<a aria-label="Page {i}" href="{self.req_path}?page={i}&amp;q=django++blog&amp;type=Repositories">{i}</a>'
            elif self.page_num>6:
                if 1<i<self.page_num-4:
                    if '<span class="gap">&hellip;</span>'  not in page_html:
                        page_html += '<span class="gap">&hellip;</span>'
                else:
                    page_html += f'<a aria-label="Page {i}" href="{self.req_path}?page={i}&amp;q=django++blog&amp;type=Repositories">{i}</a>'

        # 下一页
        if self.page_num < self.page_num_count:
                page_next_html =  f'<a class="next_page" rel="next" href="{self.req_path}?page={self.page_num+1}">Next</a>'
        else:
                page_next_html = f'<span class="next_page disabled">Next</span>'
        page_html += page_next_html
        return mark_safe(page_html)
