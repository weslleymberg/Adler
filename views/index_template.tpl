<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Adler</title>
    <style>
      .container {
        width: 90%;
        max-width: 850px;
        margin-left: auto;
        margin-right: auto;
      }

      .circle {
        width: 17px;
        height: 17px;
        border-radius: 50%;
        float: right;
      }

      .up{
        background: #2fcc66;
        margin-top: 3px;
      }

      .down {
        background: #F00;
        margin-top: 3px;
      }

      .text {
        color: rgba(51,51,51,.8);
        font-size: 1em;
        line-height: 1.5rem;
        vertical-align: middle;
        text-align: left;
        width: 40%;
        float:left;
      }

      .name {
        color: black;
      }

      .item {
        border-style: solid;
        border-color: #E0E0E0;
        border-bottom-width: 1px;
        border-radius: 4px;
        border-width: 1px;
        padding: 1.1rem 1.25rem 1rem;
        overflow: hidden;
        text-align: center;
      }

      .item form {
        float: left;
        margin-left: 75px;
      }

      .item form input {
        border: none;
        background: antiquewhite;
      }

      .overall-status {
        font-size: 1.25rem;
        border: 1px solid rgba(0,0,0,0.1);
        margin-bottom: 70px;
        padding: .75rem 1.25rem;
        border-radius: 4px;
        text-align: center;
        color: white;
      }

      .red {
        background: #F00;
      }

      .green {
        background: #2fcc66;
      }

      .orange {
        background: #F39631
      }

      header {
        background: rgb(19, 143, 108);
        height: 50px;
        color: white;
        margin-bottom: 50px;
        font-size: 2.5rem;
        padding-left: 5px;
      }

      header form {
        float: right;
        line-height: 0px;
        margin-top: 11px;
        margin-right: 5px;
      }

      body {
        margin: 0px;
      }

      .brand {

      }

    </style>
    <meta http-equiv="refresh" content="60">
  </head>
  <body>
    <header>
      <span>Adler</span>
    </header>
    <div class="container">
      %if all == True:
        <div class="overall-status green">
          <span>All sites online!</span>
        </div>
      %elif all == False and any == True:
        <div class="overall-status orange">
          <span>Oops! Not all sites are online.</span>
        </div>
      %elif any == False:
        <div class="overall-status red">
          <span>Wow! Something is really wrong.</span>
        </div>
      %end
      <div class="components">
        %for site in sites:
          <div class="item">
            <span class="text name">{{site['name']}}</span>
            <span class="text">{{site['url']}}</span>
            <form action="/deletesite" method="POST">
                <input type="hidden" name="site_id" value="{{site['id']}}">
                <input type="submit" value="Delete">
            </form>
            %if site['status']:
              <span class="circle up"></span>
            %else:
              <span class="circle down"></span>
            %end
          </div>
          %end
      </div>
    </div>
  </body>
</html>
