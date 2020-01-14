from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = '文章管理(blog app)'
    site_title = '文章管理(blog app)管理后台'
    index_title = '文章管理(blog app)首页'


custom_site = CustomSite(name='cus_admin')
