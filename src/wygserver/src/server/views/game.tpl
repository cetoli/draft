<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <title>RTC Game</title>
        <link rel="stylesheet" href="/style.css" type="text/css" />
        <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
        <script src="http://cdn.peerjs.com/0.3/peer.js"></script>
        <script type="text/javascript" src="https://cdn.rawgit.com/brython-dev/brython/3.3.2/www/src/brython.js"></script>

        <script type="text/python">
            from rtcgame import main
            main({{lastid}},"{{ nodekey }}")
        </script>
    </head>
    <body onLoad="brython({debug:1, cache:'browser', static_stdlib_import:true})" background="https://i.imgur.com/IIY8Oj7.jpg">
           <div id="pydiv"  title="" style="width: 400px;
                height: 400px;
                position: absolute;
                top:0;
                bottom: 0;
                left: 0;
                right: 0;
                margin: auto;">
                <span style="color:white">LOADING..</span>
           </div>
    </body>
</html>