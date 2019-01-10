桃園市交通事故互動地圖
======================

![](banner/banner.png)


data source: [桃園市交通事故資料集](https://data.tycg.gov.tw/opendata/datalist/search?page=0&organize=380130000C&group=&format=&tag=&oldText=&allText=%E6%A1%83%E5%9C%92%E5%B8%82%E4%BA%A4%E9%80%9A%E4%BA%8B%E6%95%85%E8%B3%87%E6%96%99%E8%A1%A8&sort=&sord=score&sdir=desc)

統計年份: 2017 ~ 2018


Web
===

Front-end

```
$ cd web
$ npm install
$ npm run dev   # local development
$ npm run build # build production dist
```

Backend

```
$ pipenv install
$ pipenv install gunicorn
$ pipenv run gunicorn -b 0.0.0.0:8888 app:app
```
