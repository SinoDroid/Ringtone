<!DOCTYPE html>
<html language="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
<link rel="stylesheet" type="text/css" href="/media/css/retrieve.css"/>
</head>

<body>
<div id="main">

    <div id="head">
        <a href="/mobosite/retrieve/0/recent/10/1/"><img class="ringtone" src="/media/image/title_main.png"/></a>
        <a href="/mobosite/search/0/recent/10/1/"><img class="category" src="/media/image/ic_search.png"/></a>
        <img class="spliter" src="/media/image/line_tab.png"/>
        <a href="/mobosite/category"><img class="category" src="/media/image/ic_category.png"/></a>
        <img class="spliter" src="/media/image/line_tab.png"/>
        <div class="title">{{ category_name}}</div>
    </div>
    
    <div class="tab">
        <div class="tab-all">
            <a href="/mobosite/retrieve/{{ category_id }}/recent/10/1/">Lastest</a>
            <a href="/mobosite/retrieve/{{ category_id }}/popular/10/1/">Popular</a>
            <a href="/media/static/app.html">Our App</a>
        </div>
        <div class="tab-selected {{ tab_index}}" style="text-weight:bold">{{ tab_name}}</div>
    </div>
    
    {% for ringtone in ringtones %}
    <a class="item" href="{{ ringtone.link}}">
        <img src="/media/image/ic_ringtone.png"/>
        <div class="content">
            <div class="ringtone-title">{{ ringtone.name }}</div>
            <div class="ringtone-description">{{ ringtone.category }}</div>
        </div>
        <div class="ringtone-size">{{ ringtone.size}} KB</div>
    </a>
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