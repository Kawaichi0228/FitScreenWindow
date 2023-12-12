<template>
  <div id="Demonstration">
    <section class="demonstration-section">
      <h1 id="content-title">選択中のウィンドウを すばやく画面にフィット</h1>
      <ul class="card-list">
        <li class="card">
          <img class="card-img" src="../assets/demonstration.gif" alt="">
          <div class="card-text">
            <p>選択中のアクティブなウィンドウに対して、ショートカットキーを押すごとに、画面の端に合わせて自動的に配置 & サイズを拡大(縮小)します。</p>
            <div class="line"></div>
            <p><b>- 初期ショートカットキー(変更可能) -</b></p>
            <p class="demo-hotkey">左方向へ配置：<b>Shift + Alt + ←</b></p>
            <p class="demo-hotkey">右方向へ配置：<b>Shift + Alt + →</b></p>
          </div>
        </li>
      </ul>
    </section>

    <section class="demonstration-settingmenu-section">
      <h2 id="content-title">サイズやショートカットキーなど 変更可能</h2>
      <ul class="card-list">
        <li class="card">
          <img class="card-img" src="../assets/demonstration-settingmenu.gif" alt="">
          <div class="card-text">
            <p>サイズやショートカットキーなどの各種設定は、タスクトレイからアプリを右クリックし、表示されたメニューの「設定」から変更可能です。</p>
          </div>
        </li>
      </ul>
    </section>
  </div>
</template>

<style lang="scss" scoped>
@import "../styles/base/_mixin.scss";
@import "../styles/base/_variables.scss";
@import "../styles/function/_rem.scss";

div#Demonstration {
  padding: $section-padding;
  background-color: $color-white;
}

// TODO: hrタグCSSを共通化
.line {
  border-top: 3px solid $color-lightgray;
  width: 80%;
  margin: 0 auto;
}

.demonstration-section {
  margin-bottom: 3.5rem;
}

.demonstration-settingmenu-section {
  /*  */
}

ul.card-list {}

li.card {
  display: inline-block;
  padding: rem(30) 0;
  max-width: rem(550);
  border-radius: 5px;
  box-shadow: 0 2px 5px #ccc;

  $_content-width: 85%;

  img.card-img {
    border-radius: 5px 5px 0 0;
    width: $_content-width; // 親要素に対してのwidth比率
  }

  div.card-text {
    width: $_content-width;
    margin: 0 auto;
    line-height: rem(30);
  }
}

.demo-hotkey {
  border: 2px solid $color-lightblue;
  background-color: $color-lightblue;
  color: $color-gray;
  text-decoration: none;
  margin-bottom: 25px;
  //width: 50%;
  padding: 1px 10px;
  border-radius: 5px;
}
</style>
