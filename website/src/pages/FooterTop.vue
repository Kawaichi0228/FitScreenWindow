<template>
  <div id="footer-top">
    <div class="footer-component">
      <div class="column-main">
        <h2><img class="footer-logo" src="../assets/logo-long.png" alt=""/></h2>
        <p class="text-footer">アクティブウィンドウを、すばやく画面にフィットすることができるWindows向けのアプリです。
          <br>
          <br>
          Free Software, Created by Kawaichi
        </p>
      </div>

      <div class="column-sub">
        <h2>Made Possible By</h2>

        <ul>
          <li class="text-footer">
            <a href="https://www.python.org/">
              <img src="../assets/python.svg" class="item-img">
              <span>Python</span>
            </a>
          </li>
          <li class="text-footer">
            <a href="https://code.visualstudio.com/">
              <img src="../assets/vscode.svg" class="item-img">
              <span>Visual Studio Code</span>
            </a>
          </li>
          <li class="text-footer">
            <a href="https://github.com/">
              <img src="../assets/github.svg" class="item-img">
              <span>GitHub</span>
            </a>
          </li>
          <li class="text-footer">
            <a href="https://vuejs.org/index.html">
              <img src="../assets/vue.svg" class="item-img">
              <span>Vue.js</span>
            </a>
          </li>
          <li class="text-footer">
            <a href="https://www.w3.org/html/">
              <img src="../assets/html5.svg" class="item-img">
              <span>HTML5</span>
            </a>
          </li>
          <li class="text-footer">
            <a href="https://www.w3.org/Style/CSS/Overview.en.html">
              <img src="../assets/css3.svg" class="item-img">
              <span>CSS3</span>
            </a>
          </li>
          <li class="text-footer">
            <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference">
              <img src="../assets/javascript.svg" class="item-img">
              <span>JavaScript</span>
            </a>
          </li>
          <li class="text-footer">
            <a href="https://www.adobe.com/jp/products/illustrator.html">
              <img src="../assets/illustrator.svg" class="item-img">
              <span>Illustrator</span>
            </a>
          </li>
        </ul>

      </div>

      <div class="column-sub">
        <h2>Contact</h2>
        
        <div>
          <a
            href="http://twitter.com/kawaichi228"
            class="link-icon"
            target="_blank"
            rel="noreferrer"
            ><font-awesome-icon
              :icon="['fab', 'twitter']"
              class="web-icon twitter"
            />
          </a>
          <a
            href="http://github.com/kawaichi0228"
            class="link-icon"
            target="_blank"
            rel="noreferrer"
            ><font-awesome-icon
              :icon="['fab', 'github']"
              class="web-icon github"
          /></a>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
</script>

<style lang="scss" scoped>
@import "../base/_mixin.scss";

#footer-top {
  background-color: var(--theme-color-lightgray);

  text-align: left;
  padding-left: 40px;
  @include tab {
    text-align: center;
    padding: 30px 0px 30px 0px;
  }

  a {
      text-decoration: underline;

      // グレースケール有効
      filter: url("data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\'><filter id=\'grayscale\'><feColorMatrix type=\'matrix\' values=\'0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0 0 0 1 0\'/></filter></svg>#grayscale");
      filter: gray;
      -webkit-filter: grayscale(100%);

    &:hover {
      transition: 1ms;
      text-decoration: none;

      // グレースケール解除
      filter: none;
      -webkit-filter: grayscale(0%);
    }
  }

  li {
    margin: 12px 0px;
  }
}

.footer-component {
  text-align: left;
  display: inline-flex;
  padding-left: 5%;
  padding-right: 5%;
  padding: var(--section-padding);

  @include tab {
    text-align: center;
    flex-direction: column;
  }

  @include sp {
  }
}

.column-main {
  margin: 0 0px;
  max-width: 350px;

  img.footer-logo {
    height: 55px;
    object-fit: contain; /* 画像縦横比を維持したまま、heightに対してリサイズする(ブロックに対してではない) */

    // グレースケール有効
    //filter: url("data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\'><filter id=\'grayscale\'><feColorMatrix type=\'matrix\' values=\'0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0 0 0 1 0\'/></filter></svg>#grayscale");
    //filter: gray;
    //-webkit-filter: grayscale(100%);
  }
}

.column-sub {
  max-width: 350px;
  margin: 0 80px;
  @include tab {margin: 0 auto;}
}

.text-footer {
  font-weight: 400;
  // ---垂直中央寄せ---
  display: flex;
  flex-direction: row;
  align-items: center; // 垂直中央
  // -----------------------------
  img.item-img {
    --img-size: 23px; // 各言語のイメージサイズ
    height: var(--img-size);
    width: var(--img-size);
    margin-right: 15px;
  }
}
// -------------------------------------------------------------------------
// -------------------------------------------------------------------------
.link-icon {
  /* アイコン同士のマージン */
  margin: 0px 16px 0px 0px;
  @include tab {margin: 0px 8px 0px 8px;}
  .web-icon {
    font-size: 2em; /* アイコンの大きさ */
    padding: 0.3em;
    border-radius: 50%;
    background-color: var(--theme-color-gray);
    &:hover {color: var(--theme-color-gray);}
  }
    .twitter {
      color: var(--theme-color-white);
      &:hover {background-color: var(--theme-color-white);}
    }
    .github {
      color: var(--theme-color-white);
      &:hover {background-color: var(--theme-color-white);}
    }
}

</style>
