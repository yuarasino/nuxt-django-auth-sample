# nuxt-django-auth-sample
Nuxt.js × Django で認証やるサンプル

## 試してみる

```
$ docker-compose up -d

# apiサーバーを起動
$ docker-compose exec api make migrate
$ docker-compose exec api make createsuperuser
$ docker-compose exec api make runserver

# appサーバーを起動
$ docker-compose exec app npm run dev
```

http://localhost:3000 を開くと、ログイン画面が見えるはず

## 使ったもの

- Django djangorestframework TokenAuthentication
- Nuxt.js @nuxtjs/auth
