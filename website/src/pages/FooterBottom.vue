<template>
  <div id="footer-bottom">
    <p class="text-footer">© Kawaichi. All rights reserved</p>
  </div>
</template>

<style lang="scss" scoped>
@import "../styles/base/_variables.scss";

#footer-bottom {
  /* フッターのデフォルトマージンを削除 */
  width: 100%;
  position: absolute;
  /* 画面上部に固定(ブロック要素として扱われるため、一番上の要素が隠れない) */
  /*position: sticky;*/
  /*bottom: 0;*/

  font-size: $font-size-small;
  background-color: $color-lightgray;
}

</style>