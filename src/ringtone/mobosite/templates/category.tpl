<!DOCTYPE html>
<html language="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
<link rel="stylesheet" type="text/css" href="/media/css/category.css"/>
</head>
    
<body>
<div id="main">

    <div id="head">
        <a href="/mobosite/retrieve/0/rencet/20/1/"><img class="home" src="/media/image/ic_home.png"/></a>
        <img class="spliter" src="/media/image/line_tab.png"/>
        <img class="title" src="/media/image/title_category.png"/>
    </div>
    
    {% for category in categories %}
    <a class="item {{ forloop.first|yesno:'first,,'}}{{ forloop.last|yesno:'last,,'}}"
        href="/mobosite/retrieve/{{ category.id }}/popular/10/1/" >
        <img src="/media/image/ic_category_default.png"/>
        <h2>{{ category.name }}</h2>
    </a>
    {% endfor %}
    
    <div id="ads"></div>
    
    <div id="foot">
        <span>
            <a href="/media/static/about.html">about us</a> | <a href="mailto:mobodev@gmail.com">contact us</a> | <a href="/media/static/app.html">our App</a>
        </span>
    </div>
</div>
</body>
</html>