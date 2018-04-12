# 鐵人賽 - Django
- 2018/04/11(三) - 1~6 done
- [Django 鐵人賽 30天](https://ithelp.ithome.com.tw/articles/10157091)
- **自學!!**

```cmd
:: 我在 Win10, 使用 Anaconda3.6版執行~~
> python --version
Python 3.6.0 :: Anaconda 4.3.0 (64-bit)

:: 建立 && 進入 虛擬環境
:: conda create --name <env name>

> pip install django==1.11.12

> django-admin startproject lunch

> cd lunch
```

> *全域變數* 皆為 `[A-Z]+_[A-Z0-9]+`


## Django - MTV
* Models 代表資料，通常是用來與資料庫溝通。
* Templates 代表把東西呈現給使用者的媒介。
* Views 用來處理 models，以將其呈現於 templates 中，或者處理使用者送來的資料（以 HTTP POST 等方式），並存入 models。

```cmd
:: (作者沒提到這個, DB版本控管用)
> python manage.py migrate

> python
:: 完成上述設定後, 進入python, 執行看看, 沒報錯表示資料庫設定OK ((這邊是很久以前寫的, 但好像會出錯!!))
from django.db import connection
cursor = connection.cursor()
```


## 目標~
1. 使用者註冊與登入。
2. 列出與顯示店家資訊，包括名稱與菜單圖片。使用者可以自由新增、修改、刪除。
3. 選取一家店，讓每個使用者可以填入自己想吃什麼。


## 1
(先pass, django有內建好一套註冊機制)
```cmd
> python manage.py createsuperuser
```


## 2. 建立 app
- 在 Django 中，網站叫做 _project_，而組成網站的元件則是 _app_, 習慣就好...
- 在 Django 中，通常習慣把 app 取名為它主要功能的 model 的複數形

```cmd
:: 建立 
> python manage.py startapp stores
```


> `Server 收到一個 HTTP request 時，會確認 request 的 URI 應該對應到哪個 view（如果對應不到，直接回傳 404 Not Found），並把 request 交給它。View 要負責處理這個 request，並回傳一個 HTTP response.` 這個過程, 根本就是一個 function 在做的事情!! 

```py
# 這邊是我瞎掰的, 但概念就是這樣
def make_response():
    response = view(request, data, headers, URL, ...)   # django.http.HttpResponse 物件
    return response
```

#### 改底下幾個個地方
* /lunch/settings/base.py
```py
# ...pass
INSTALLED_APPS = [
    'stores',       ### 增加這行
    'django.contrib.admin',
# pass...
```
* /lunch/urls.py
```py
from django.conf.urls import url, include   ### 增加 include
from django.contrib import admin

urlpatterns = [
    url(r'^stores/', include('stores.urls')),   ### 增加 app router
    url(r'^admin/', admin.site.urls),
]
```
* /lunch/stores/urls.py
```py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
]
```
* /lunch/stores/templates/home.url
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>午餐系統</title>
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-default navbar-static-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <a class="navbar-brand" href="{% url 'home' %}">午餐系統</a>
            </div>
        </div>
    </nav>
</body>
</html>
```

----------------------------------------------

* /stores/models.py
```py
class Store(models.Model):

    name = models.CharField(max_length=20)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    store = models.ForeignKey('Store', related_name='menu_items')
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name
```

```cmd
:: 重新偵測 models.py, 並且對目前 資料庫 的狀況做紀錄.
> python manage.py makemigrations stores
Migrations for 'stores':
  0001_initial.py:
    - Create model MenuItem
    - Create model Store
    - Add field store to menuitem
```
> 這些資訊被放在 `store/migrations/0001_initial.py`. 

```cmd
:: 將 資料庫 與 models.py同步.
> python manage.py migrate stores
Operations to perform:
  Apply all migrations: stores
Running migrations:
  Applying stores.0001_initial... OK
```


[Win10找不到'sqlite3'的解法](https://stackoverflow.com/questions/4578231/error-while-accessing-sqlite3-shell-from-django-application/4578325)
```cmd
> python manage.py dbshell
SQLite version 3.23.1 2018-04-10 17:39:29
Enter ".help" for usage hints.

sqlite> .tables
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            stores_menuitem
auth_user_user_permissions  stores_stores

sqlite> select * from django_migrations;
1|contenttypes|0001_initial|2018-04-11 15:50:39.368698
2|auth|0001_initial|2018-04-11 15:50:39.393640
3|admin|0001_initial|2018-04-11 15:50:39.415085
...
13|sessions|0001_initial|2018-04-11 15:50:39.625293
14|stores|0001_initial|2018-04-12 16:14:09.528863
:: 目前各 app 被 migrate 到哪個階段，以及進行的時間
```

Migration 結束

-------------------------------------------

## Django admin
```cmd
> python manage.py createsuperuser
:: http://localhost:8000/admin/
```