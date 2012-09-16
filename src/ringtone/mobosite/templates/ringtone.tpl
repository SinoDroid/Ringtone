<!DOCTYPE html>
<html language="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
<link rel="stylesheet" type="text/css" href="/media/css/ringtone.css"/>
</head>

<body>
<div id="main">

    {% for ringtone in ringtones %}
    <div id="head">
        <a href="/mobosite/retrieve/0/recent/10/1/"><img class="home" src="/media/image/ic_home.png"/></a>
        <img class="spliter" src="/media/image/line_tab.png" />
        <h1>{{ ringtone.name }}</h1>
    </div>
    
    <div class="product"></div>
    
    <div id="ringtone">
        <h2>{{ ringtone.name }}</h2>
        <div id="info">
            <h3>{{ ringtone.category }}</h3>
            <h4>{{ ringtone.size}} KB</h4>
        </div>
        <a href="{{ ringtone.download_link }}"><img src="/media/image/bt_download.png"/></a>
    </div>
    {% endfor %}
    
    <div id="ads"></div>
    
    <div id="pagination">
        <a href="{% if page_no != 1 and page_count != 0 %}{{ prev_link}}{% endif %}"><img class="prev" src="/media/image/ic_next.png"></a>
        <a href="{% if page_no != page_count and page_count != 0 %}{{ next_link}}{% endif %}"><img class="next" src="/media/image/ic_last.png"></a>
        <div class="counter">{{ page_no}}/{{ page_count}}</div>
    </div>
    
    <div id="foot">
        <span>
            <a href="/media/static/about.html">about us</a> | <a href="mailto:mobodev@gmail.com">countact us</a> | <a href="/media/static/app.html">our App</a>
        </span>
    </div>
</div>
</body>
</html>