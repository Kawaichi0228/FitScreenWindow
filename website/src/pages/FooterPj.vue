<template>
  <div id="footer-w">
    <div class="footer-component">
      <div class="column-main">
        <h2><img class="footer-logo" src="../assets/logo-long.png" alt="" /></h2>
        <p class="text-footer">選択中のアクティブなウィンドウを、すばやく画面にフィットすることができるWindows向けのアプリです。
          <br>
          <br>
          Free and Open Source software. Created by Kawaichi.
        </p>
      </div>

      <div class="column-sub">
        <h2>開発環境</h2>

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
        <h2>著作権</h2>
        <ul>
          <li class="text-footer">
            <a href="https://opensource.org/licenses/MIT">
              MIT
            </a>
            <span>(FitScreenWindow)</span>
          </li>
        </ul>
      </div>

      <div class="column-sub">
        <h2>連絡先</h2>

        <div>
          <!-- x-twitter -->
          <a href="http://twitter.com/kawaichi228" class="link-icon" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 1200 1227" width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="x-twitter">
              <path
                d="m714.163 519.284 446.727-519.284h-105.86l-387.893 450.887-309.809-450.887h-357.328l468.492 681.821-468.492 544.549h105.866l409.625-476.152 327.181 476.152h357.328l-485.863-707.086zm-144.998 168.544-47.468-67.894-377.686-540.2396h162.604l304.797 435.9906 47.468 67.894 396.2 566.721h-162.604l-323.311-462.446z" />
            </svg>
          </a>
          <!-- github -->
          <a href="http://github.com/kawaichi0228" class="link-icon" target="_blank" rel="noreferrer">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="github">
              <path
                d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
            </svg>
          </a>
        </div>
      </div>
    </div>

    <div id="footer-bottom">
      <p class="text-footer">© Kawaichi. All rights reserved</p>
    </div>

  </div>
</template>

<script>
</script>

<style lang="scss" scoped>
@import "../styles/base/_mixin.scss";
@import "../styles/base/_variables.scss";

#footer-w {
  background-color: $color-lightgray;
  font-size: $font-size-small;

  h2 {
    font-size: $font-size-base;
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
    margin: 10px 0px;
  }
}

.footer-component {
  padding: $section-padding;
  margin-right: 15%;

  text-align: left;
  display: inline-flex;

  @include tab {
    flex-direction: column;
  }
}

.column-main {
  margin-right: 20px;
  max-width: 350px;

  @include tab {
    margin: 0 0;
  }

  img.footer-logo {
    max-height: 55px;
    width: 100%;
    object-fit: contain;
    /* 画像縦横比を維持したまま、heightに対してリサイズする(ブロックに対してではない) */
  }
}

.column-sub {
  white-space: nowrap; // 改行を禁止
  max-width: 350px;
  margin: 0 40px;

  @include tab {
    margin: 0 0;
  }
}

.text-footer {
  @include vertical-center;

  img.item-img {
    --img-size: 20px; // 各言語のイメージサイズ
    height: var(--img-size);
    width: var(--img-size);
    margin-right: 13px;
  }
}

// -------------------------------------------------------------------------
// -------------------------------------------------------------------------
.link-icon {
  /* アイコン同士のマージン */
  margin: 0px 16px 0px 0px;

  @include tab {
    margin: 0px 8px 0px 8px;
  }

  .web-icon {
    font-size: 2em;
    /* アイコンの大きさ */
    padding: 0.3em;
    border-radius: 50%;
    background-color: $color-gray;

    &:hover {
      color: $color-gray;
    }
  }

  .x-twitter {
    filter: opacity(0.5);

    &:hover {
      filter: opacity(1);
    }
  }

  .github {
    filter: opacity(0.5);

    &:hover {
      filter: opacity(1);
    }
  }
}

div#footer-bottom {
  @include horizontal-center;
}
</style>
