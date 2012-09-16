<!DOCTYPE html>
<html language="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
<link rel="stylesheet" type="text/css" href="/media/css/search.css"/>
</head>

<body>
<div id="main">

    <div class="head">
        <a href="/mobosite/retrieve/0/recent/10/1/"><img class="home" src="/media/image/ic_home.png"/></a>
        <img class="spliter" src="/media/image/line_tab.png"/>
        <img class="search" src="/media/image/title_search.png"/>
    </div>
    
    <div class="searchbar">
        <form action="/mobosite/search/0/popular/10/1/" method="get">
            <input class="keyword" name="k" type="input" value="{{ keyword }}" />
            <input class="start" type="submit" value=""/>
        </form>
    </div>
    
    <div class="list-body">
        {% for ringtone in ringtones %}
        <a class="item" href="{{ ringtone.link }}" style="">
            <img src="/media/image/ic_ringtone.png"/>
            <div class="content">
                <div class="ringtone-title">{{ ringtone.name }}</div>
                <div class="ringtone-description">{{ ringtone.category }}</div>
            </div>
            <div class="ringtone-size">{{ ringtone.size}} KB</div>
        </a>
        {% empty %}
        <div>{{ noresult }}</div>
        {% endfor %}
    </div>
    
    <div id="ads"></div>
    
    <div id="paginator">
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