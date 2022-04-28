<template>
  <div id="Demonstration">
    <h1 id="content-title">選択中のウィンドウを すばやく画面にフィット</h1>
    <img id="main-image" src="../assets/demonstration.gif" alt="" />
    <p>画面にフィットさせたいウィンドウを選択した状態で<br>
    ショートカットキーを押すごとにサイズ変化 & 画面の端に<br>
    合わせるように自動的に配置します。</p>
    <p>[ショートカットキー]</p>
    <p>ウィンドウ左寄せ：Shift + Alt + ←</p>
    <p>ウィンドウ右寄せ：Shift + Alt + →</p>
  </div>
</template>

<style lang="scss" scoped>
@import "../styles/base/_mixin.scss";
@import "../styles/base/_variables.scss";
@import "../styles/function/_rem.scss";

div#Demonstration{
  padding: $section-padding;
  background-color: $color-white;
}

img#main-image{
  width: 100%;
  max-width: rem(500);
}

</style>
